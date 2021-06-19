import math


class Triangle:
    def __init__(self, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3):
        self.vertex_1 = self.Vertex(x_1, y_1, z_1)
        self.vertex_2 = self.Vertex(x_2, y_2, z_2)
        self.vertex_3 = self.Vertex(x_3, y_3, z_3)
        self.length_a = self.Edge(self.vertex_1, self.vertex_2).get_length()
        self.length_b = self.Edge(self.vertex_2, self.vertex_3).get_length()
        self.length_c = self.Edge(self.vertex_1, self.vertex_3).get_length()

    def get_area(self):
        semi_perimeter = (self.length_a, self.length_b, self.length_c) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.length_a) * (semi_perimeter - self.length_b) * (semi_perimeter - self.length_c))

    class Vertex:
        def __init__(self, x_coordinate, y_coordinate, z_coordinate):
            self.x_coordinate = x_coordinate
            self.y_coordinate = y_coordinate
            self.z_coordinate = z_coordinate

        def __get__(self):
            return (self.x_coordinate, self.y_coordinate, self.z_coordinate)

    class Edge:
        def __init__(self, vertex_1, vertex_2):
            self.vertex_1 = vertex_1
            self.vertex_2 = vertex_2

        def get_length(self):
            return math.sqrt(pow(self.vertex_2.x_coordinate - self.vertex_1.x_coordinate, 2) +
                             pow(self.vertex_2.y_coordinate - self.vertex_1.y_coordinate, 2) +
                             pow(self.vertex_2.z_coordinate - self.vertex_1.z_coordinate, 2) * 1.0)
