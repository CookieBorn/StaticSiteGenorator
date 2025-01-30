import unittest
from markdowntotext import *

class TestMarkDownToText(unittest.TestCase):

    def test_to_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        test=markdown_to_blocks(text)
        output=['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(test, output)

    def test_to_blocks2(self):
        text = "# This is a heading\n\n   This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n  "
        test=markdown_to_blocks(text)
        output=['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(test, output)

    def test_block_normal(self):
        text="223"
        test=block_to_block_type(text)
        self.assertEqual("normal",test)
    def test_block_heading(self):
        text="###223"
        test=block_to_block_type(text)
        self.assertEqual("heading",test)

    def test_block_code(self):
        text="```223```"
        test=block_to_block_type(text)
        self.assertEqual("code",test)

    def test_block_quote(self):
        text=">223"
        test=block_to_block_type(text)
        self.assertEqual("quote",test)

    def test_block_unlist1(self):
        text="* 223"
        test=block_to_block_type(text)
        self.assertEqual("unordered list",test)

    def test_block_unlist2(self):
        text="- 223"
        test=block_to_block_type(text)
        self.assertEqual("unordered list",test)

    def test_block_list1(self):
        text="1.223"
        test=block_to_block_type(text)
        self.assertEqual("ordered list",test)
