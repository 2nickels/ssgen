from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, value: str, text_type: TextType, url: str | None = None) -> None:
        self.value = value
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        return bool(isinstance(other, TextNode) and self.value == other.value and self.text_type == other.text_type and self.url == other.url)

    def __repr__(self) -> str:
        return f"{TextNode(self.value, self.text_type, self.url)}"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.value)
        case TextType.BOLD:
            return LeafNode("b", text_node.value)
        case TextType.ITALIC:
            return LeafNode("i", text_node.value)
        case TextType.CODE:
            return LeafNode("code", text_node.value)
        case TextType.LINK:
            assert text_node.url is not None
            return LeafNode("a", text_node.value, {"href": text_node.url})
        case TextType.IMAGE:
            assert text_node.url is not None
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.value})
        case _:
            raise AttributeError("Invalid text type")
