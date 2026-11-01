import unittest

from textnode import TextNode, TextType


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
        node = TextNode("This text is the same", TextType.PLAIN)
        node2 = TextNode("This text is not", TextType.PLAIN)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
