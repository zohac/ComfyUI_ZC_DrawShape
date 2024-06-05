import unittest
from PIL import Image
import numpy as np
import torch
from ..utils.helpers import check_index_exists, pil2tensor

class TestHelpers(unittest.TestCase):
    def test_check_index_exists(self):
        self.assertTrue(check_index_exists([1, 2, 3], 1))
        self.assertFalse(check_index_exists([1, 2, 3], 3))

    def test_pil2tensor(self):
        img = Image.new('RGB', (10, 10), color='red')
        tensor = pil2tensor(img)
        self.assertIsInstance(tensor, torch.Tensor)
        self.assertEqual(tensor.shape, (10, 10, 3))
        self.assertTrue(np.allclose(tensor.numpy(), np.array(img).astype(np.float32) / 255.0))

if __name__ == '__main__':
    unittest.main()
