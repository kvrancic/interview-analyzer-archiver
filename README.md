# 🎙️ Automated Internship Assistant

An AI-powered multi-agent system that analyzes interview audio recordings and provides comprehensive feedback using CrewAI and OpenRouter.

## 📋 Overview

This project implements a sophisticated 6-agent sequential workflow that:
1. Transcribes interview audio using GPT-4o audio preview
2. Structures the transcript into Q&A format
3. Analyzes technical responses with expert-level feedback
4. Provides holistic performance review
5. Ensures quality and coherence
6. Exports results to Notion or markdown

## 🚀 Features

- **Audio Transcription**: Supports MP3, WAV, M4A, OGG, and WebM formats (up to 20MB)
- **Intelligent Analysis**: Distinguishes between technical and behavioral questions
- **Expert Feedback**: Compares answers against ideal responses from a "Principal Engineer AI"
- **Performance Coaching**: Provides actionable feedback on both technical and communication skills
- **Flexible Export**: Saves to Notion database or local markdown files
- **Multi-Model Support**: Uses different AI models optimized for each task

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- OpenRouter API key (get one at [https://openrouter.ai/keys](https://openrouter.ai/keys))

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/internship-agent.git
cd internship-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys:
```bash
cp .env.example .env
# Edit .env and add your OPENROUTER_API_KEY
```

## 📖 Usage

### Basic Usage
```bash
python src/main.py --audio interview.mp3
```

### With Company and Role Information
```bash
python src/main.py --audio interview.mp3 --company "Tech Corp" --role "Software Engineer"
```

### Custom Output Directory
```bash
python src/main.py --audio interview.wav --output results/
```

### Command Line Options
- `--audio`: Path to the interview audio file (required)
- `--company`: Company name for the interview (default: "Unknown Company")
- `--role`: Role applied for (default: "Unknown Role")
- `--output`: Output directory for the analysis (default: "interviews/")

## 🤖 Agent Architecture

### 1. The Transcriptionist
- **Role**: Audio Intelligence Specialist
- **Model**: Google Gemini 2.0 Flash (via OpenRouter)
- **Task**: Accurately transcribe audio to text

### 2. The Dialogue Structurer
- **Role**: Interview Scribe & Organizer
- **Model**: Google Gemini 2.0 Flash
- **Task**: Parse transcript into Q&A format, tag technical questions

### 3. The Technical Solution Architect
- **Role**: Principal Engineer AI
- **Model**: Qwen 2.5 72B Instruct
- **Task**: Evaluate technical answers and provide ideal solutions

### 4. The Performance Analyst & Coach
- **Role**: AI Interview Coach
- **Model**: Google Gemini 2.0 Flash
- **Task**: Provide holistic performance review

### 5. The Quality Assurance Editor
- **Role**: Chief Editor AI
- **Model**: Google Gemini 2.0 Flash
- **Task**: Final review for coherence and accuracy

### 6. The Notion Exporter
- **Role**: Digital Records Manager
- **Model**: Google Gemini 2.0 Flash
- **Task**: Export to Notion or markdown format

## 📂 Project Structure

```
internship-agent/
├── src/
│   ├── agents/         # Agent definitions
│   ├── tasks/          # Task configurations
│   ├── tools/          # Custom tools (transcription, file writer, Notion)
│   ├── crew.py         # Main crew orchestration
│   └── main.py         # CLI entry point
├── config/
│   ├── agents.yaml     # Agent configurations
│   └── tasks.yaml      # Task configurations
├── audio/              # Input audio files
├── interviews/         # Output analysis reports
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md          # This file
```

## 📊 Output Format

The analysis report includes:

```markdown
# [Company] - [Role] Interview Analysis

## Overall Performance Summary
- Strengths
- Areas for Improvement

## Full Interview Transcript & Analysis

### Question 1: [Question]
**Your Answer:** [Candidate's response]
**Coach's Notes:** [Feedback]

### Question 2 [TECHNICAL]: [Technical Question]
**Your Answer:** [Candidate's response]
**Coach's Notes:** [Comparison with ideal answer]
**⭐ Ideal Answer:** [Expert-level response]
```

## 🔧 Configuration

### Environment Variables (.env)
```bash
# Required
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# Optional (for Notion export)
NOTION_TOKEN=your_notion_token_here
NOTION_DATABASE_ID=your_notion_database_id_here
```

### Model Configuration
Models can be changed in `config/agents.yaml`. Current models used:
- Transcription: `openai/gpt-4o-audio-preview`
- Analysis: `google/gemini-2.0-flash-exp:free`
- Technical Review: `qwen/qwen-2.5-72b-instruct`

## 🧪 Testing

To test with a sample audio file:
1. Place an interview audio file in the `audio/` directory
2. Run: `python src/main.py --audio audio/sample_interview.mp3`
3. Check the `interviews/` directory for the output

## 📝 Assignment Requirements

This project fulfills the MIT AI Studio homework requirements:
- ✅ Multiple agents with defined roles, goals, and backstories (6 agents)
- ✅ Multiple tasks with descriptions and expected outputs (6 sequential tasks)
- ✅ Terminal interaction via CLI
- ✅ Clean, well-documented Python code
- ✅ GitHub repository structure
- ✅ Comprehensive documentation

## 🤝 Contributing

This is a homework project, but suggestions and improvements are welcome!

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- CrewAI framework for multi-agent orchestration
- OpenRouter for unified AI model access
- MIT AI Studio for the assignment framework

## 💡 Future Enhancements

- [ ] Support for video interviews
- [ ] Real-time transcription during interviews
- [ ] Integration with calendar apps for scheduling
- [ ] Export to multiple formats (PDF, DOCX)
- [ ] Multi-language support
- [ ] Interview question bank suggestions

---

**Built with CrewAI** | **Powered by OpenRouter**