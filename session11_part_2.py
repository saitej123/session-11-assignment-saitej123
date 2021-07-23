
from session11_part_1 import Polygon

class PolygonSequence():
    """
    This is a polygon sequence class used to develop a custom sequence
    """
    def __init__(self, edges, circumradius):
        self._edges = edges
        self._circumradius = circumradius

    def __iter__(self):
        return self.PolygonIter(self)

    def __len__(self):
        return self._edges - 2

    def __repr__(self):
        return f'PolygonSequence(Edges = {self._edges}, Circumradius = {self._circumradius})'

    @property
    def efficient_polygon(self):
        sorted_polygons = sorted(
            self, key=lambda p: p.area/p.perimeter, reverse=True)
        return sorted_polygons[0]

    class PolygonIter:
        """
        This is a polygon ITERATOR
        (next method callable only with iterator : lazily produce next value )
        """
        def __init__(self, poly_obj):
            self._index = 3
            self._poly_obj = poly_obj

        def __iter__(self):
            return self

        def __next__(self):
            if self._index > self._poly_obj._edges:
                raise StopIteration
            else:
                item = Polygon(self._index, self._poly_obj._circumradius)
                self._index += 1
                return item
