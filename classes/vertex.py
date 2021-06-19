class Vertex:
    def __init__(self, x_coordinate: float, y_coordinate: float, z_coordinate: float):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate

    def __get__(self):
        return (self.x_coordinate, self.y_coordinate, self.z_coordinate)
