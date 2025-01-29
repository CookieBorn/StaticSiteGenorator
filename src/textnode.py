from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    TEXT="text"
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
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT | "text":
                return LeafNode(value=self.text)
            case TextType.Bold | "bold":
                return LeafNode(tag="b", value=self.text)
            case TextType.Italic | "italic":
                return LeafNode(tag="i", value=self.text)
            case TextType.Code | "code":
                return LeafNode(tag="code", value=self.text)
            case TextType.Links | "links":
                return LeafNode(tag="a", value=self.text, props="href")
            case TextType.Images | "images":
                return LeafNode(tag="img",value="", props={"src":self.url, "alt":self.text})
            case _:
                raise Exception ("Missing text type")
