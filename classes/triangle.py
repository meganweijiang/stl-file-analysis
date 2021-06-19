from .edge import Edge
from .vertex import Vertex
import math


class Triangle:
    def __init__(self, vertex_1=tuple, vertex_2=tuple, vertex_3=tuple):
        self.vertex_1 = Vertex(vertex_1[0], vertex_1[1], vertex_1[2])
        self.vertex_2 = Vertex(vertex_2[0], vertex_2[1], vertex_2[2])
        self.vertex_3 = Vertex(vertex_3[0], vertex_3[1], vertex_3[2])

    def get_area(self):
        length_a = Edge(self.vertex_1, self.vertex_2).get_length()
        length_b = Edge(self.vertex_2, self.vertex_3).get_length()
        length_c = Edge(self.vertex_1, self.vertex_3).get_length()

        semi_perimeter = (length_a + length_b + length_c) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - length_a) * (semi_perimeter - length_b) * (semi_perimeter - length_c))
