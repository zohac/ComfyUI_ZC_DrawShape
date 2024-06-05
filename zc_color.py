class ZcColor:
    """
    Class representing a color with methods to convert between RGB and hexadecimal formats.

    Attributes:
        COLORS (dict): A dictionary of predefined color names and their RGB values.
        rgb (tuple): The RGB value of the color instance.
    """

    COLORS = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'magenta': (255, 0, 255)
    }

    def __init__(self, name=None):
        """
        Initializes a ZcColor instance.

        Args:
            name (str, optional): The name of the color. Must be one of the predefined colors.

        Raises:
            ValueError: If the color name is not recognized or not provided.
        """
        if name:
            if name in self.COLORS:
                self.rgb = self.COLORS[name]
            else:
                raise ValueError("Unrecognized color name. Use 'black', 'white', 'red', 'green', 'blue', 'yellow', or 'magenta'.")
        else:
            raise ValueError("You must provide a color name, RGB values, or a hexadecimal value.")

    @staticmethod
    def hex_to_rgb(hex_value):
        """
        Converts a hexadecimal color value to an RGB tuple.

        Args:
            hex_value (str): The hexadecimal color value.

        Returns:
            tuple: The RGB value as a tuple.
        """
        hex_value = hex_value.lstrip('#')
        return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb):
        """
        Converts an RGB tuple to a hexadecimal color value.

        Args:
            rgb (tuple): The RGB value as a tuple.

        Returns:
            str: The hexadecimal color value.
        """
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

    def to_rgb(self):
        """
        Returns the RGB value of the color instance.

        Returns:
            tuple: The RGB value.
        """
        return self.rgb

    def to_hex(self):
        """
        Returns the hexadecimal value of the color instance.

        Returns:
            str: The hexadecimal value.
        """
        return self.rgb_to_hex(self.rgb)

    @classmethod
    def available_colors(cls):
        """
        Returns a list of available color names.

        Returns:
            list: A list of color names.
        """
        return list(cls.COLORS.keys())

    def __repr__(self):
        """
        Returns a string representation of the color instance.

        Returns:
            str: A string representation of the color.
        """
        return f"Color(rgb={self.rgb}, hex='{self.to_hex()}')"
