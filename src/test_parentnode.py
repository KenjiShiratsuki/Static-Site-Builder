import unittest

from htmlnode import LeafNode, ParentNode, HTMLNode
#Reminder that the variables in order are Tag(required), Value(not used), Children(required), Props(optional)
class TestParentNode(unittest.TestCase):
    def test_parent_node_raises_tag_error(self):
        with self.assertRaises(ValueError):
            node1 = LeafNode("p", "This is a paragraph")
            parent1 = ParentNode(None, [node1])
            string = parent1.to_html()
    def test_parent_node_raises_child_error_none(self):
        with self.assertRaises(ValueError):
            parent1 = ParentNode("p", None)
            string = parent1.to_html()
    def test_parent_node_raises_child_error_empty(self):
        with self.assertRaises(ValueError):
            parent1 = ParentNode("p", [])
            string = parent1.to_html()
    def test_parent_node_raises_tag_error_message(self):
        with self.assertRaises(ValueError) as context:
            node1 = LeafNode("p", "This is a paragraph")
            parent1 = ParentNode(None, [node1])
            string = parent1.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no tag")
    def test_parent_node_raises_child_error_none(self):
        with self.assertRaises(ValueError) as context:
            parent1 = ParentNode("p", None)
            string = parent1.to_html()
        self.assertEqual(str(context.exception), "Invalid Parent Node: no children")
    def test_parent_node_raises_child_error_empty(self):
        with self.assertRaises(ValueError) as context:
            parent1 = ParentNode("p", [])
            string = parent1.to_html()
        self.assertEqual(str(context.exception), "Invalid Parent Node: no children")
    def test_parent_node_with_props(self):
        child1 = LeafNode("p", "This is a paragraph")
        child2 = LeafNode(None, "This is raw text")
        parent1 = ParentNode("p", [child1, child2], {"class": "container", "id": "main"})
        self.assertEqual(parent1.to_html(), '<p class="container" id="main"><p>This is a paragraph</p>This is raw text</p>')
    # def test_normal_leaf_node_to_html(self):
    #     node1 = LeafNode("p", "This is a paragraph")
    #     self.assertEqual(node1.to_html(), "<p>This is a paragraph</p>")
    # def test_empty_tag_leaf_node_to_html(self):
    #     node1 = LeafNode(None, "This is raw text")
    #     self.assertEqual(node1.to_html(), "This is raw text")
    # def test_leaf_node_link_to_html(self):
    #     node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #     self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')