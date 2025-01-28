

from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    x=list()
    for old in old_nodes:
        if old.text_type == TextType.Normal or old.text_type=="normal":
            spl=old.text.split(delimiter)
            if spl[0]==old.text:
                raise Exception ("Delimeter not found")
            else:
                x.append(TextNode(spl[0],TextType.Normal))
                x.append(TextNode(spl[1],text_type))
                x.append(TextNode(spl[2],TextType.Normal))
        else:
            x.append(old)
    return x
