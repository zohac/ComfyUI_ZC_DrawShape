from PIL import Image, ImageDraw
from ..zc_color import ZcColor as Color
from ..utils.helpers import pil2tensor
from ..abstract.base_shape import BaseShape

class ZcCircle(BaseShape):
    """
    Class for drawing a circle on an image.

    Methods:
        draw: Draws a circle on an image with the specified parameters.
    """

    def draw(self, width, height, shape_color, back_color,
             x_offset=0, y_offset=0, zoom=1.0, zoom_multiplier=1.0):
        """
        Draws a circle on an image.

        Args:
            width (int): The width of the image.
            height (int): The height of the image.
            shape_color (str): The color of the shape.
            back_color (str): The background color of the image.
            x_offset (int, optional): The x-axis offset for the shape's position. Default is 0.
            y_offset (int, optional): The y-axis offset for the shape's position. Default is 0.
            zoom (float, optional): The zoom factor for the shape. Default is 1.0.
            zoom_multiplier (float, optional): The zoom multiplier. Default is 1.0.

        Returns:
            torch.Tensor: The created image as a PyTorch tensor.
        """
        bg_color = Color(name=back_color)
        shape_color = Color(name=shape_color)

        img = Image.new("RGB", (width, height), color=bg_color.to_rgb())
        draw = ImageDraw.Draw(img)

        center_x = width // 2 + x_offset
        center_y = height // 2 + y_offset
        size = min(width - x_offset, height - y_offset) * zoom * zoom_multiplier

        radius = size / 2

        draw.ellipse([(center_x - radius, center_y - radius),
                      (center_x + radius, center_y + radius)],
                     fill=shape_color.to_hex())

        return pil2tensor(img)
