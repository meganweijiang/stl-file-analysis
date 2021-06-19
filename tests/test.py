from classes.edge import Edge
from classes.triangle import Triangle
from classes.vertex import Vertex

from main import *

import unittest


class Test(unittest.TestCase):
    def test_parse_vertex_line(self):
        line = 'vertex 0 0 0\n'

        self.assertEqual(parse_vertex_line(line), (0, 0, 0))

    def test_get_total_area(self):
        triangles = [Triangle(Vertex(0, 0, 0), Vertex(1, 0, 0), Vertex(1, 1, 1)), Triangle(
            Vertex(0, 0, 0), Vertex(0, 1, 1), Vertex(1, 1, 1))]

        self.assertEqual(get_total_area(triangles), 1.4142135623730956)

    def test_get_result_string(self):
        number_of_triangles = 5
        surface_area = 10.0

        self.assertEqual(get_result_string(number_of_triangles, surface_area),
                         'Number of Triangles: 5\nSurface area: 10.0')

    def test_triangle_get_area(self):
        triangle = Triangle(Vertex(0, 0, 0), Vertex(1, 0, 0), Vertex(1, 1, 1))

        self.assertEqual(triangle.get_area(), 0.7071067811865478)

    def test_edge_get_length(self):
        edge = Edge(Vertex(1, 1, 1), Vertex(2, 1, 1))

        self.assertEqual(edge.get_length(), 1)
