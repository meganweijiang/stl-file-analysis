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

    return print_result(len(triangles), get_total_area(triangles))


def parse_vertex_line(line):
    return tuple(map(float, filter(None, line.replace(VERTEX_PREFIX, '').replace('\n', '').split(' '))))


def get_total_area(triangles):
    return sum(map(lambda triangle: triangle.get_area(), triangles))


def print_result(triangle_count, total_area):
    print('Triangle count: ' + str(triangle_count))
    print('Surface area: ' + str(total_area))


if __name__ == '__main__':
    analyze_stl_file()
