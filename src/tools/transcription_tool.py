import os
import base64
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from openai import OpenAI


class TranscriptionToolInput(BaseModel):
    """Input schema for TranscriptionTool."""
    audio_file_path: str = Field(..., description="Path to the audio file to transcribe")


class TranscriptionTool(BaseTool):
    name: str = "Audio Transcription Tool"
    description: str = "Transcribes audio files to text using GPT-4o audio preview via OpenRouter"
    args_schema: Type[BaseModel] = TranscriptionToolInput

    def _run(self, audio_file_path: str) -> str:
        """
        Transcribe an audio file to text using GPT-4o audio preview via OpenRouter.

        Args:
            audio_file_path: Path to the audio file

        Returns:
            Transcribed text from the audio file
        """
        api_key = os.getenv('OPENROUTER_API_KEY')
        if not api_key:
            return "Error: OPENROUTER_API_KEY not found in environment variables. Please set it in .env file."

        if not os.path.exists(audio_file_path):
            return f"Error: Audio file not found at {audio_file_path}"

        try:
            # Initialize OpenAI client with OpenRouter endpoint
            client = OpenAI(
                api_key=api_key,
                base_url="https://openrouter.ai/api/v1"
            )

            print(f"Starting transcription of {audio_file_path}...")

            # Read and encode the audio file
            with open(audio_file_path, 'rb') as audio_file:
                audio_data = audio_file.read()

            # Check file size (20MB limit for inline data)
            file_size_mb = len(audio_data) / (1024 * 1024)
            if file_size_mb > 20:
                # For now, return an error. In production, you could:
                # 1. Compress the audio
                # 2. Split into chunks
                # 3. Use a different transcription service
                return f"Error: Audio file is too large ({file_size_mb:.1f}MB). Maximum size is 20MB. Please use a smaller audio file or compress it."

            # Encode to base64
            audio_base64 = base64.b64encode(audio_data).decode('utf-8')

            # Determine mime type based on file extension
            file_ext = os.path.splitext(audio_file_path)[1].lower()
            mime_types = {
                '.mp3': 'audio/mp3',
                '.wav': 'audio/wav',
                '.m4a': 'audio/mp4',
                '.ogg': 'audio/ogg',
                '.webm': 'audio/webm'
            }
            mime_type = mime_types.get(file_ext, 'audio/mpeg')

            # Create the transcription request
            response = client.chat.completions.create(
                model="openai/gpt-4o-audio-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Please transcribe this audio file completely and accurately. Include all spoken words and indicate different speakers if there are multiple people speaking."
                            },
                            {
                                "type": "input_audio",
                                "input_audio": {
                                    "data": audio_base64,
                                    "format": mime_type.split('/')[-1]  # Extract format from mime type
                                }
                            }
                        ]
                    }
                ],
                modalities=["text"],
                audio={"voice": "alloy", "format": "wav"}
            )

            print("Transcription completed successfully!")
            return response.choices[0].message.content

        except Exception as e:
            return f"Error during transcription: {str(e)}"