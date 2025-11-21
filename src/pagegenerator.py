import re
from htmlnode import HTMLNode
from markdown_blocks import markdown_to_html_node
from pathlib import Path
import os

def extract_title(markdown):

    markdown_lines = markdown.splitlines()

    for line in markdown_lines:
        stripped_line = line.lstrip()
        title = re.search(r"^#\s(.+)", stripped_line)
        if title:
            return title.group(1)

    raise ValueError("String must start with title as h1 Heading")


def generate_page(from_path, template_path, dest_path, basepath):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template_content = f.read()

    node_tree = markdown_to_html_node(markdown_content)

    html_tree = node_tree.to_html()

    title = extract_title(markdown_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_tree)
    template_content = template_content.replace('href="/', 'href="' + basepath)
    template_content = template_content.replace('src="/', 'src="' + basepath)
    dest_dir: str = os.path.dirname(dest_path)

    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)

        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
