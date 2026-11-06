from block import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import *
from string_to_text_node import *


def markdown_to_html_node(markdown: str) -> HtmlNode:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        pass

def block_to_html_node(block: str):
    bt = block_to_block_type(block)

def paragraph_to_html_node(block: str):
    pass

def heading_to_html_node(block: str):
    pass

def code_to_html_node(block: str):
    pass

def quote_to_html_node(block: str):
    pass

def ulist_to_html_node(block: str):
    pass

def olist_to_html_node(block: str):
    pass

def text_to_children(text: str):
    pass
