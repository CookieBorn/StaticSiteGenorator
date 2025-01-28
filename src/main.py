
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from tkinter import Image
from parentnode import ParentNode



def main():
    node = TextNode("poopy buthole",TextType.Images)

    test=node.text_node_to_html_node()
    testy=test.to_html()
    print(testy)

print("hello world")
main()
