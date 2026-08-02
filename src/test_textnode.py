import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_match(self):
        node = TestTextNode("This is a test node", TextType.LINK, "www.google.com")
        node2 = TestTextNode("This isn't a test node", TextType.LINK, "www.kink.com")
        self.assertNotEqual(node, node2)

    def test_link_none(self):
        node = TestTextNode("Rotten Mango", TextType.ITALIC)
        node2 = TestTextNode("Rotten Mango", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_text_type(self):
        node = TestTextNode("Aang is the best Avatar!", TextType.BOLD)
        node2 = TestTextNode("Katara is the best Avatar!", TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()