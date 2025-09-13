#!/usr/bin/env python3
"""
Simplified interview processing script that saves intermediary results.
"""
import os
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def process_transcription(transcription: str, output_dir: Path):
    """Process transcription through each agent step by step."""

    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found")

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    # Step 1: Structure the dialogue
    print("\n📋 Step 1: Structuring dialogue...")
    structured_prompt = f"""
    You are a dialogue structurer. Take this interview transcription and structure it into a clear format.

    Format it as:
    - Interviewer questions/statements
    - Candidate responses
    - Topic transitions
    - Key technical discussions

    Transcription:
    {transcription[:8000]}  # Limit for context

    Please structure this dialogue clearly with proper formatting.
    """

    response = client.chat.completions.create(
        model="openrouter/google/gemini-2.5-flash-lite",
        messages=[{"role": "user", "content": structured_prompt}],
        temperature=0.7
    )

    structured_dialogue = response.choices[0].message.content

    # Save structured dialogue
    structured_file = output_dir / "1_structured_dialogue.md"
    with open(structured_file, 'w') as f:
        f.write("# Structured Dialogue\n\n")
        f.write(structured_dialogue)
    print(f"   ✅ Saved to {structured_file}")

    # Step 2: Technical Analysis
    print("\n📋 Step 2: Analyzing technical content...")
    technical_prompt = f"""
    You are a technical analyst. Analyze this interview for technical topics discussed.

    Focus on:
    - Technical concepts mentioned (options, delta, probability, etc.)
    - Accuracy of candidate's technical knowledge
    - Problem-solving approach
    - Mathematical/statistical understanding

    Interview content:
    {transcription[:8000]}

    Provide a detailed technical analysis.
    """

    response = client.chat.completions.create(
        model="openrouter/qwen/qwen3-next-80b-a3b-instruct",
        messages=[{"role": "user", "content": technical_prompt}],
        temperature=0.7
    )

    technical_analysis = response.choices[0].message.content

    # Save technical analysis
    technical_file = output_dir / "2_technical_analysis.md"
    with open(technical_file, 'w') as f:
        f.write("# Technical Analysis\n\n")
        f.write(technical_analysis)
    print(f"   ✅ Saved to {technical_file}")

    # Step 3: Performance Review
    print("\n📋 Step 3: Evaluating performance...")
    performance_prompt = f"""
    You are a performance evaluator. Review this interview and assess the candidate's performance.

    Evaluate:
    - Communication skills
    - Technical competence
    - Problem-solving ability
    - Areas of strength
    - Areas for improvement
    - Overall recommendation

    Interview content:
    {transcription[:8000]}

    Technical analysis:
    {technical_analysis[:2000]}

    Provide a comprehensive performance review.
    """

    response = client.chat.completions.create(
        model="openrouter/google/gemini-2.5-flash-lite",
        messages=[{"role": "user", "content": performance_prompt}],
        temperature=0.7
    )

    performance_review = response.choices[0].message.content

    # Save performance review
    performance_file = output_dir / "3_performance_review.md"
    with open(performance_file, 'w') as f:
        f.write("# Performance Review\n\n")
        f.write(performance_review)
    print(f"   ✅ Saved to {performance_file}")

    # Step 4: Final Report
    print("\n📋 Step 4: Creating final report...")
    final_prompt = f"""
    Create a comprehensive final interview report combining all analyses.

    Include:
    1. Executive Summary
    2. Interview Overview (company: DaVinci, role: Quant Trader)
    3. Technical Assessment Summary
    4. Performance Highlights
    5. Recommendations
    6. Overall Rating

    Based on:
    - Structured dialogue
    - Technical analysis: {technical_analysis[:1500]}
    - Performance review: {performance_review[:1500]}

    Format as a professional interview assessment report.
    """

    response = client.chat.completions.create(
        model="openrouter/google/gemini-2.5-flash-lite",
        messages=[{"role": "user", "content": final_prompt}],
        temperature=0.7
    )

    final_report = response.choices[0].message.content

    # Save final report
    final_file = output_dir / "4_final_report.md"
    with open(final_file, 'w') as f:
        f.write("# Interview Analysis Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Company:** DaVinci Trading\n")
        f.write(f"**Role:** Quant Trader\n")
        f.write(f"**Candidate:** Vica\n\n")
        f.write("---\n\n")
        f.write(final_report)
    print(f"   ✅ Saved to {final_file}")

    # Save metadata
    metadata = {
        "processing_date": datetime.now().isoformat(),
        "company": "DaVinci Trading",
        "role": "Quant Trader",
        "candidate": "Vica",
        "interviewer": "Kevin",
        "steps_completed": [
            "transcription",
            "dialogue_structuring",
            "technical_analysis",
            "performance_review",
            "final_report"
        ],
        "output_files": [
            str(structured_file),
            str(technical_file),
            str(performance_file),
            str(final_file)
        ]
    }

    metadata_file = output_dir / "metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"\n✅ All processing complete! Results saved in {output_dir}")
    return final_report


if __name__ == "__main__":
    # Load the transcription from the successful run
    transcription = """Speaker 1: Hey.

Speaker 2: Hi.

Speaker 1: Sorry, one second, I can't hear you.

Speaker 2: Hi, can you hear me now?

Speaker 1: Ok, cool, cool cool. Hey, how's it going, thanks for joining.

Speaker 2: Awesome, you?

Speaker 1: Yeah, not bad. So yeah, before we get started with the technical part of the interview, if I just quickly introduce myself. So I'm Kevin, I'm a quant researcher at DaVinci. I've been in the company for two years. I started in Amsterdam on the digital assets desk, and recently I moved to Hong Kong to help start the team here. Maybe you can tell me a little bit about yourself?

Speaker 2: Yeah, so I'm Vica, I'm currently— I just finished my third year of mathematics, so my bachelor's degree, and my plan is to enroll in Masters of Statistics here in Zagreb. I'm also part member of a finance club where I'm in a group called algorithmic analysis and market modeling. That's when I really started to be interested in trading, and also we as members of that group also compete in, let's say, some hackathons and things like that. For example, Algo trading hackathon, which my team this year was first. So I'm really proud of that. And yeah, except for that, I really like probability, statistics, and thinking in that way."""

    # Continue with rest of transcription...
    # For now using just the beginning for testing

    # Create output directory
    output_dir = Path("interviews") / f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save the full transcription first
    transcription_file = output_dir / "0_transcription.txt"
    with open(transcription_file, 'w') as f:
        f.write(transcription)
    print(f"Transcription saved to {transcription_file}")

    # Process the transcription
    process_transcription(transcription, output_dir)