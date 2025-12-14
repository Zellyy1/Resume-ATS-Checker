# Resume ATS Analyzer

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![React](https://img.shields.io/badge/React-18-61dafb.svg)
![AI Powered](https://img.shields.io/badge/AI-Powered-orange.svg)

**AI-powered resume analysis tool with comprehensive skill gap identification and personalized learning recommendations**

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [API Setup](#api-setup) • [Customization](#customization)

</div>

---

## 📋 Overview

Resume ATS Analyzer is a modern, sleek web application that leverages OpenAI's GPT-4 to provide comprehensive resume analysis against job descriptions. It identifies skill gaps, provides actionable recommendations, and suggests curated learning resources to help candidates improve their job match score.

## ✨ Features

### 🎯 Core Functionality

- **ATS Compatibility Analysis**: Evaluates resume format and structure for Applicant Tracking Systems
- **Match Score Calculation**: Overall percentage match between resume and job requirements
- **Skill Gap Identification**: Pinpoints missing skills with importance ratings (1-10 scale)
- **Learning Resources**: Curated recommendations from Coursera, Udemy, YouTube, and other platforms
- **Experience Gap Analysis**: Compares required vs. actual years of experience

### 📊 Visualizations

- **Radar Chart**: Category breakdown (Technical Skills, Experience, Education, Soft Skills)
- **Bar Chart**: Skill importance levels with visual indicators
- **Progress Bars**: Individual skill gap importance visualization
- **Score Circle**: Animated circular progress indicator for overall match

### 🎨 Customization

- **Theme Presets**: 6 beautiful pre-designed color schemes
  - Indigo Night (Default)
  - Cyan Dreams
  - Purple Haze
  - Emerald Forest
  - Rose Garden
  - Amber Glow
- **Custom Colors**: Full control over accent, background, and text colors
- **Real-time Updates**: Instant preview of theme changes

### 📁 File Support

- **Resume Formats**: LaTeX (.tex), PDF, TXT, DOCX
- **Job Descriptions**: TXT, PDF, DOCX
- **Drag & Drop**: Easy file upload interface

---

## 🚀 Demo

### Interface Preview

```
┌─────────────────────────────────────────────────┐
│  Resume ATS Analyzer              [⚙ Settings]  │
│  AI-powered resume analysis                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  [OpenAI API Key Input]                        │
│                                                 │
│  ┌──────────────┐  ┌──────────────┐           │
│  │   Upload     │  │   Upload     │           │
│  │   Resume     │  │   Job Desc   │           │
│  └──────────────┘  └──────────────┘           │
│                                                 │
│         [Analyze Resume Button]                │
│                                                 │
│  ┌─────────────────────────────────────────┐  │
│  │  Score: 85%  [Radar Chart] [Bar Chart] │  │
│  │  Learning Resources                      │  │
│  │  Strengths | Missing Keywords            │  │
│  └─────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## 📦 Installation

### Option 1: Direct Usage (Recommended)

1. Download the `resume-ats-enhanced.html` file
2. Open it in any modern web browser (Chrome, Firefox, Safari, Edge)
3. No installation or build process required!

### Option 2: Local Development

```bash
# Clone or download the repository
git clone https://github.com/yourusername/resume-ats-analyzer.git

# Navigate to the project directory
cd resume-ats-analyzer

# Open the HTML file
open resume-ats-enhanced.html  # macOS
start resume-ats-enhanced.html # Windows
xdg-open resume-ats-enhanced.html # Linux
```

---

## 🔑 API Setup

### Getting Your OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to **API Keys** section
4. Click **"Create new secret key"**
5. Copy your API key (starts with `sk-`)
6. Paste it into the application's API Key field

### API Costs

The application uses the **GPT-4o** model. Typical costs per analysis:

- Average tokens per request: ~2,000-4,000
- Estimated cost: $0.01 - $0.03 per analysis
- [OpenAI Pricing Details](https://openai.com/pricing)

> **Note**: Your API key is only stored in your browser session and is never transmitted anywhere except to OpenAI's servers.

---

## 💡 Usage

### Step-by-Step Guide

1. **Enter API Key**
   ```
   Paste your OpenAI API key in the top input field
   ```

2. **Upload Resume**
   ```
   • Drag & drop your resume file
   • Or click to browse and select
   • Supports: .tex, .txt, .pdf, .docx
   ```

3. **Upload Job Description**
   ```
   • Drag & drop the job description
   • Or click to browse and select
   • Supports: .txt, .pdf, .docx
   ```

4. **Analyze**
   ```
   Click "Analyze Resume" button
   Wait for AI analysis (10-30 seconds)
   ```

5. **Review Results**
   ```
   • Overall match score
   • Category breakdowns
   • Skill gaps with learning resources
   • Experience analysis
   • Recommendations
   ```

---

## 🎨 Customization

### Using Preset Themes

1. Click the **Settings** (⚙) button in the top-right
2. Choose from 6 preset themes:
   - **Indigo Night**: Professional blue-purple tones
   - **Cyan Dreams**: Cool aqua and teal palette
   - **Purple Haze**: Rich purple gradients
   - **Emerald Forest**: Natural green shades
   - **Rose Garden**: Warm pink and red hues
   - **Amber Glow**: Golden orange accents

### Custom Color Configuration

Fine-tune your theme with custom colors:

| Color Property | Description | Default Value |
|---------------|-------------|---------------|
| Accent Color | Primary interactive elements | `#6366f1` |
| Background Primary | Main page background | `#09090b` |
| Background Secondary | Card backgrounds | `#18181b` |
| Background Tertiary | Input fields | `#27272a` |
| Text Primary | Headings and labels | `#e4e4e7` |
| Text Secondary | Body text | `#a1a1aa` |

---

## 📊 Analysis Output Structure

### JSON Response Format

The AI returns a comprehensive analysis with the following structure:

```json
{
  "match_score": 85,
  "category_scores": [
    { "category": "Technical Skills", "score": 90 },
    { "category": "Experience", "score": 75 },
    { "category": "Education", "score": 95 },
    { "category": "Soft Skills", "score": 80 }
  ],
  "skill_gaps": [
    {
      "skill": "Kubernetes",
      "importance": 9,
      "learning_resources": [
        {
          "title": "Kubernetes for Beginners",
          "url": "https://...",
          "platform": "Coursera"
        }
      ]
    }
  ],
  "experience_gap": {
    "required_years": 5,
    "candidate_years": 3,
    "gap_analysis": "..."
  },
  "top_resources": [...],
  "strengths": [...],
  "missing_keywords": [...],
  "recommendations": [...],
  "ats_readability": "..."
}
```

---

## 🛠️ Technical Stack

### Frontend Technologies

- **React 18**: UI component library
- **Chart.js**: Data visualization
- **Tailwind CSS**: Utility-first styling
- **Babel Standalone**: In-browser JSX transpilation

### Fonts

- **Syne**: Modern display font for headings
- **IBM Plex Mono**: Professional monospace for code and data

### APIs

- **OpenAI GPT-4o**: Resume analysis and recommendations
- Model: `gpt-4o`
- Response format: Structured JSON

---

## 🔒 Privacy & Security

- ✅ **Local Processing**: All file reading happens in your browser
- ✅ **No Server Storage**: Files are never uploaded to any server
- ✅ **API Key Security**: Stored only in browser session storage
- ✅ **Direct API Calls**: Communication only with OpenAI servers
- ⚠️ **HTTPS Recommended**: Use secure connections when possible

---

## 🐛 Troubleshooting

### Common Issues

**1. "API Error: 401 Unauthorized"**
```
Solution: Check that your API key is correct and has not expired
```

**2. "API Error: 429 Too Many Requests"**
```
Solution: You've exceeded your rate limit. Wait a few minutes or upgrade your OpenAI plan
```

**3. Charts not displaying**
```
Solution: Ensure JavaScript is enabled and you're using a modern browser
```

**4. File upload not working**
```
Solution: Check file format and size. Try converting to .txt format
```

**5. Theme colors not changing**
```
Solution: Refresh the page and try again. Check browser console for errors
```

### Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Fully Supported |
| Firefox | 88+ | ✅ Fully Supported |
| Safari | 14+ | ✅ Fully Supported |
| Edge | 90+ | ✅ Fully Supported |
| Opera | 76+ | ✅ Fully Supported |

---

## 📈 Roadmap

### Planned Features

- [ ] **PDF Export**: Download analysis results as PDF
- [ ] **Resume Templates**: ATS-friendly resume templates
- [ ] **Batch Analysis**: Compare multiple resumes at once
- [ ] **Cover Letter Generator**: AI-powered cover letter creation
- [ ] **Interview Prep**: Question generation based on job description
- [ ] **Browser Extension**: Quick analysis from job boards
- [ ] **Local Storage**: Save analysis history
- [ ] **LinkedIn Integration**: Import profile data directly

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue with details
2. **Suggest Features**: Share your ideas in discussions
3. **Submit PRs**: Fork, create a branch, and submit a pull request
4. **Improve Docs**: Help make documentation clearer

### Development Guidelines

- Keep the single-file architecture for easy distribution
- Maintain the minimalistic, sleek design philosophy
- Test across multiple browsers before submitting
- Follow the existing code style and naming conventions

---

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 Resume ATS Analyzer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **OpenAI**: For providing the GPT-4 API
- **Chart.js**: For beautiful data visualizations
- **React Team**: For the amazing UI library
- **Tailwind CSS**: For the utility-first CSS framework
- **Google Fonts**: For Syne and IBM Plex Mono fonts

---

## 📞 Support

Need help? Here's how to get support:

- 📧 **Email**: premnath4th@gmail.com

---

## ⭐ Star History

If you find this project useful, please consider giving it a star on GitHub!

---

<div align="center">

**Made with ❤️ for job seekers everywhere**

[Back to Top](#resume-ats-analyzer)

</div>
