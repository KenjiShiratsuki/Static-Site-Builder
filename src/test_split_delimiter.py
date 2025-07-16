import unittest

from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_normal_bold_split(self):
        list = [TextNode("This is **bold text** embedded in normal text.", TextType.NORMAL)]
        results = split_nodes_delimiter(list, "**", TextType.BOLD)
        self.assertEqual(results[0].text, "This is ")
        self.assertEqual(results[1].text, "bold text")
        self.assertEqual(results[1].text_type, TextType.BOLD)
        self.assertEqual(results[2].text, " embedded in normal text.")
    
    def test_normal_italic_split(self):
        list = [TextNode("This is _italic text_ embedded in normal text.", TextType.NORMAL)]
        results = split_nodes_delimiter(list, "_", TextType.ITALIC)
        self.assertEqual(results[0].text, "This is ")
        self.assertEqual(results[1].text, "italic text")
        self.assertEqual(results[1].text_type, TextType.ITALIC)
        self.assertEqual(results[2].text, " embedded in normal text.")

    def test_normal_code_split(self):
        list = [TextNode("This is `code text` embedded in normal text.", TextType.NORMAL)]
        results = split_nodes_delimiter(list, "`", TextType.CODE)
        self.assertEqual(results[0].text, "This is ")
        self.assertEqual(results[1].text, "code text")
        self.assertEqual(results[1].text_type, TextType.CODE)
        self.assertEqual(results[2].text, " embedded in normal text.")

    def test_delimiter_missing_close(self):
        with self.assertRaises(Exception):
            list = [TextNode("This is **bold text embedded in normal text.", TextType.NORMAL)]
            results = split_nodes_delimiter(list, "**", TextType.BOLD)



if __name__ == "__main__":
    unittest.main()