from enum import Enum
from typing_extensions import Text

class TextType(Enum):
    Normal="normal"
    Bold="bold"
    Italic="italic"
    Code="code"
    Links="links"
    Images="images"

class TextNode:
    def __innit__(self, text, text_type, url=None):
        self.text=text
        self.text_type=text_type
        self.url=url
    def __eq__(self, other):
        if self.text==other.text and self.text_type==other.text_type and self.url==other.url:
            return True
        return False
    def __repr__(self) -> str:

        pass
