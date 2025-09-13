#!/usr/bin/env python3
"""
Test setup script to verify the installation and configuration.
"""

import os
import sys
from dotenv import load_dotenv


def check_environment():
    """Check if the environment is properly configured."""
    print("🔍 Checking environment setup...")
    print("-" * 50)

    # Load environment variables
    load_dotenv()

    # Check Python version
    python_version = sys.version_info
    print(f"✓ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("  ⚠️  Warning: Python 3.8+ is recommended")

    # Check for .env file
    if os.path.exists('.env'):
        print("✓ .env file found")
    else:
        print("✗ .env file not found - please copy .env.example to .env")
        return False

    # Check for API key
    api_key = os.getenv('OPENROUTER_API_KEY')
    if api_key and api_key != 'your_openrouter_api_key_here':
        print(f"✓ OpenRouter API key configured (length: {len(api_key)})")
    else:
        print("✗ OpenRouter API key not configured")
        print("  Please add your API key to the .env file")
        print("  Get your key at: https://openrouter.ai/keys")
        return False

    # Check directories
    directories = ['src', 'config', 'audio', 'interviews']
    for directory in directories:
        if os.path.exists(directory):
            print(f"✓ Directory exists: {directory}/")
        else:
            print(f"✗ Directory missing: {directory}/")
            return False

    # Check key files
    files = [
        'src/main.py',
        'src/crew.py',
        'config/agents.yaml',
        'config/tasks.yaml',
        'requirements.txt'
    ]
    for file in files:
        if os.path.exists(file):
            print(f"✓ File exists: {file}")
        else:
            print(f"✗ File missing: {file}")
            return False

    return True


def check_imports():
    """Check if all required packages can be imported."""
    print("\n🔍 Checking package imports...")
    print("-" * 50)

    packages = [
        ('crewai', 'CrewAI'),
        ('crewai_tools', 'CrewAI Tools'),
        ('openai', 'OpenAI'),
        ('pydantic', 'Pydantic'),
        ('yaml', 'PyYAML'),
        ('dotenv', 'python-dotenv'),
        ('langchain_openai', 'LangChain OpenAI')
    ]

    all_imports_ok = True
    for package, name in packages:
        try:
            __import__(package)
            print(f"✓ {name} ({package})")
        except ImportError:
            print(f"✗ {name} ({package}) - not installed")
            all_imports_ok = False

    if not all_imports_ok:
        print("\n⚠️  Some packages are missing. Please run:")
        print("  pip install -r requirements.txt")
        return False

    return True


def check_crew_setup():
    """Check if the crew can be initialized."""
    print("\n🔍 Checking crew initialization...")
    print("-" * 50)

    try:
        from src.crew import InterviewAssistantCrew
        crew = InterviewAssistantCrew()
        print("✓ Crew initialized successfully")
        print(f"  Agents created: {len(crew.agents)}")
        return True
    except Exception as e:
        print(f"✗ Failed to initialize crew: {e}")
        return False


def main():
    """Run all checks."""
    print("\n" + "=" * 50)
    print("🎙️  AUTOMATED INTERNSHIP ASSISTANT - TEST SETUP")
    print("=" * 50 + "\n")

    checks = [
        ("Environment", check_environment),
        ("Package Imports", check_imports),
        ("Crew Setup", check_crew_setup)
    ]

    all_passed = True
    for name, check_func in checks:
        if not check_func():
            all_passed = False
            print(f"\n❌ {name} check failed")
        else:
            print(f"\n✅ {name} check passed")

    print("\n" + "=" * 50)
    if all_passed:
        print("✅ All checks passed! The system is ready to use.")
        print("\nNext steps:")
        print("1. Place an audio file in the audio/ directory")
        print("2. Run: python src/main.py --audio audio/your_file.mp3")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
    print("=" * 50 + "\n")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())