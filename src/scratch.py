import os
from block_to_html import markdown_to_html_node

# Get the directory of the current file
current_dir = os.path.dirname(__file__)
# Go up one directory and join with 'index.md'
markdown_path = os.path.join(current_dir, '..', 'index.md')

# Read the markdown file
with open(markdown_path, 'r') as f:
    markdown = f.read()

html_node = markdown_to_html_node(markdown)

print (html_node.to_html())