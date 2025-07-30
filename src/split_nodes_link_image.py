from textnode import TextNode, TextType
import re
def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            original_text = node.text
            images_found = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", original_text)
            if images_found == []:
                new_nodes.append(TextNode(original_text, TextType.NORMAL))
            else:
                tup = images_found[0]
                image = (TextNode(tup[0], TextType.IMAGE, tup[1]))
                sections = original_text.split(f"![{image.text}]({image.url})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                new_nodes.append(image)
                if sections[1] != "":
                    new_nodes.extend(split_nodes_images([TextNode(sections[1], TextType.NORMAL)]))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            original_text = node.text
            links_found = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", original_text)
            if links_found == []:
                new_nodes.append(TextNode(original_text, TextType.NORMAL))
            else:
                tup = links_found[0]
                link = (TextNode(tup[0], TextType.LINK, tup[1]))
                sections = original_text.split(f"[{link.text}]({link.url})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                new_nodes.append(link)
                if sections[1] != "":
                    new_nodes.extend(split_nodes_links([TextNode(sections[1], TextType.NORMAL)]))
        else:
            new_nodes.append(node)
    return new_nodes