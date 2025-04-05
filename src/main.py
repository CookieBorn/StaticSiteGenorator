
import sys
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from tkinter import Image
from parentnode import ParentNode
from markdowntotext import *
from static import *


def main():
    basepath = sys.argv[1]
    if len(basepath)==0:
        basepath="/"
    clear_copy("./docs/","./static")
    generate_pages_recursive("./content", "./template.html","./docs/", basepath)




print("hello world")
main()
