import unittest
import torch
from ..nodes.zc_draw_shape_factory import ZcDrawShapeFactory

class TestZcDrawShapeFactory(unittest.TestCase):
    def setUp(self):
        self.factory = ZcDrawShapeFactory()

    def test_input_types(self):
        input_types = self.factory.input_types()
        self.assertIn('required', input_types)
        self.assertIn('shape_name', input_types['required'])
        self.assertIn('circle', input_types['required']['shape_name'][0])

    def test_make_shape(self):
        result = self.factory.make_shape(512, 512, 1, 'circle', 'white', 'black')
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], torch.Tensor)

    def test_invalid_shape_name(self):
        with self.assertRaises(ValueError):
            self.factory.make_shape(512, 512, 1, 'invalid_shape', 'white', 'black')

if __name__ == '__main__':
    unittest.main()
