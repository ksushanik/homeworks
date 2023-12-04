import math
import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        if not self.is_valid_triangle(point1, point2, point3):
            raise ValueError("Треугольник с такими координатами точек не существует.")
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    @staticmethod
    def is_valid_triangle(p1, p2, p3):
        a = math.dist((p1.x, p1.y), (p2.x, p2.y))
        b = math.dist((p2.x, p2.y), (p3.x, p3.y))
        c = math.dist((p3.x, p3.y), (p1.x, p1.y))
        return a + b > c and b + c > a and c + a > b

    def area(self):
        a = math.dist((self.point1.x, self.point1.y), (self.point2.x, self.point2.y))
        b = math.dist((self.point2.x, self.point2.y), (self.point3.x, self.point3.y))
        c = math.dist((self.point3.x, self.point3.y), (self.point1.x, self.point1.y))
        semi_perimeter = (a + b + c) / 2
        if semi_perimeter <= 0 or (semi_perimeter - a) <= 0 or (semi_perimeter - b) <= 0 or (semi_perimeter - c) <= 0:
            return 0
        return math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

    def __str__(self):
        return f"Треугольник: ({self.point1.x}, {self.point1.y}), ({self.point2.x}, {self.point2.y}), ({self.point3.x}, {self.point3.y}) "


def read_points(filename):
    with open(filename, 'r') as file:
        points_data = file.read()
    points_match = re.findall(r'\[(\d+), (\d+)]', points_data)
    points = [Point(int(x), int(y)) for x, y in points_match]
    return points


def print_triangle_info(triangle, number):
    print(f"Треугольник {number}:")
    print("Координаты точек:")
    print(f"Точка 1: ({triangle.point1.x}, {triangle.point1.y})")
    print(f"Точка 2: ({triangle.point2.x}, {triangle.point2.y})")
    print(f"Точка 3: ({triangle.point3.x}, {triangle.point3.y})")
    print(f"Площадь: {triangle.area()}")
    print()


def find_triangles(points):
    triangles = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                try:
                    triangle = Triangle(points[i], points[j], points[k])
                    triangles.append(triangle)
                except ValueError as e:
                    print(e,
                          f"({points[i].x}, {points[i].y}), ({points[j].x}, {points[j].y}), ({points[k].x}, {points[k].y})")
    return triangles


def find_min_max_triangles(triangles):
    triangles = [triangle for triangle in triangles if triangle.area() > 0]
    min_triangle = min(triangles, key=lambda x: x.area())
    max_triangle = max(triangles, key=lambda x: x.area())
    return min_triangle, max_triangle


def main():
    points = read_points('plist.txt')
    triangles = find_triangles(points)
    min_triangle, max_triangle = find_min_max_triangles(triangles)
    print_triangle_info(min_triangle, "с наименьшей площадью")
    print_triangle_info(max_triangle, "с наибольшей площадью")


if __name__ == "__main__":
    main()
