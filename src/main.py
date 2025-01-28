
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from tkinter import Image
from parentnode import ParentNode
from markdowntotext import *



def main():
    node = TextNode("This is text with a `code block` word", TextType.Code)
    node2 = TextNode("This is text with a `code block 2` word", TextType.Normal)
    new_nodes = split_nodes_delimiter([node, node2], "`", TextType.Code)
    print(new_nodes)

print("hello world")
main()
