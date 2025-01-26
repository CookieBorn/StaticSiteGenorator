import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_neq_texttype(self):
        node3 = TextNode("This is a text node", TextType.Italic)
        node4 = TextNode("This is a text node", TextType.Bold)
        self.assertNotEqual(node3, node4)

    def test_eq_url(self):
        node5 = TextNode("This is a text node", TextType.Bold, None)
        node6 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node5, node6)

    def test_neq_text(self):
        node7 = TextNode("This is a test", TextType.Bold)
        node8 = TextNode("This is a text node", TextType.Bold)
        self.assertNotEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()
