
from htmlnode import HTMLNODE
import parentnode
from textnode import *
from leafnode import LeafNode
from tkinter import Image
from parentnode import ParentNode
from markdowntotext import *



def main():
    text ="# Welcome to My Markdown Example\n\nThis is a simple example of Markdown text. Below, you'll find a list, a code block, and a link.\n\n## My Favorite Fruits\n\n- Apples\n- Bananas\n- Oranges\n- Strawberries\n\n## Code Example\n\nHere's a Python code block:\n\n```python\nprint(Hello, Markdown!)\n```\n\n## Useful Resources\n\nIf you'd like to learn more about Markdown, check out this [Markdown Guide](https://www.markdownguide.org/).\n\n---\n\nFeel free to modify or expand this example as needed"
    print(markdown_to_html_node(text))


print("hello world")
main()
