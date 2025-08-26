import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type
class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_block_to_blocktype(self):
        md = """
This is a normal paragraph.

>This is a
>multi-line
>quotation.

```This is a block of code
with multiple lines
before the end```

# This is a level 1 heading

## This is a level 2 heading

### This is a level 3 heading

#### This is a level 4 heading

##### This is a level 5 heading

###### This is a level 6 heading

- This is an
- unordered list
- with multiple entries

1. This is a properly
2. Ordered list
3. with multiple entries
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(blocks[0]))
        self.assertEqual(BlockType.QUOTE, block_to_block_type(blocks[1]))
        self.assertEqual(BlockType.CODE, block_to_block_type(blocks[2]))
        self.assertEqual(BlockType.HEADING, block_to_block_type(blocks[3]))
        self.assertEqual(BlockType.HEADING, block_to_block_type(blocks[4]))
        self.assertEqual(BlockType.HEADING, block_to_block_type(blocks[5]))
        self.assertEqual(BlockType.HEADING, block_to_block_type(blocks[6]))
        self.assertEqual(BlockType.HEADING, block_to_block_type(blocks[7]))
        self.assertEqual(BlockType.HEADING, block_to_block_type(blocks[8]))
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(blocks[9]))
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(blocks[10]))