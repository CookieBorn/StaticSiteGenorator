from htmlnode import HTMLNODE
from textnode import *
from leafnode import LeafNode



def main():
    node=TextNode("git", TextType.Bold, "www.boot.dev")
    print(repr(node))
    props3={
        "href": "https://www.google.com",
        "target": "_blank",
    }
    testnode2= LeafNode("a", "Click me!",props3)
    test2=testnode2.props_to_html()
    print(testnode2.props)
    print(test2)

print("hello world")
main()
