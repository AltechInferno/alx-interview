#!/usr/bin/python3
"""Island perimeter computing
"""


def island_perimeter(grid):
    """Computes perimeter of an island with no lakes
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for l, row in enumerate(grid):
        m = len(row)
        for w, cell in enumerate(row):
            if cell == 0:
                continue
            borders = (
                l == 0 or (len(grid[l - 1]) > w and grid[l - 1][w] == 0),
                w == m - 1 or (m > w + 1 and row[w + 1] == 0),
                l == n - 1 or (len(grid[l + 1]) > w and grid[l + 1][w] == 0),
                w == 0 or row[w - 1] == 0,
            )
            perimeter += sum(borders)
    return perimeter
