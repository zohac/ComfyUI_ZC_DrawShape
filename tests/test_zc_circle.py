import unittest
import torch
from ..nodes.zc_circle import ZcCircle

class TestZcCircle(unittest.TestCase):
    def setUp(self):
        self.circle = ZcCircle()

    def test_draw(self):
        result = self.circle.draw(512, 512, 'white', 'black')
        self.assertIsInstance(result, torch.Tensor)

if __name__ == '__main__':
    unittest.main()
