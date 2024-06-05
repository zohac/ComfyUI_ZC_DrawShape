import numpy as np
import torch

def pil2tensor(image):
    """
    Converts a PIL image to a normalized PyTorch tensor.

    Args:
        image (PIL.Image.Image): The PIL image to convert.

    Returns:
        torch.Tensor: The normalized PyTorch tensor.
    """
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0)

def check_index_exists(array, index):
    """
    Checks if an index exists in an array.

    Args:
        array (iterable): The array or sequence to check.
        index (int): The index to check.

    Returns:
        bool: True if the index exists, False otherwise.
    """
    try:
        array[index]
        return True
    except IndexError:
        return False
