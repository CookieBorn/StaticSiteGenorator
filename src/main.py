
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from tkinter import Image
from parentnode import ParentNode
from markdowntotext import *



def main():
    node = TextNode(
        "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) too ![to you](https://www.youtube.com/@bootdotdev) three ![to tube](https://www.youtube.com/@bootdotdev)",
        TextType.Normal,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)
    # [
    #     TextNode("This is text with a link ", TextType.TEXT),
    #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #     TextNode(" and ", TextType.TEXT),
    #     TextNode(
    #         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]

print("hello world")
main()
