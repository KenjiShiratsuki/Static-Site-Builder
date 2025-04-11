from textnode import TextNode, TextType

def main():
    test_node = TextNode("This is only a text, I mean TEST", TextType.LINK, "https://www.boot.dev")
    print(test_node)


if __name__ == "__main__":
    main()