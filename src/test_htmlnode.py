from htmlnode import HTMLNODE
import unittest

props1={
    "href": "https://www.google.com",
    "target": "_blank",
}
props2={
    "test":"testytest",
    "rest":"festy yreed"
}

class TestHTMLNODE(unittest.TestCase):


    def test_to_props(self):
        testHTML1=HTMLNODE("bold", "test", None, props1)
        test=testHTML1.props_to_html()
        output=" href='https://www.google.com' target='_blank'"
        self.assertEqual(test, output)

    def testrpr(self):
        testHTML2=HTMLNODE("bold", "test", None, props2)
        output2=f"HTMLNODE(bold, test, {None}, {props2})"
        self.assertEqual(repr(testHTML2), output2)
