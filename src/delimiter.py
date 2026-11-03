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
