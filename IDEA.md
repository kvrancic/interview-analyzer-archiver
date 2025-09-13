# The Automated Internship Assistant

---

### 1. The Expanded CrewAI Agent Roster

We now need a larger, more specialized crew.

**Agent 1: The Transcriptionist**

*   **Role:** Audio Intelligence Specialist
*   **Goal:** To accurately transcribe spoken words from an audio file into a clean, readable text format.
*   **Backstory:** An AI agent powered by the latest speech-to-text models, ensuring the highest possible accuracy for the raw transcript that forms the foundation for all further analysis.
*   **Tools:** Custom `TranscriptionTool` (using GPT-4o audio preview via OpenRouter).
*   **Model:** google/gemini-2.5-flash-lite

**Agent 2: The Dialogue Structurer**

*   **Role:** Interview Scribe & Organizer
*   **Goal:** To parse the raw text transcript, structure it into a clear Question and Answer format, and most importantly, **tag questions that are clearly technical in nature.**
*   **Backstory:** A meticulous organizer who can easily distinguish between behavioral questions ("Tell me about a time...") and technical questions ("Explain the difference between SQL and NoSQL..."). Your output clearly separates dialogue turns and flags technical challenges for the specialist agents.
*   **Tools:** None needed (relies on LLM's analytical ability).
*   **Model:** google/gemini-2.5-flash-lite

**Agent 3: The Technical Solution Architect (The New "Task Solver")**

*   **Role:** Principal Engineer AI
*   **Goal:** For each tagged technical question, first evaluate the candidate's provided answer for accuracy and completeness. Then, generate a detailed, comprehensive, and perfectly explained "ideal answer" as if it were for a textbook or official documentation.
*   **Backstory:** You are an AI modeled on a FAANG principal engineer who is also a renowned technical author and conference speaker. You have an encyclopedic knowledge of software engineering principles, data structures, algorithms, and system design. Your answers are not just correct; they are clear, well-structured, and include best practices and trade-offs.
*   **Model:** qwen/qwen3-next-80b-a3b-thinking

**Agent 4: The Performance Analyst & Coach**

*   **Role:** AI Interview Coach
*   **Goal:** To synthesize the structured dialogue and the analysis from the Technical Solution Architect to provide a holistic performance review.
*   **Backstory:** A seasoned career coach who now has a technical expert on their team. You analyze the candidate's communication of their technical knowledge by **comparing their answer to the "ideal answer."** You also evaluate their responses to behavioral questions, focusing on structure (like the STAR method), clarity, and confidence.
*   **Tools:** None needed.
*   **Model:** google/gemini-2.5-flash-lite

**Agent 5: The Quality Assurance Editor (The New "Tester")**

*   **Role:** Chief Editor AI
*   **Goal:** To perform a final review of the entire compiled report (Structured Q&A, Ideal Answers, and Performance Review) before it's sent to the user. You check for coherence, consistency in tone, factual accuracy, and ensure the feedback is constructive and easy to understand.
*   **Backstory:** You are a meticulous editor with an obsessive eye for detail. You are the final quality gate. Your job is to catch any errors, awkward phrasing, or AI hallucinations from the previous agents, ensuring the final product is polished, professional, and trustworthy.
*   **Tools:** None needed.
*   **Model:** google/gemini-2.5-flash-lite

**Agent 6: The Notion Exporter**

*   **Role:** Digital Records Manager
*   **Goal:** To take the final, QA-approved report and create a new, beautifully formatted entry in the user's specified Notion database.
*   **Backstory:** An automation wizard who is an expert with the Notion MCP server , ensuring that all valuable insights are saved perfectly.
*   **Tools:** Notion MCP server

---

### 2. The Enhanced Sequential Workflow

The `Crew` will still use a `Process.sequential` workflow, but with more steps and more complex data being passed between tasks.

1.  **Task 1 (Transcriptionist):** Transcribe the audio from the provided MP3 file.
    *   **Expected Output:** A single block of text.

2.  **Task 2 (Dialogue Structurer):** Ingest the text from Task 1. Reformat it into a Q&A script and add a `[TECHNICAL]` tag next to any question that requires a technical explanation.
    *   **Expected Output:** A structured text file, e.g., `"Interviewer: [TECHNICAL] What is the event loop in JavaScript?"\n"Candidate: It's what allows Node.js to perform non-blocking I/O..."`

3.  **Task 3 (Technical Solution Architect):** Ingest the structured script from Task 2. For every question tagged `[TECHNICAL]`, generate an "Ideal Answer."
    *   **Expected Output:** A document containing each technical question, the candidate's answer, and a new "Ideal Answer" section for each.

4.  **Task 4 (Performance Analyst):** Ingest the outputs from Task 2 (full dialogue) and Task 3 (technical analysis). Generate a full performance review, including analysis of behavioral questions and a comparison of the candidate's technical answers to the ideal ones.
    *   **Expected Output:** A complete performance report with sections like "Strengths," "Areas for Improvement," etc.

5.  **Task 5 (Quality Assurance Editor):** Ingest the outputs from Task 2, 3, and 4 to form a complete draft. Review the entire document for quality, coherence, and accuracy. Make any necessary edits to create the final, polished report.
    *   **Expected Output:** The final, approved version of the full interview analysis.

6.  **Task 6 (Notion Exporter):** Ingest the final report from Task 5. Format it and create a new page in the specified Notion database.
    *   **Expected Output:** A success or failure message.

---

### 3. Model Selection & Implementation

always use openrouter: https://openrouter.ai/docs/quickstart
model for transcription = openai/gpt-4o-audio-preview (via OpenRouter)
model_for_structuring = google/gemini-2.5-flash-lite
model for technical solution architect = qwen/qwen3-next-80b-a3b-thinking
model for quality assurance editor = google/gemini-2.5-flash-lite
notion exporter info: https://github.com/makenotion/notion-mcp-server

---

### 4. The Updated Notion Output

The final page created in the user's Notion database should have a clear, rich structure.

*   **Page Title:** [Company Name] - [Role Applied For] Interview

*   **Properties:**
    *   `Company`: [Company Name]
    *   `Role`: [Role]
    *   `Date`: [Date of run]

*   **Page Body (Content generated by the crew):**
    *   **Overall Performance Summary**
        *   What Went Well
        *   Key Areas for Improvement
    *   **Full Interview Transcript & Analysis**
        *   **Question 1:** [Interviewer's Question]
            *   **Your Answer:** [Candidate's full answer]
            *   **Coach's Notes:** [Feedback on this specific answer from the Performance Analyst]
        *   **Question 2 [TECHNICAL]:** [Interviewer's technical question]
            *   **Your Answer:** [Candidate's full answer]
            *   **Coach's Notes:** [Feedback comparing your answer to the ideal one]
            *   **⭐ Ideal Answer (Provided by Solution Architect):** [The comprehensive, correct answer]
        *   *(...and so on for all questions)*
