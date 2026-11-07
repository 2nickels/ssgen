from block import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import *
from string_to_text_node import *
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HtmlNode:
    children = []
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        block = block_to_html_node(b)
        children.append(block)
    parent: ParentNode = ParentNode("div", children)
    return parent

def block_to_html_node(block: str):
    bt = block_to_block_type(block)
    if bt == BlockType.HEADING:
        return heading_to_html_node(block)
    elif bt == BlockType.CODE:
        return code_to_html_node(block)
    elif bt == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif bt == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    elif bt == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    else:
        return paragraph_to_html_node(block)

def paragraph_to_html_node(block: str):
    block = block.replace("\n", " ")
    children: list[HtmlNode] = text_to_children(block)
    parent = ParentNode("p", children)
    return parent

def heading_to_html_node(block: str):
    count = 0
    block = block.replace("\n", " ")
    for ch in block:
        if ch == "#":
            count += 1
        else:
            break
    children: list[HtmlNode] = text_to_children(block[count+1:])
    parent = ParentNode(f"h{count}", children)
    return parent

def code_to_html_node(block: str):
    children = []
    block = block.removeprefix("```\n")
    block = block.replace("```", "")
    code = TextNode(block, TextType.CODE)
    children.append(text_node_to_html_node(code))
    parent = ParentNode("pre", children)
    return parent


def quote_to_html_node(block: str):
    block = block.replace("> ", "")
    block = block.replace(">", "")
    children: list[HtmlNode] = text_to_children(block)
    parent = ParentNode("blockquote", children)
    return parent

def ulist_to_html_node(block: str):
    li = []
    for i in block.split("\n"):
        i = i.removeprefix("- ")
        li.append(ParentNode("li", text_to_children(i)))
    parent = ParentNode("ul", li)
    return parent

def olist_to_html_node(block: str):
    li = []
    for i in block.split("\n"):
        i = re.sub(r"^.*?\. ", "", i)
        li.append(ParentNode("li", text_to_children(i)))
    parent = ParentNode("ol", li)
    return parent

def text_to_children(text: str):
    htmlnodes = []
    nodes = string_to_text_nodes(text)
    for node in nodes:
        leaf = text_node_to_html_node(node)
        htmlnodes.append(leaf)
    return htmlnodes
