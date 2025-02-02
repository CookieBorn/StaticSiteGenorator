
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from tkinter import Image
from parentnode import ParentNode
from markdowntotext import *
from static import *


def main():
    clear_copy("./public/","./static")
    generate_pages_recursive("./content", "./template.html", "./public")




print("hello world")
main()
