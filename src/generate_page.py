import os
from pathlib import Path
from block_to_html import markdown_to_html_node  # adjust import to your module name
from extract_title import extract_title          # adjust import to your module name

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    full_page = (
        template
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    write_file(dest_path, full_page)

def write_file(dest_path, content):
    dirpath = os.path.dirname(dest_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(f"Scanning '{dir_path_content}' for markdown files to convert:")

    mdfiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(dir_path_content)
             for name in files
             if name.endswith(".md")]

    print(mdfiles)

    for file in mdfiles:
        print(f"Processing '{file}'")
        source_path = file
        dest_path = Path(dest_dir_path, *Path(file).parts[1:]).with_suffix('.html')

        print(f"Converting and writing to '{dest_path}'")
        generate_page(source_path, template_path, dest_path, basepath)