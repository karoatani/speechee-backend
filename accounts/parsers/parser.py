from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def extract_heading(self, file_path: str):
        """Extract headings from the file."""
        pass
    
    @abstractmethod
    def extract_content(self, file_path: str):
        """Extract content from the file."""
        pass

    @abstractmethod
    def parse(self, file_path: str):
        """Main method to parse the file."""
        pass
