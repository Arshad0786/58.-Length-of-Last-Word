import unittest
from LengthofLastWord import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.input = "Hello World"
        self.assertEqual(temp.lengthOfLastWord(self.input), 5)

    def test_no_space_word(self):
        temp = Solution()
        self.input = "Hello"
        self.assertEqual(temp.lengthOfLastWord(self.input), 5)

    def test_long_last_word(self):
        temp = Solution()
        self.input = "Hello 0123456789012345678901234567890123456789"
        self.assertEqual(temp.lengthOfLastWord(self.input), 40)

    def test_one_word(self):
        temp = Solution()
        self.input = "a"
        self.assertEqual(temp.lengthOfLastWord(self.input), 1)

    def test_one_word_with_space(self):
        temp = Solution()
        self.input = "a   b  "
        self.assertEqual(temp.lengthOfLastWord(self.input), 1)

    def test_no_word(self):
        temp = Solution()
        self.input = " "
        self.assertEqual(temp.lengthOfLastWord(self.input), 0)

if __name__ == "__main__":
    unittest.main()
