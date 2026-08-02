from textnode import TextNode, TextType


def main() -> None:
    node = TextNode("I should go for a walk", TextType.LINK, "https://www.kink.com")
    print(node)


main()
