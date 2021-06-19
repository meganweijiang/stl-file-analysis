from classes.triangle import Triangle

import fileinput

FILE_ENDING = 'endsolid'
VERTEX_PREFIX = 'vertex '
LOOP_END = 'endloop'


def analyze_stl_file():
    triangles = []

    vertices = []

    for line in fileinput.input():
        if (FILE_ENDING) in line:
            break
        elif (VERTEX_PREFIX) in line:
            vertices.append(parse_vertex_line(line))
            continue
        elif (LOOP_END) in line:
            triangle = Triangle(vertices[0], vertices[1], vertices[2])
            triangles.append(triangle)

            vertices = []

    return print(get_result(len(triangles), get_total_area(triangles)))


def parse_vertex_line(line: str):
    return tuple(map(float, filter(None, line.replace(VERTEX_PREFIX, '').replace('\n', '').split(' '))))


def get_total_area(triangles: list):
    return sum(map(lambda triangle: triangle.get_area(), triangles))


def get_result(triangle_count: int, surface_area: float):
    return('Number of Triangles: ' + str(triangle_count) + '\nSurface area: ' + str(surface_area))


if __name__ == '__main__':
    analyze_stl_file()
