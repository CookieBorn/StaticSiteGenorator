from htmlnode import HTMLNODE

class LeafNode(HTMLNODE):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)


    def to_html(self):
        # Raise ValueError if no value exists
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        # If there's no tag, return raw value
        if self.tag is None:
            return self.value
        # If there are props, include them in the rendered tag
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
                   # Otherwise, render tag with just the value inside
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
         return f"LeafNode({self.tag}, {self.value}, {self.props})"
