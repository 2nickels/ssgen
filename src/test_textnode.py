import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This node has a link", TextType.LINK, "https://linky.link")
        node2 = TextNode("This node has a link", TextType.LINK, "https://linky.link")
        self.assertEqual(node, node2)

    def test_url_neq(self):
        node = TextNode("This node has a link", TextType.LINK, "https://linky.q")
        node2 = TextNode("This node has a link", TextType.LINK, "https://linky.link")
        self.assertNotEqual(node, node2)

    def test_text_neq(self):
        node = TextNode("This text is the same", TextType.TEXT)
        node2 = TextNode("This text is not", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://link.lnk")
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://link.lnk"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://link.lnk/image.png")
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://link.lnk/image.png", "alt": "This is an image"})

    def test_invalid_type(self):
        node = TextNode("This is invalid", TextType.TEXT)
        node.text_type = "this is invalid"  # pyright: ignore[reportAttributeAccessIssue]
        with self.assertRaises(AttributeError) as context:
            text_node_to_html_node(node)
        self.assertTrue("Invalid text type" in str(context.exception))

if __name__ == "__main__":
    unittest.main()
