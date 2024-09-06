import unittest

from main import f

class TestCharacterCountFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(f(""), {})
    
    def test_white_space_string(self):
        self.assertEqual(f("my name"), {"m": 2, "y": 1, " ": 1, "n": 1, "a": 1, "e": 1})
    
    def test_special_character(self):
        self.assertEqual(f("!@#$%"), {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1})

    def test_mixed_characters_and_numbers(self):
        self.assertEqual(f("abc123abc"), {'a': 2, 'b': 2, 'c': 2, '1': 1, '2': 1, '3': 1})
    
    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            f(12345)
        
    def test_mixed_case(self):
        self.assertEqual(f("AaAa"), {'A': 2, 'a': 2})
    
    def test_long_string(self):
        s = "abc" * 1000
        self.assertEqual(f(s), {'a': 1000, 'b': 1000, 'c': 1000})

if __name__ == "__main__":
    unittest.main()
