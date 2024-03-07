#!/usr/bin/python3
"""Island perimeter computing
"""


def island_perimeter(grid):
 """Computes perimeter of an island with no lakes
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check if there's land in neighboring cells
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
