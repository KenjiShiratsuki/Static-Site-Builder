import unittest
from textnode import TextNode, TextType
from split_nodes_link_image import split_nodes_images, split_nodes_links

class TestSplitNodesImagesLinks(unittest.TestCase):
    def test_no_images(self):
        self.assertEqual(split_nodes_images([TextNode("testing", TextType.NORMAL)]), [TextNode("testing", TextType.NORMAL)])

    def test_two_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) with some text after!",
        TextType.NORMAL)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" with some text after!", TextType.NORMAL)
            ],
            new_nodes,
        )
    
    def test_two_images_consecutive(self):
        node = TextNode(
        "This is text with two consecutive ![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png) images!",
        TextType.NORMAL)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with two consecutive ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" images!", TextType.NORMAL)
            ],
            new_nodes,
        )

    def test_only_images(self):
        node = TextNode(
        "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.NORMAL)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    
    def test_no_links(self):
        self.assertEqual(split_nodes_links([TextNode("testing", TextType.NORMAL)]), [TextNode("testing", TextType.NORMAL)])

    def test_two_links(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) with some text after!",
        TextType.NORMAL,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode(" with some text after!", TextType.NORMAL)
            ],
            new_nodes,
        )
    
    def test_two_links_consecutively(self):
        node = TextNode(
        "This is text with two consecutive links [to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev) with some text after!",
        TextType.NORMAL,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with two consecutive links ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode(" with some text after!", TextType.NORMAL)
            ],
            new_nodes,
        )
    
    def test_only_links(self):
            node = TextNode(
            "[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
            )
            new_nodes = split_nodes_links([node])
            self.assertListEqual(
                [
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ],
                new_nodes,
            )
    
    def test_wrong_node_type(self):
        node = TextNode("to boot.dev", TextType.LINK, "https://www.boot.dev")
        new_nodes_image = split_nodes_images([node])
        new_nodes_link = split_nodes_links([node])
        self.assertListEqual([TextNode("to boot.dev", TextType.LINK, "https://www.boot.dev")], new_nodes_image)
        self.assertListEqual([TextNode("to boot.dev", TextType.LINK, "https://www.boot.dev")], new_nodes_link)