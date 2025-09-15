# 🎙️ Interview Learning Assistant

An AI-powered multi-agent system that transforms interview audio recordings into comprehensive learning documents with Q&A pairs and model answers using CrewAI.

## 📋 Overview

This project implements a sophisticated 6-agent sequential workflow that:
1. Transcribes interview audio using GPT-4o audio preview
2. Extracts every Q&A pair from the interview
3. Generates comprehensive model answers for each question
4. Analyzes performance gaps and learning opportunities
5. Formats everything into a clean study document
6. Exports results as structured markdown files

## 🚀 Features

- **Audio Transcription**: Supports MP3, WAV, M4A, OGG, and WebM formats (up to 20MB)
- **Complete Q&A Extraction**: Captures every single question and answer from the interview
- **Model Answer Generation**: Provides comprehensive correct answers for all questions
- **Topic Organization**: Groups related questions into logical sections
- **Learning Focused**: Designed for interview preparation and knowledge archiving
- **Multi-Model Support**: Uses optimized AI models for each specific task

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

### 1. Transcriptionist
- **Role**: Audio Intelligence Specialist
- **Model**: GPT-4o Audio Preview
- **Task**: Accurately transcribe audio to text

### 2. Dialogue Structurer
- **Role**: Interview Q&A Extractor
- **Model**: Google Gemini 2.5 Flash Lite
- **Task**: Extract ALL Q&A pairs and organize by topic

### 3. Technical Architect
- **Role**: Model Answer Creator
- **Model**: Google Gemini 2.5 Flash Lite
- **Task**: Generate comprehensive model answers for every question

### 4. Performance Analyst
- **Role**: Learning Performance Analyst
- **Model**: Google Gemini 2.5 Flash Lite
- **Task**: Compare answers and create learning roadmap

### 5. Quality Editor
- **Role**: Learning Document Creator
- **Model**: Google Gemini 2.5 Flash Lite
- **Task**: Format Q&As with model answers clearly

### 6. Notion Exporter
- **Role**: Digital Records Manager
- **Model**: Google Gemini 2.5 Flash Lite
- **Task**: Export and verify completeness

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

The learning document includes:

```markdown
# Interview Learning Document

## Interview Metadata
- Company: [Company Name]
- Role: [Position]
- Interviewer: [Name]
- Candidate: [Name]

## Topic: [e.g., Options Pricing]

### Question 1: [Exact question text]

**Candidate's Answer:**
[Complete answer from candidate]

**MODEL ANSWER:**
[Comprehensive correct answer with explanations]

**Key Learning Points:**
- Concept 1
- Concept 2

---
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
- All Agents: `google/gemini-2.5-flash-lite` (cost-effective and efficient)

## 🧪 Testing

To test with a sample audio file:
1. Place an interview audio file in the `audio/` directory
2. Run: `python src/main.py --audio audio/sample_interview.mp3`
3. Check the `interviews/` directory for the output

## 🤝 Contributing

This is a homework project, but suggestions and improvements are welcome!

## 📄 License

MIT License - See LICENSE file for details

## 🔮 Future Enhancements
- [ ] Coding interview support 
  - [ ] After transcription, new agent figures out is it live-coding interview or not
  - [ ] If it is, it routes to another agent that solves coding tasks 
  - [ ] After solving, it routes to another agent that checks the solution inside a code sandbox 

## 🙏 Acknowledgments

- CrewAI framework for multi-agent orchestration
- OpenRouter for unified AI model access
- MIT AI Studio for the assignment framework
---

**Built with CrewAI** | **Powered by OpenRouter**