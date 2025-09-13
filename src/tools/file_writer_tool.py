import os
from datetime import datetime
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class FileWriterToolInput(BaseModel):
    """Input schema for EnhancedFileWriterTool."""
    content: str = Field(..., description="Content to write to the file")
    filename: str = Field(default=None, description="Optional filename. If not provided, will generate timestamp-based name")
    directory: str = Field(default="interviews", description="Directory to save the file in")


class EnhancedFileWriterTool(BaseTool):
    name: str = "Enhanced File Writer"
    description: str = "Writes content to markdown files with proper formatting and organization"
    args_schema: Type[BaseModel] = FileWriterToolInput

    def _run(self, content: str, filename: str = None, directory: str = "interviews") -> str:
        """
        Write content to a markdown file.

        Args:
            content: Content to write to the file
            filename: Optional filename (without extension)
            directory: Directory to save the file in

        Returns:
            Path to the created file or error message
        """
        try:
            # Ensure directory exists
            os.makedirs(directory, exist_ok=True)

            # Generate filename if not provided
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"interview_analysis_{timestamp}"

            # Ensure .md extension
            if not filename.endswith('.md'):
                filename = f"{filename}.md"

            # Full file path
            file_path = os.path.join(directory, filename)

            # Write content to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            return f"Successfully saved analysis to {file_path}"

        except Exception as e:
            return f"Error writing file: {str(e)}"