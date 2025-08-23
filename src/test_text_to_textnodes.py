import unittest
from textnode import TextNode, TextType
from split_nodes_link_image import split_nodes_images, split_nodes_links
from split_delimiter import split_nodes_delimiter
from text_to_textnodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes_unit_example(self):
        result = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(result, [
    TextNode("This is ", TextType.NORMAL),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.NORMAL),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.NORMAL),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.NORMAL),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.NORMAL),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])
    def test_text_to_textnodes_individual_delimiters_none_normal(self):
        empty = text_to_textnodes("")
        self.assertEqual(empty, [])
        plain = text_to_textnodes("this is plain text only")
        self.assertEqual(plain, [TextNode("this is plain text only", TextType.NORMAL)])
        bold = text_to_textnodes("**bold**")
        self.assertEqual(bold, [TextNode("bold", TextType.BOLD)])
        italics = text_to_textnodes("_italics_")
        self.assertEqual(italics, [TextNode("italics", TextType.ITALIC)])
        code = text_to_textnodes("`code block`")
        self.assertEqual(code, [TextNode("code block", TextType.CODE)])
        image = text_to_textnodes("![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(image, [TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")])
        link = text_to_textnodes("[link](https://boot.dev)")
        self.assertEqual(link, [TextNode("link", TextType.LINK, "https://boot.dev")])