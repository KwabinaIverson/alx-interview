#!/usr/bin/env python3
"""Graph. Finding perimeter of an Island."""


def island_perimeter(grid):
    """Find the perimeter of the 2D matrix.
    Arg:
        -grid (List[List]): 0 represents water
            1 represents land
            Each cell is square, with a side length of 1
            Cells are connected horizontally/vertically (not diagonally).
            grid is rectangular, with its width and height not exceeding 100
    Return:
        perimeter (int): Calculated perimeter of the Island.
    """
    perimeter = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (grid[i][j] == 1):

                # Check left for water
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

                # Check right for water
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

                # Check top for water
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1

                # Check bottom for water
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter
