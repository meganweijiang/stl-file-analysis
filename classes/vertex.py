class Vertex:
    def __init__(self, x_coordinate: float, y_coordinate: float, z_coordinate: float):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return NotImplemented

        return self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate and self.z_coordinate == other.z_coordinate
