

class HTMLNODE:
   def __init__(self, tag=None, value=None, children=None, props=None):
     self.tag = tag
     self.value=value
     self.children=children
     self.props=props

   def to_html(self):
           raise NotImplementedError("to_html method not implemented")


   def props_to_html(self):
       prop_str=" "
       if not isinstance(self.props, dict):
               return prop_str
       if self.props==None:
           return prop_str
       for prop in self.props.items():
           prop_str=prop_str+f"{prop[0]}='{prop[1]}' "
       prop_str=prop_str.rstrip()
       return prop_str

   def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"
