#!/usr/bin/env python3
"""
Automated Internship Assistant - Main Entry Point

This tool analyzes interview audio recordings and provides comprehensive feedback.
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv


def validate_audio_file(file_path: str) -> bool:
    """Validate that the audio file exists and has a supported format."""
    if not os.path.exists(file_path):
        print(f"Error: Audio file not found: {file_path}")
        return False

    supported_formats = ['.mp3', '.wav', '.m4a', '.ogg', '.webm']
    file_ext = Path(file_path).suffix.lower()

    if file_ext not in supported_formats:
        print(f"Error: Unsupported audio format '{file_ext}'")
        print(f"Supported formats: {', '.join(supported_formats)}")
        return False

    # Check file size (20MB limit for GPT-4o audio)
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if file_size_mb > 20:
        print(f"Error: Audio file too large ({file_size_mb:.1f}MB). Maximum size is 20MB.")
        return False

    return True


def main():
    """Main entry point for the Interview Assistant."""
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Automated Internship Assistant - Analyze interview audio and provide comprehensive feedback",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/main.py --audio interview.mp3
  python src/main.py --audio interview.mp3 --company "Tech Corp" --role "Software Engineer"
  python src/main.py --audio interview.wav --output custom_output_dir/

For more information, see README.md
        """
    )

    parser.add_argument(
        '--audio',
        type=str,
        required=True,
        help='Path to the interview audio file (mp3, wav, m4a, ogg, webm)'
    )

    parser.add_argument(
        '--company',
        type=str,
        default='Unknown Company',
        help='Company name for the interview (default: Unknown Company)'
    )

    parser.add_argument(
        '--role',
        type=str,
        default='Unknown Role',
        help='Role applied for (default: Unknown Role)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='interviews/',
        help='Output directory for the analysis (default: interviews/)'
    )

    # Parse arguments
    args = parser.parse_args()

    # Load environment variables
    load_dotenv()

    # Check for API key
    if not os.getenv('OPENROUTER_API_KEY'):
        print("\n" + "=" * 60)
        print("ERROR: OpenRouter API key not found!")
        print("=" * 60)
        print("\nPlease set up your API key:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenRouter API key to the .env file")
        print("3. Get your API key from: https://openrouter.ai/keys")
        print("\nExample:")
        print("  cp .env.example .env")
        print("  # Edit .env and add your OPENROUTER_API_KEY")
        return 1

    # Validate audio file
    if not validate_audio_file(args.audio):
        return 1

    # Import crew (do this after env check to avoid import errors)
    try:
        from src.crew import InterviewAssistantCrew
    except ImportError as e:
        print(f"\nError importing crew: {e}")
        print("Please ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        return 1

    # Display startup information
    print("\n" + "=" * 60)
    print("🎙️  AUTOMATED INTERNSHIP ASSISTANT")
    print("=" * 60)
    print(f"Audio File: {args.audio}")
    print(f"Company: {args.company}")
    print(f"Role: {args.role}")
    print(f"Output Directory: {args.output}")
    print("=" * 60 + "\n")

    try:
        # Initialize the crew
        crew = InterviewAssistantCrew()

        # Prepare inputs
        inputs = {
            'audio_path': args.audio,
            'company': args.company,
            'role': args.role,
            'output_dir': args.output
        }

        # Execute the analysis
        result = crew.kickoff(inputs)

        # Display result
        print("\n" + "=" * 60)
        print("✅ ANALYSIS COMPLETE")
        print("=" * 60)
        print("\nYour interview analysis has been saved.")
        print(f"Check the '{args.output}' directory for the detailed report.")

        return 0

    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user.")
        return 1
    except Exception as e:
        print(f"\n\nError during analysis: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())