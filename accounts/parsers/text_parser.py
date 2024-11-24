from .parser import Parser

class TextParser(Parser):
    def extract_heading(self, file_path: str):
        headings = []
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip().startswith("#"):  # Simple example, assuming headings start with "#"
                    headings.append(line.strip())
        return headings

    def extract_content(self, file_path: str):
        content = []
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip().startswith("#"):  # Exclude headings
                    content.append(line.strip())
        return content

    def parse(self, file_path: str):
        headings = self.extract_heading(file_path)
        content = self.extract_content(file_path)
        return headings, content
