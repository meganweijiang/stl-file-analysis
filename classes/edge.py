from .vertex import Vertex

import math


class Edge:
    def __init__(self, vertex_1: Vertex, vertex_2: Vertex):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2

    def get_length(self):
        return math.sqrt(pow(self.vertex_2.x_coordinate - self.vertex_1.x_coordinate, 2) +
                         pow(self.vertex_2.y_coordinate - self.vertex_1.y_coordinate, 2) +
                         pow(self.vertex_2.z_coordinate - self.vertex_1.z_coordinate, 2) * 1.0)
