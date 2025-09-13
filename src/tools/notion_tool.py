import os
from datetime import datetime
from typing import Type, Optional
from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class NotionToolInput(BaseModel):
    """Input schema for NotionTool."""
    content: str = Field(..., description="Content to save to Notion or markdown file")
    company: str = Field(default="Unknown Company", description="Company name for the interview")
    role: str = Field(default="Unknown Role", description="Role applied for")


class NotionTool(BaseTool):
    name: str = "Notion Exporter"
    description: str = "Exports interview analysis to Notion database or markdown file as fallback"
    args_schema: Type[BaseModel] = NotionToolInput

    def _run(self, content: str, company: str = "Unknown Company", role: str = "Unknown Role") -> str:
        """
        Export content to Notion database or save as markdown file if Notion is unavailable.

        Args:
            content: The formatted interview analysis content
            company: Company name
            role: Role applied for

        Returns:
            Success message with location of saved content
        """
        notion_token = os.getenv('NOTION_TOKEN')
        notion_database_id = os.getenv('NOTION_DATABASE_ID')

        # If Notion credentials are available, attempt to save to Notion
        if notion_token and notion_database_id:
            try:
                return self._save_to_notion(content, company, role, notion_token, notion_database_id)
            except Exception as e:
                print(f"Failed to save to Notion: {str(e)}. Falling back to markdown file.")
                return self._save_to_markdown(content, company, role)
        else:
            # No Notion credentials, save to markdown
            print("Notion credentials not found. Saving to markdown file.")
            return self._save_to_markdown(content, company, role)

    def _save_to_notion(self, content: str, company: str, role: str, token: str, database_id: str) -> str:
        """
        Save content to Notion database.
        Note: This is a placeholder for Notion integration.
        In production, you would use the Notion API or MCP server.
        """
        # This would be implemented with actual Notion API calls
        # For now, we'll just save to markdown as the MCP server setup is complex
        print("Note: Full Notion integration requires MCP server setup.")
        return self._save_to_markdown(content, company, role)

    def _save_to_markdown(self, content: str, company: str, role: str) -> str:
        """
        Save content to a markdown file.

        Args:
            content: The formatted interview analysis
            company: Company name
            role: Role applied for

        Returns:
            Path to the saved file
        """
        try:
            # Create interviews directory if it doesn't exist
            os.makedirs("interviews", exist_ok=True)

            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_company = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in company)
            safe_role = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in role)
            filename = f"{safe_company}_{safe_role}_Interview_{timestamp}.md"
            file_path = os.path.join("interviews", filename)

            # Add header to content if not present
            if not content.startswith("#"):
                header = f"# {company} - {role} Interview Analysis\n\n"
                header += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                header += "---\n\n"
                content = header + content

            # Write content to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            return f"Interview analysis successfully saved to {file_path}"

        except Exception as e:
            return f"Error saving to markdown file: {str(e)}"