import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_base_case(self):
        title, remaining = extract_title("# Title\nrest")
        self.assertEqual("Title", title)

    def test_leading_trailing_spaces(self):
        title, remaining = extract_title("  # Title  \nmore")
        self.assertEqual("Title", title)
    def enpty_title_error(self):
        with self.assertRaises(ValueError("h1 title has no text")):
            error = extract_title("# ")
    def no_h1_test(self):
        with self.assertRaises(ValueError("no h1 title found")):
            error = extract_title("Nothing here but us chickens")
    def no_space_error(self):
        with self.assertRaises(ValueError):
            error = extract_title("#Title")
    def enpty_title_error(self):
        with self.assertRaises(ValueError):
            error = extract_title("## Not H1")
    def test_h1_removed(self):
        title, remaining = extract_title("# Title\r\nA\nB")
        self.assertEqual("Title", title)
        self.assertEqual("A\nB", remaining.replace("\r\n", "\n"))