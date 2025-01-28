from htmlnode import HTMLNODE

class ParentNode (HTMLNODE):
    def __init__(self, tag, children=None, props=None):
        super().__init__(tag=tag, value=None, props=props, children=children)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("Parent missing tag")
        elif self.children is None:
            raise ValueError ("Parent missing children")
        result=f"<{self.tag}>"
        for chil in self.children:
            result+=chil.to_html()
        result=result+f"</{self.tag}>"
        return result
