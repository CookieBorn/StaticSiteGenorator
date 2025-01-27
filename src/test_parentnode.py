from parentnode import ParentNode
from leafnode import LeafNode
import unittest

props1={
    "href": "https://www.google.com",
    "target": "_blank",
}
props2={
    "test":"testytest",
    "rest":"festy yreed"
}
props3={"href": "https://www.google.com"}

class TestParentNode(unittest.TestCase):
    def test_tohtml(self):
      node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

      test=node.to_html()
      output1="<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
      self.assertEqual(output1,test)
