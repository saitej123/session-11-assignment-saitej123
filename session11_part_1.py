import sys
import re
import math
import random


class Polygon:
    """
    A Polygon class which will generate regular polygon of
    desired vertex and circumradius. """

    def __init__(self, edges: int, circumradius: int):
        """
        This is a constructor
        """
        if type(edges) is not int:
            raise TypeError("Edges fields must be an integer")

        if edges < 3:
            raise ValueError("Edges of Polygon should be 3 or greater than 3")

        if type(circumradius) not in [int, float]:
            raise TypeError("Circumradius must be either integer or float")

        self._edges = edges
        self._circumradius = circumradius

    def __iter__(self):
        return self

    def __next__(self):
        return self

    @property
    def edges(self):
        return self._edges

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def vertices(self):
        return self._edges

    @property
    def interior_angle(self):
        return (self.edges - 2) * (180 / self.edges)

    @property
    def edge_length(self):
        return 2 * self.circumradius * math.sin(math.pi / self.edges)

    @property
    def apothem(self):
        return self.circumradius * math.cos(math.pi / self.edges)

    @property
    def area(self):
        return 0.5 * self.edges * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self.edges * self.edge_length

    def __repr__(self):
        """
        This function is used to display the output of the class object.
        """
        return f"Polygon with \n Edges: {self.edges}, \
                \n Circumradius: {self.circumradius}, \
                \n Interior Angle: {self.interior_angle}, \
                \n Edge Length: {self.edge_length:.2f}, \
                \n Apothem: {self.apothem:.2f}, \
                \n Area: {self.area:.2f}, \
                \n Perimeter: {self.perimeter:.2f}"

    def __gt__(self, other):
        """
        This class is to check greater than. It checks the self.no_edges and self.circumradius with the ones
        of the other passed in as argument
        """
        if isinstance(other, self.__class__):
            return self.vertices > other.vertices
        else:
            raise TypeError("Polygon class instance is expected")

    def __eq__(self, other):
        """
        This class is to check equality. It checks the self.no_edges and self.circumradius with the ones
        of the other passed in as argument
        """
        if isinstance(other, self.__class__):
            return (self.edges == other.edges) and (
                self.circumradius == other.circumradius
            )
        else:
            raise TypeError("Polygon class instance is expected")
