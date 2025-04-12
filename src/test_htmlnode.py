import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Click Me!", None, {"href": "https://www.example.com", "target": "_blank"})
        example = ' href="https://www.example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), example)
    
    def test_repr(self):
        node = HTMLNode("a", "Click Me!", None, {"href": "https://www.example.com", "target": "_blank"})
        example = "a, Click Me!, [], {'href': 'https://www.example.com', 'target': '_blank'}"
        self.assertEqual(node.__repr__(), example)

    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_empty_props(self):
        node = HTMLNode("a" "something")
        self.assertEqual(node.props_to_html(), "")

    def test_node_with_children(self):
        child = HTMLNode("span", "Child content")
        parent = HTMLNode("div", children=[child])
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0].tag, "span")