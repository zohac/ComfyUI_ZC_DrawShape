import torch
from .zc_circle import ZcCircle as Circle
from ..zc_color import ZcColor as Color
from ..utils.helpers import check_index_exists

class ZcDrawShapeFactory:
    """
    Class for drawing shapes on images.

    Attributes:
        shapes (dict): A dictionary mapping shape names to their corresponding classes.

    Methods:
        input_types: Returns the required input types for shape creation.
        make_shape: Creates one or more images with drawn shapes.
        get_shape_class: Retrieves the class for the specified shape.
        get_zoom: Retrieves the zoom factor for the given index.
        create_image: Creates an image with the specified parameters.
    """

    shapes = {
        "circle": Circle
    }

    @classmethod
    def INPUT_TYPES(cls):
        """
        Returns the required input types for shape creation.

        Returns:
            dict: A dictionary describing the required input types.
        """
        shapes = list(cls.shapes.keys())
        available_colors = Color.available_colors()

        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 64, "max": 4096}),
                "height": ("INT", {"default": 512, "min": 64, "max": 4096}),
                "shape_name": (shapes,),
                "shape_color": (available_colors, {"default": "white"}),
                "back_color": (available_colors, {"default": "black"}),
                "x_offset": ("INT", {"default": 0, "min": -2048, "max": 2048}),
                "y_offset": ("INT", {"default": 0, "min": -2048, "max": 2048}),
                "zoom": ("FLOAT", {"default": 1.00, "min": 0.00, "max": 10.00, "step": 0.05, "forceInput": True}),
                "zoom_multiplier": ("FLOAT", {"default": 1.00, "min": 0.00, "max": 10.00, "step": 0.05}),
                "batch": ("INT", {"default": 1, "min": -2048, "max": 2048}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "make_shape"
    CATEGORY = "🐉 ZC Shape"

    def make_shape(self, width, height, batch, shape_name, shape_color, back_color,
                   x_offset=0, y_offset=0, zoom=1.0, zoom_multiplier=1.0):
        """
        Creates one or more images with drawn shapes.

        Args:
            width (int): The width of the image.
            height (int): The height of the image.
            batch (int): The number of images to create.
            shape_name (str): The shape to draw.
            shape_color (str): The color of the shape.
            back_color (str): The background color of the image.
            x_offset (int, optional): The x-axis offset for the shape's position. Default is 0.
            y_offset (int, optional): The y-axis offset for the shape's position. Default is 0.
            zoom (float, optional): The zoom factor for the shape. Default is 1.0.
            zoom_multiplier (float, optional): The zoom multiplier. Default is 1.0.

        Returns:
            tuple: A tuple containing a batch of images as PyTorch tensors.
        """
        shape_class = self.get_shape_class(shape_name)
        images = [
            self.create_image(
                shape_class, width, height, shape_color, back_color,
                x_offset, y_offset, self.get_zoom(zoom, index), zoom_multiplier
            ) for index in range(batch)
        ]
        return (torch.stack(images, dim=0),)

    def get_shape_class(self, shape_name):
        """
        Retrieves the class for the specified shape.

        Args:
            shape_name (str): The name of the shape.

        Returns:
            class: The class corresponding to the shape name.

        Raises:
            ValueError: If the shape name is not recognized.
        """
        shape_class = self.shapes.get(shape_name.lower())
        if not shape_class:
            raise ValueError(f"Shape '{shape_name}' not recognized.")
        return shape_class

    def get_zoom(self, zoom, index):
        """
        Retrieves the zoom factor for the given index.

        Args:
            zoom (list or float): The zoom factors.
            index (int): The index to retrieve the zoom factor for.

        Returns:
            float: The zoom factor for the given index.
        """
        return zoom[index] if check_index_exists(zoom, index) else 0

    def create_image(self, shape_class, width, height, shape_color, back_color,
                     x_offset, y_offset, zoom, zoom_multiplier):
        """
        Creates an image with the specified parameters.

        Args:
            shape_class (class): The class of the shape to draw.
            width (int): The width of the image.
            height (int): The height of the image.
            shape_color (str): The color of the shape.
            back_color (str): The background color of the image.
            x_offset (int): The x-axis offset for the shape's position.
            y_offset (int): The y-axis offset for the shape's position.
            zoom (float): The zoom factor for the shape.
            zoom_multiplier (float): The zoom multiplier.

        Returns:
            torch.Tensor: The created image as a PyTorch tensor.
        """
        shape = shape_class()
        return shape.draw(width, height, shape_color, back_color,
                          x_offset, y_offset, zoom, zoom_multiplier)
