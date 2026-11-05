from linkgrabber import *
from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_split = node.value.split(delimiter)
        if len(node_split) % 2 == 0:
            raise ValueError("Invalid Markdown syntax: missing closing delimiter")
        for index, value in enumerate(node_split):
            if not value:
                continue
            if index % 2 == 0:
                new_nodes.append(TextNode(value, TextType.TEXT))
            else:
                new_nodes.append(TextNode(value, text_type))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if not node.value:
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        link = extract_markdown_images(node.value)
        if len(link) == 0:
            new_nodes.append(node)
            continue
        text = node.value
        for _, value in enumerate(link):
            split = text.split(f"![{value[0]}]({value[1]})", 1)
            if len(split) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if len(split[0]) > 0:
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(value[0],TextType.IMAGE, value[1]))
            text = split[1]
        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if not node.value:
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        link = extract_markdown_links(node.value)
        if len(link) == 0:
            new_nodes.append(node)
            continue
        text = node.value
        for _, value in enumerate(link):
            split = text.split(f"[{value[0]}]({value[1]})", 1)
            if len(split) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if len(split[0]) > 0:
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(value[0],TextType.LINK, value[1]))
            text = split[1]
        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def markdown_to_blocks(text: str):
    lines = []
    linebreak = text.split("\n\n")
    for s in linebreak:
        lines.append(s.strip())
    return lines
