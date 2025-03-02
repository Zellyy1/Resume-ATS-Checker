import os
import sys
import json
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from openai import OpenAI

class ResumeATSCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume ATS Checker")
        self.root.geometry("900x700")
        self.root.configure(bg="#f5f5f5")
        
        self.resume_path = tk.StringVar()
        self.job_path = tk.StringVar()
        self.api_key = tk.StringVar()
        self.model = tk.StringVar(value="gpt-3.5-turbo")
        
        self.create_widgets()
        
        # Check for API key in environment
        env_api_key = os.environ.get('OPENAI_API_KEY', '')
        if env_api_key:
            self.api_key.set(env_api_key)
            self.api_key_entry.config(show="*")
    
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20, bg="#f5f5f5")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Resume ATS Checker", font=("Helvetica", 18, "bold"), 
                             bg="#f5f5f5", fg="#333")
        title_label.pack(pady=(0, 15))
        
        # Input section
        input_frame = tk.LabelFrame(main_frame, text="Input Settings", padx=15, pady=15, bg="#f5f5f5")
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Resume file
        resume_frame = tk.Frame(input_frame, bg="#f5f5f5")
        resume_frame.pack(fill=tk.X, pady=5)
        
        resume_label = tk.Label(resume_frame, text="Resume File:", width=15, anchor="w", bg="#f5f5f5")
        resume_label.pack(side=tk.LEFT)
        
        resume_entry = tk.Entry(resume_frame, textvariable=self.resume_path, width=50)
        resume_entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        
        resume_button = tk.Button(resume_frame, text="Browse", command=self.browse_resume)
        resume_button.pack(side=tk.LEFT)
        
        # Job description file
        job_frame = tk.Frame(input_frame, bg="#f5f5f5")
        job_frame.pack(fill=tk.X, pady=5)
        
        job_label = tk.Label(job_frame, text="Job Description:", width=15, anchor="w", bg="#f5f5f5")
        job_label.pack(side=tk.LEFT)
        
        job_entry = tk.Entry(job_frame, textvariable=self.job_path, width=50)
        job_entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        
        job_button = tk.Button(job_frame, text="Browse", command=self.browse_job)
        job_button.pack(side=tk.LEFT)
        
        # API Key
        api_frame = tk.Frame(input_frame, bg="#f5f5f5")
        api_frame.pack(fill=tk.X, pady=5)
        
        api_label = tk.Label(api_frame, text="OpenAI API Key:", width=15, anchor="w", bg="#f5f5f5")
        api_label.pack(side=tk.LEFT)
        
        self.api_key_entry = tk.Entry(api_frame, textvariable=self.api_key, width=50, show="*")
        self.api_key_entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        
        # Model selection
        model_frame = tk.Frame(input_frame, bg="#f5f5f5")
        model_frame.pack(fill=tk.X, pady=5)
        
        model_label = tk.Label(model_frame, text="GPT Model:", width=15, anchor="w", bg="#f5f5f5")
        model_label.pack(side=tk.LEFT)
        
        models = ["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"]
        model_dropdown = ttk.Combobox(model_frame, textvariable=self.model, values=models)
        model_dropdown.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        
        # Analyze button
        button_frame = tk.Frame(main_frame, bg="#f5f5f5")
        button_frame.pack(fill=tk.X, pady=10)
        
        analyze_button = tk.Button(button_frame, text="Analyze Resume", 
                                command=self.analyze_resume, bg="#4CAF50", fg="white",
                                font=("Helvetica", 12), padx=15, pady=5)
        analyze_button.pack()
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, orient="horizontal", 
                                      length=100, mode="indeterminate")
        self.progress.pack(fill=tk.X, pady=10)
        
        # Results section
        results_frame = tk.LabelFrame(main_frame, text="Analysis Results", padx=15, pady=15, bg="#f5f5f5")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, wrap=tk.WORD, 
                                                   font=("Courier", 10))
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def browse_resume(self):
        filename = filedialog.askopenfilename(
            title="Select Resume File",
            filetypes=(("Text files", "*.txt"), ("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        if filename:
            self.resume_path.set(filename)
    
    def browse_job(self):
        filename = filedialog.askopenfilename(
            title="Select Job Description File",
            filetypes=(("Text files", "*.txt"), ("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        if filename:
            self.job_path.set(filename)
    
    def read_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            self.status_var.set(f"Error reading file: {e}")
            return None
    
    def analyze_resume(self):
        # Check if files are selected
        if not self.resume_path.get() or not self.job_path.get():
            self.status_var.set("Error: Please select both resume and job description files")
            return
        
        # Check if API key is provided
        if not self.api_key.get():
            self.status_var.set("Error: Please enter your OpenAI API key")
            return
        
        # Clear results and update status
        self.results_text.delete(1.0, tk.END)
        self.status_var.set("Analyzing resume against job description...")
        self.progress.start()
        
        # Load files
        resume_text = self.read_file(self.resume_path.get())
        job_text = self.read_file(self.job_path.get())
        
        if not resume_text or not job_text:
            self.progress.stop()
            return
        
        # Run analysis in a separate thread to avoid freezing UI
        self.root.after(100, lambda: self.run_analysis(resume_text, job_text))
    
    def run_analysis(self, resume_text, job_text):
        try:
            client = OpenAI(api_key=self.api_key.get())
            
            prompt = f"""
            You are an ATS (Applicant Tracking System) analyzer. Evaluate the compatibility between 
            the resume and job description below.
            
            Resume:
            {resume_text}
            
            Job Description:
            {job_text}
            
            Provide a JSON response with the following:
            1. "match_score": A percentage (0-100) representing overall match
            2. "missing_keywords": List of important keywords from the job description missing in the resume
            3. "recommendations": List of specific improvements
            4. "strengths": List of areas where the resume aligns well with the job
            5. "ats_readability": Assessment of format/structure for ATS systems
            """
            
            response = client.chat.completions.create(
                model=self.model.get(),
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "You analyze resumes against job descriptions and provide structured feedback in JSON format."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            analysis = json.loads(response.choices[0].message.content)
            self.display_results(analysis)
            
            # Save results
            with open('ats_analysis_results.json', 'w') as f:
                json.dump(analysis, f, indent=2)
            
            self.status_var.set("Analysis complete. Results saved to ats_analysis_results.json")
            
        except Exception as e:
            self.results_text.insert(tk.END, f"Error calling OpenAI API: {e}\n\n")
            self.results_text.insert(tk.END, "Check your API key and internet connection.")
            self.status_var.set("Error during analysis")
        
        finally:
            self.progress.stop()
    
    def display_results(self, analysis):
        self.results_text.delete(1.0, tk.END)
        
        self.results_text.insert(tk.END, "===== RESUME ATS ANALYSIS =====\n\n")
        
        self.results_text.insert(tk.END, f"🎯 Match Score: {analysis['match_score']}%\n\n")
        
        self.results_text.insert(tk.END, "📋 ATS Readability Assessment:\n")
        self.results_text.insert(tk.END, f"  {analysis['ats_readability']}\n\n")
        
        self.results_text.insert(tk.END, "💪 Strengths:\n")
        for strength in analysis["strengths"]:
            self.results_text.insert(tk.END, f"  ✓ {strength}\n")
        self.results_text.insert(tk.END, "\n")
        
        self.results_text.insert(tk.END, "🚩 Missing Keywords:\n")
        for keyword in analysis["missing_keywords"]:
            self.results_text.insert(tk.END, f"  ✗ {keyword}\n")
        self.results_text.insert(tk.END, "\n")
        
        self.results_text.insert(tk.END, "🔧 Recommendations:\n")
        for i, rec in enumerate(analysis["recommendations"], 1):
            self.results_text.insert(tk.END, f"  {i}. {rec}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeATSCheckerGUI(root)
    root.mainloop()
