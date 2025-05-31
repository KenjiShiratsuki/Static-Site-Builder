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

if __name__ == "__main__":
    unittest.main()