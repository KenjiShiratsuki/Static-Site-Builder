import re
def extract_markdown_images(text):
    list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) 
    return list

def extract_markdown_links(text):
    list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return list