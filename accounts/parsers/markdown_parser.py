from .parser import Parser
class MarkdownParser(Parser):
    def extract_heading(self, file_path: str):
        headings = []
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip().startswith("#"):  # In markdown, headings are prefixed with #
                    headings.append(line.strip())
        return headings

    def extract_content(self, file_path: str):
        content = []
        with open(file_path, 'r') as file:
            in_content = False
            for line in file:
                if line.strip().startswith("#"):  # Skip heading lines
                    in_content = True
                if in_content:
                    content.append(line.strip())
        return content

    def parse(self, file_path: str):
        headings = self.extract_heading(file_path)
        content = self.extract_content(file_path)
        return headings, content
