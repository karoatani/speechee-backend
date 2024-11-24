import os
from .text_parser import TextParser
from .markdown_parser import MarkdownParser
from .rtf_parser import RtfParser
from .docx_parser import DocxParser
from .doc_parser import DocParser

class ParserFactory:
    @staticmethod
    def get_parser(file_path: str):
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".txt":
            return TextParser()
        elif file_extension == ".md":
            return MarkdownParser()
        elif file_extension == ".rtf":
            return RtfParser()
        elif file_extension == ".docx":
            return DocxParser()
        elif file_extension == ".doc":
            return DocParser()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
