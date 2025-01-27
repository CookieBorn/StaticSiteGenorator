
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from parentnode import ParentNode



def main():
    node = ParentNode(
        "p",
        [
            ParentNode("b", [LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),]),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    test=node.to_html()
    print(test)

print("hello world")
main()
