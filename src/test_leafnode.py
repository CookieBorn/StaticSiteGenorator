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

class TestLeafNode(unittest.TestCase):
    def test_tohtml(self):
      testnode1 = LeafNode("p", "This is a paragraph of text.")
      test1=testnode1.to_html()
      output1="<p>This is a paragraph of text.</p>"
      self.assertEqual(output1,test1)

    def test_tohtml2(self):
        testnode2= LeafNode("a", "Click me!", props3)
        test2=testnode2.to_html()
        output2="<a href='https://www.google.com'>Click me!</a>"
        self.assertEqual(output2,test2)
