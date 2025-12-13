from enum import Flag, auto
from itertools import combinations
from math import dist

class Direction(Flag):
    Up = auto()
    Right = auto()
    Down = auto()
    Left = auto()
    

class Corner:
    def __init__(self, point, direction):
        self.x, self.y = point
        self.direction = direction

# Always straight for the purpose of this puzzle
class Line:
    def __init__(self, p1, p2, min_x = None, min_y = None):
        if min_x:
            p1[0] = min(min_x, p1[0])
            p2[0] = min(min_x, p2[0])
        if min_y:
            p1[1] = min(min_x, p1[1])
            p2[1] = min(min_x, p2[1])

        self.point1 = p1
        self.point2 = p2
        self.min_x, self.max_x = sorted([p1[0], p2[0]])
        self.min_y, self.max_y = sorted([p1[1], p2[1]])

    
    def is_vertical(self):
        return self.min_x == self.max_x
    
    def same_orientation(self, other_line):
        return self.is_vertical() == other_line.is_vertical()
    
    def get_over_extension(self, other_line):
        over_extension = None
        if self.is_vertical():
            if self.min_x == other_line.min_x and self.max_y > other_line.max_y:
                over_extension = Line(self.point1, self.point2, min_y=other_line.max_y)
        elif self.min_y == other_line.min_y and self.max_x > other_line.max_x:
            over_extension = Line(self.point1, self.point2, min_x=other_line.max_x)
        return over_extension
    
    def cross_intersects(self, other_line):
        horizontal_line, vertical_line = sorted([self, other_line], key=lambda l:l.is_vertical())
        return (horizontal_line.min_x < vertical_line.min_x < horizontal_line.max_x 
                and vertical_line.min_y < horizontal_line.min_y < vertical_line.max_y)

    def intersects_horizontally(self, vertical_line):
        if self.is_vertical():
            return False
        return (self.min_x < vertical_line.min_x < self.max_x
                and vertical_line.min_y < self.min_y < vertical_line.max_y)

    def intersects_vertically(self, horizontal_line):
        if not self.is_vertical():
            return False
        return (horizontal_line.min_x < self.min_x < horizontal_line.max_x
                and self.min_y < horizontal_line.min_y < self.max_y)


def day9_part1(input_path: str)->int:
    corner_coordinates : list[tuple[int]] = []
    with open(input_path, 'r', encoding='utf-8') as input_file:
        for coordinate in input_file.read().splitlines():
            corner_coordinates.append(tuple[int](int(pos) for pos in coordinate.split(',')))
    
    orig_point = (0, 0)
    corner_coordinates.sort(key=lambda cord: dist(orig_point, cord))
    biggest_rect_dimension = tuple(point2 - point1 + 1 for point1, point2 in zip(corner_coordinates[0], corner_coordinates[-1]))
    return biggest_rect_dimension[0] * biggest_rect_dimension[1]


def is_rect_in_area(top_corner, bottom_corner, horizontal_area_edges, vertical_area_edges, x_corner_map, y_corner_map):
    min_x, max_x = sorted([top_corner[0], bottom_corner[0]])
    min_y = top_corner[1]
    max_y = bottom_corner[1]
    
    rect_edges = [
        (Line((min_x, min_y), (max_x, min_y)), Direction.Down),
        (Line((min_x, min_y), (min_x, max_y)), Direction.Right),
        (Line((max_x, min_y), (max_x, max_y)), Direction.Left),
        (Line((min_x, max_y), (max_x, max_y)), Direction.Up),
    ]
    for rect_edge, concave_direction in rect_edges:
        if rect_edge.is_vertical():
            for area_edge in horizontal_area_edges:
                if rect_edge.cross_intersects(area_edge):
                    return False
                for corner in x_corner_map[rect_edge.min_x]:
                    if rect_edge.min_y < corner.y < rect_edge.max_y and concave_direction in corner.direction:
                        return False
        else:
            for area_edge in vertical_area_edges:
                if rect_edge.cross_intersects(area_edge):
                    return False
            for corner in y_corner_map[rect_edge.min_y]:
                if rect_edge.min_x < corner.x < rect_edge.max_x and concave_direction in corner.direction:
                    return False
                
    return True


def day9_part2(input_path: str) -> int:
    corner_coordinates: list[tuple[int, int]] = []

    with open(input_path, 'r', encoding='utf-8') as input_file:
        for coordinate in input_file.read().splitlines():
            new_corner_cord = (tuple[int, int](int(pos) for pos in coordinate.split(',')))
            corner_coordinates.append(new_corner_cord)

    horizontal_area_edges, vertical_area_edges, x_corner_map, y_corner_map = ([], [], {}, {})
    for i in range(len(corner_coordinates)):
        corner = corner_coordinates[i]
        prev_corner = corner_coordinates[i-1]
        next_corner = corner_coordinates[(i+1) % len(corner_coordinates)]
        direction = Direction(0)
        for adjacent_corner in [prev_corner, next_corner]:
            if adjacent_corner[0] < corner[0]:
                direction |= Direction.Left
            if adjacent_corner[0] > corner[0]:
                direction |= Direction.Right
            if adjacent_corner[1] < corner[1]:
                direction |= Direction.Up
            if adjacent_corner[1] > corner[1]:
                direction |= Direction.Down
        corner = Corner(corner, direction)
        new_line = Line(corner_coordinates[i - 1], corner_coordinates[i])
        if new_line.is_vertical():
            vertical_area_edges.append(new_line)
        else:
            horizontal_area_edges.append(new_line)
        if corner.x in x_corner_map:
            x_corner_map[corner.x].append(corner)
        else:
            x_corner_map[corner.x] = [corner]
        if corner.y in y_corner_map:
            y_corner_map[corner.y].append(corner)
        else:
            y_corner_map[corner.y] = [corner]
    
    corner_coordinates.sort(key=lambda cord: (cord[1], cord[0]))
    biggest_area = 0
    
    for top_corner, bottom_corner in combinations(corner_coordinates, 2):
        if bottom_corner[1] <= top_corner[1]:
            continue
        if not is_rect_in_area(top_corner, bottom_corner,  horizontal_area_edges, vertical_area_edges, x_corner_map, y_corner_map):
            continue

        rect_area = (abs(top_corner[0] - bottom_corner[0]) + 1) * (abs(top_corner[1] - bottom_corner[1]) + 1)
        if rect_area > biggest_area:
            biggest_area = rect_area
            
                    
    return biggest_area


if __name__ == '__main__':
    print("-----DAY 09----")
    print("Examples:")
    print(f'Part1: {day9_part1("inputs/day09_test")}')
    print(f'Part2: {day9_part2("inputs/day09_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day9_part1("inputs/day09")}')
    print(f'Part2: {day9_part2("inputs/day09")}')
   
