
import re
from tkinter import Image
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old in old_nodes:
        if old.text_type == TextType.TEXT:  # Use correct enum
            parts = old.text.split(delimiter)
            if len(parts) == 1:  # No delimiter found
                result.append(old)
                continue

            for i in range(len(parts)):
                if i % 2 == 0:
                    if parts[i] != "":  # Only append non-empty strings
                        result.append(TextNode(parts[i], TextType.TEXT))
                else:
                    result.append(TextNode(parts[i], text_type))
        else:
            result.append(old)
    return result

def split_nodes_image(old_nodes):
    result = []
    for old in old_nodes:
        if old.text_type == TextType.TEXT:
            images = extract_markdown_images(old.text)
            if not images:  # If no images found, keep original node
                result.append(old)
                continue

            sections = old.text
            for img_text, img_url in images:
                parts = sections.split(f"![{img_text}]({img_url})", 1)
                if parts[0]:  # Add text before image
                    result.append(TextNode(parts[0], TextType.TEXT))
                result.append(TextNode(img_text, TextType.Images, img_url))
                sections = parts[1] if len(parts) > 1 else ""

            if sections:  # Add remaining text
                result.append(TextNode(sections, TextType.TEXT))
        else:
            result.append(old)
    return result

def split_nodes_link(old_nodes):
    result = []
    for old in old_nodes:
        if old.text_type == TextType.TEXT:
            images = extract_markdown_links(old.text)
            if not images:  # If no images found, keep original node
                result.append(old)
                continue

            sections = old.text
            for img_text, img_url in images:
                parts = sections.split(f"[{img_text}]({img_url})", 1)
                if parts[0]:  # Add text before image
                    result.append(TextNode(parts[0], TextType.TEXT))
                result.append(TextNode(img_text, TextType.Links, img_url))
                sections = parts[1] if len(parts) > 1 else ""

            if sections:  # Add remaining text
                result.append(TextNode(sections, TextType.TEXT))
        else:
            result.append(old)
    return result

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return  re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def text_to_textnodes(text):
    y=split_nodes_delimiter([TextNode(text,TextType.TEXT)],"**",TextType.Bold)
    y=split_nodes_delimiter(y,"*",TextType.Italic)
    y=split_nodes_delimiter(y,"`",TextType.Code)
    y=split_nodes_link(y)
    y=split_nodes_image(y)
    return y

def markdown_to_blocks(markdown):
    blocks=markdown.split("\n\n")
    x=0
    for block in blocks:
        blocks[x]=block.strip()
        if block.isspace():
            del blocks[x]
        x+=1
    return blocks

def block_to_block_type(block):
    return
