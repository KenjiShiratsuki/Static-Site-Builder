import unittest

from htmlnode import LeafNode, HTMLNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_raises_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
    def test_normal_leaf_node_to_html(self):
        node1 = LeafNode("p", "This is a paragraph")
        self.assertEqual(node1.to_html(), "<p>This is a paragraph</p>")
    def test_empty_tag_leaf_node_to_html(self):
        node1 = LeafNode(None, "This is raw text")
        self.assertEqual(node1.to_html(), "This is raw text")
    def test_leaf_node_link_to_html(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')