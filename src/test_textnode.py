import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_nourl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = "TextNode(This is a text node, bold, None)"
        self.assertEqual(repr(node), node2)
    
    def test_text_node_NORMAL_to_HTML_node(self):
        node = TextNode("This is normal text", TextType.NORMAL)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, None)
        self.assertEqual(leaf.value, "This is normal text")
    
    def test_text_node_BOLD_to_HTML_node(self):
        node = TextNode("This is bold text", TextType.BOLD)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, "b")
        self.assertEqual(leaf.value, "This is bold text")
    
    def test_text_node_ITALIC_to_HTML_node(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, "i")
        self.assertEqual(leaf.value, "This is italic text")

    def test_text_node_CODE_to_HTML_node(self):
        node = TextNode("This is code", TextType.CODE)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, "code")
        self.assertEqual(leaf.value, "This is code")
    
    def test_text_node_LINK_to_HTML_node(self):
        node = TextNode("This is a link", TextType.LINK, "https://imgur.com/a/jxVfFmR")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, "a")
        self.assertEqual(leaf.value, "This is a link")
        self.assertEqual(leaf.props, {"href": "https://imgur.com/a/jxVfFmR"})
    
    def test_text_node_IMAGE_to_HTML_node(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://i.imgur.com/hD4ZhnL.jpeg")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, "img")
        self.assertEqual(leaf.value, "")
        self.assertEqual(leaf.props, {"src": "https://i.imgur.com/hD4ZhnL.jpeg", "alt": "This is an image"})

    def test_text_node_empty_LINK_to_HTML_node(self):
        node = TextNode("This is a link", TextType.LINK, "")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, "a")
        self.assertEqual(leaf.value, "This is a link")
        self.assertEqual(leaf.props, {"href": ""})
    
    def test_text_node_empty_IMAGE_to_HTML_node(self):
        node = TextNode("", TextType.IMAGE, "")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.tag, "img")
        self.assertEqual(leaf.value, "")
        self.assertEqual(leaf.props, {"src": "", "alt": ""})

    def test_text_node_NoneType_to_HTML_node(self):
        with self.assertRaises(TypeError):
            node = TextNode("This is normal text", TextType.NORMAL)
            node.text_type = None
            leaf = text_node_to_html_node(node)
            

if __name__ == "__main__":
    unittest.main()