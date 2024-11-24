import subprocess
from .parser import Parser

class DocParser(Parser):
    def extract_heading(self, file_path: str):
        """Extract potential headings based on placement and heuristics."""
        raw_content = self._extract_raw_content(file_path)
        if not raw_content:
            return []

        lines = raw_content.splitlines()
        headings = []
        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Heuristics for detecting headings:
            if (
                idx < 5 or  # Early lines
                (len(line) < 50 and self._is_surrounded_by_blank_lines(idx, lines)) or  # Surrounded by blank lines
                line.isupper() or  # All uppercase
                line.endswith(":")  # Ends with ':'
            ):
                headings.append(line)
                break  # Assuming a single primary heading

        return headings

    def extract_content(self, file_path: str):
        """Extract content after excluding headings."""
        raw_content = self._extract_raw_content(file_path)
        if not raw_content:
            return ""

        lines = raw_content.splitlines()
        content = []
        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Ignore lines identified as headings
            if not (
                idx < 5 or
                (len(line) < 50 and self._is_surrounded_by_blank_lines(idx, lines)) or
                line.isupper() or
                line.endswith(":")
            ):
                content.append(line)

        return "\n".join(content)

    def parse(self, file_path: str):
        """
        Combine headings and content into a structured format.
        This is where single-pass parsing can be implemented.
        """
        raw_content = self._extract_raw_content(file_path)
        if not raw_content:
            return None, None

        lines = raw_content.splitlines()
        headings = []
        content = []
        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Heuristics for detecting headings
            if (
                idx < 5 or
                (len(line) < 50 and self._is_surrounded_by_blank_lines(idx, lines)) or
                line.isupper() or
                line.endswith(":")
            ):
                if not headings:  # Take only the first detected heading
                    headings.append(line)
            else:
                content.append(line)

        return headings, "\n".join(content)

    def _extract_raw_content(self, file_path: str):
        """Use antiword to extract raw text from the file."""
        try:
            result = subprocess.run(['antiword', file_path], capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Error reading the file: {result.stderr}")
            return result.stdout
        except Exception as e:
            print(f"Error: {e}")
            return None

    def _is_surrounded_by_blank_lines(self, idx, lines):
        """Check if a line is surrounded by blank lines."""
        prev_blank = idx > 0 and not lines[idx - 1].strip()
        next_blank = idx < len(lines) - 1 and not lines[idx + 1].strip()
        return prev_blank and next_blank
