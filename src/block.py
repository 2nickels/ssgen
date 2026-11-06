import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading" # ^(#{1,6}(?= ))
    CODE = "code" # ^(```).*(```)$
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(text: str):
    lines = []
    linebreak = text.split("\n\n")
    for s in linebreak:
        if s == "":
            continue
        block = s.strip()
        lines.append(block)
    return lines

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    if re.search(r"^(#{1,6}(?= ))", block):
        return BlockType.HEADING
    elif re.match("(?s)^(```\n).*(```)$", block):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
