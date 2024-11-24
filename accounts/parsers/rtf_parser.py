from striprtf.striprtf import rtf_to_text
from .parser import Parser

class RtfParser(Parser):
    def extract_heading(self, file_path: str):
        headings = []
        with open(file_path, 'r') as file:
            rtf_content = file.read()
            text = rtf_to_text(rtf_content)  # Convert RTF to plain text
            lines = text.splitlines()
            for line in lines:
                if line.strip().startswith("#"):  # This assumes headings are marked similarly to markdown
                    headings.append(line.strip())
        return headings

    def extract_content(self, file_path: str):
        content = []
        with open(file_path, 'r') as file:
            rtf_content = file.read()
            text = rtf_to_text(rtf_content)  # Convert RTF to plain text
            lines = text.splitlines()
            for line in lines:
                if not line.strip().startswith("#"):  # Exclude headings
                    content.append(line.strip())
        return content

    def parse(self, file_path: str):
        headings = self.extract_heading(file_path)
        content = self.extract_content(file_path)
        return headings, content
