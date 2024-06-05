import unittest
from ..zc_color import ZcColor

class TestZcColor(unittest.TestCase):
    def test_color_initialization(self):
        color = ZcColor('red')
        self.assertEqual(color.to_rgb(), (255, 0, 0))

    def test_invalid_color_name(self):
        with self.assertRaises(ValueError):
            ZcColor('invalid_color')

    def test_hex_to_rgb(self):
        self.assertEqual(ZcColor.hex_to_rgb('#ff0000'), (255, 0, 0))

    def test_rgb_to_hex(self):
        self.assertEqual(ZcColor.rgb_to_hex((255, 0, 0)), '#ff0000')

    def test_available_colors(self):
        self.assertIn('red', ZcColor.available_colors())

if __name__ == '__main__':
    unittest.main()
