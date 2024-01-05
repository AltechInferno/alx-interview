#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    func that returns a list
    of integers representing de
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)

