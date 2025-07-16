from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            string = node.text
            if string.count(delimiter) % 2 != 0:
                raise Exception(f'Invalid Markdown: no closing delimiter for text node with the text "{string}". Please close the delimiter "{delimiter}" and re-try')
            list = string.split(delimiter)
            for index, part in enumerate(list):
                if index % 2 == 0:
                    if part != "":
                        new_nodes.append(TextNode(part, TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes