from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node, TextNode, TextType
from text_to_textnodes import text_to_textnodes

def text_to_children(text):
    return list(map(lambda node: text_node_to_html_node(node), text_to_textnodes(text)))

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node_list = []
    for block in blocks:
        btype = block_to_block_type(block)
        if btype == BlockType.CODE:
            parent_node_list.append(ParentNode("pre", [LeafNode("code", block[3:-3])]))
        if btype == BlockType.HEADING:
            count = 0
            for char in block[0:6]:
                if char == '#':
                    count += 1
                else:
                    break
            parent_node_list.append(ParentNode(f"h{count}", text_to_children(block[count+1:])))
        if btype == BlockType.QUOTE:
            block_text = block
            lines = block_text.split("\n")
            newlines= []
            for line in lines:
                newlines.append(line[2:])
            block_text = "\n".join(newlines)
            parent_node_list.append(ParentNode("blockquote", text_to_children(block_text)))
        if btype == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            newlines = []
            for line in lines:
                newlines.append(ParentNode("li", text_to_children(line[2:])))
            parent_node_list.append(ParentNode("ul", newlines))
        if btype == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            newlines = []
            for line in lines:
                dot_space_index = line.find(". ")
                newlines.append(ParentNode("li", text_to_children(line[dot_space_index+2:])))
            parent_node_list.append(ParentNode("ol", newlines))
        if btype == BlockType.PARAGRAPH:
            parent_node_list.append(ParentNode("p", text_to_children(block)))
    return ParentNode("div", parent_node_list)

