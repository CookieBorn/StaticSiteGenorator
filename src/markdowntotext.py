
import re
from htmlnode import HTMLNODE
from parentnode import ParentNode
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
    y=split_nodes_delimiter(y,"_",TextType.Italic)
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
    if block[0]=="#":
        return "heading"
    elif block[:3]=="```" and block[-3:]=="```":
        return "code"
    elif block[0]==">":
        return "quote"
    elif block[:2]=="* " or block[:2]=="- ":
        return "unordered list"
    elif block[:2]=="1.":
        return "ordered list"
    else:
        return "normal"

def markdown_to_html_node(markdown):
    blocks=markdown_to_blocks(markdown)
    out=[]
    for block in blocks:
        type=block_to_block_type(block)
        if type=="heading":
            x=block[:6].count("#")
            child=text_to_children(block[x+1:])
            block_html=ParentNode(f"h{x}",child)
            out.append(block_html)
        if type=="code":
            split=block.split("\n")
            code="\n".join(split[1:-1])
            innerblock=ParentNode("code", [LeafNode(value=code)])
            block_html=ParentNode("pre",[innerblock])
            out.append(block_html)
        if type=="quote":
            child=text_to_children(block[2:])
            block_html=ParentNode("blockquote", child)
            out.append(block_html)
        if type=="unordered list":
            li=block.split("\n")
            outlist=[]
            for l in li:
                html=text_to_children(l[2:])
                node=ParentNode("li",html)
                outlist.append(node)
            block_html=ParentNode("ul",outlist)
            out.append(block_html)
        if type=="ordered list":
            li=block.split("\n")
            outlist=[]
            for l in li:
                html=text_to_children(l[2:])
                node=ParentNode("li",html)
                outlist.append(node)
            block_html=ParentNode("ol",outlist)
            out.append(block_html)
        if type=="normal":
            child=text_to_children(block)
            block_html=ParentNode("p", child)
            out.append(block_html)
    return ParentNode("div",out)

def text_to_children(block):
   lines=block.split("\n")
   text_nodes=[]
   for b in lines:
       c=b.strip()
       text_nodes.append(text_to_textnodes(c))
   html_nodes=[]
   for text in text_nodes:
       for t in text:
           html_nodes.append(t.text_node_to_html_node())
   html_final_nodes=[]
   for html in html_nodes:
        if not (html.value is None or html.value.isspace()):
            html_final_nodes.append(html)
   return html_final_nodes

def extract_title(markdown):
    blocks=markdown.split("\n")
    for block in blocks:
        if block[:2]=="# ":
            return block[2:].strip()
    raise ValueError("No Heading")
