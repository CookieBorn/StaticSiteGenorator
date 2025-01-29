
import re
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    x=list()
    for old in old_nodes:
        if old.text_type == TextType.Normal or old.text_type=="normal":
            spl=old.text.split(delimiter)
            if spl[0]==old.text:
                raise Exception ("Delimeter not found")
            else:
                i=0
                while i<len(spl):
                    if i%2==0:
                        x.append(TextNode(spl[i],"TextType.Normal"))
                        i+=1
                    else:
                        x.append(TextNode(spl[i],text_type))
                        i+=1
        else:
            x.append(old)
    return x

def split_nodes_image(old_nodes):
    x=list()
    i=0
    k=1
    for old in old_nodes:
        images=extract_markdown_images(old.text)
        for image in images:
            sections = old.text.split(f"![{image[0]}]({image[1]})", 1)
            if i==0:
                x.append(TextNode(f'"{sections[i]}"',TextType.Normal))
                x.append(TextNode(f'"{image[0]}"',TextType.Links, f'"{image[1]}"'))
                i+=1
            else:
                x.append(TextNode(f'"{sections[0].split(")")[-1]}"',TextType.Normal))
                x.append(TextNode(f'"{image[0]}"',TextType.Links, f'"{image[1]}"'))

    return x
def split_nodes_link(old_nodes):
    x=list()
    i=0
    for old in old_nodes:
        images=extract_markdown_links(old.text)
        for image in images:
            sections = old.text.split(f"[{image[0]}]({image[1]})", 1)
            if i==0:
                x.append(TextNode(f'"{sections[i]}"',TextType.Normal))
                x.append(TextNode(f'"{image[0]}"',TextType.Links, f'"{image[1]}"'))
                i+=1
            else:
                x.append(TextNode(f'"{sections[0].split(")")[1]}"',TextType.Normal))
                x.append(TextNode(f'"{image[0]}"',TextType.Links, f'"{image[1]}"'))


    return x

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return  re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
