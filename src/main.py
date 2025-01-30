
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from tkinter import Image
from parentnode import ParentNode
from markdowntotext import *



def main():
    text = "# This is a heading\n\n   This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n "
    print(markdown_to_blocks(text))


print("hello world")
main()
