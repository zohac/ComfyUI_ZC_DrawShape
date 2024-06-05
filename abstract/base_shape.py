from abc import ABC, abstractmethod

class BaseShape(ABC):
    """
    Abstract base class for shapes.

    Methods:
        draw: Abstract method to draw the shape.
    """

    @abstractmethod
    def draw(self):
        """
        Abstract method to draw the shape.

        This method should be implemented by subclasses to draw the specific shape.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        raise NotImplementedError("The draw method must be implemented by subclasses.")
