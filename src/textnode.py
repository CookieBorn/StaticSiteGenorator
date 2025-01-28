from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    Normal="normal"
    Bold="bold"
    Italic="italic"
    Code="code"
    Links="links"
    Images="images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text=text
        self.text_type=text_type
        self.url=url
    def __eq__(self, other):
        if self.text==other.text and self.text_type==other.text_type and self.url==other.url:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.Normal:
                return LeafNode(value=self.text)
            case TextType.Bold:
                return LeafNode(tag="b", value=self.text)
            case TextType.Italic:
                return LeafNode(tag="i", value=self.text)
            case TextType.Code:
                return LeafNode(tag="code", value=self.text)
            case TextType.Links:
                return LeafNode(tag="a", value=self.text, props="href")
            case TextType.Images:
                return LeafNode(tag="img",value="", props={"src":self.url, "alt":self.text})
            case _:
                raise Exception ("Missing text type")
