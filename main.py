from classes.vertex import Vertex
from classes.triangle import Triangle

import fileinput
import sys

FILE_ENDING = 'endsolid'
VERTEX_PREFIX = 'vertex'
LOOP_END = 'endloop'


def analyze_stl_file():
    triangles = []

    vertices = []

    for line in fileinput.input(sys.argv[1]):
        if (FILE_ENDING) in line:
            break
        elif (VERTEX_PREFIX) in line:
            parsed_vertex_data = parse_vertex_line(line)
            vertex = Vertex(
                parsed_vertex_data[0], parsed_vertex_data[1], parsed_vertex_data[2])

            vertices.append(vertex)
        elif (LOOP_END) in line:
            triangle = Triangle(vertices[0], vertices[1], vertices[2])
            triangles.append(triangle)

            vertices = []
        else:
            continue

    number_of_triangles = len(triangles)
    total_area_of_triangles = get_total_area(triangles)

    result = get_result_string(number_of_triangles, total_area_of_triangles)
    print(result)
    return result


def parse_vertex_line(line: str):
    return tuple(map(float, filter(None, line.replace(VERTEX_PREFIX, '').replace('\n', '').split(' '))))


def get_total_area(triangles: list):
    return sum(map(lambda triangle: triangle.get_area(), triangles))


def get_result_string(triangle_count: int, total_area: float):
    return('Number of Triangles: ' + str(triangle_count) + '\nSurface area: ' + str(total_area))


if __name__ == '__main__':
    analyze_stl_file()
