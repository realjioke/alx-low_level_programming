#!/usr/bin/python3
"""
    This module contains island_perimeter which finds
    the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
        Finds the perimeter of an island in a grid
        ** grid is a list of integer
        ** 0 represents a water zone
        ** 1 represents a land zone
        ** One cell is a square with side length 1
        ** cells are connected horizontally/vertically (not diagonally
        ** gridth is rectangular, width and height doesnt exceed 100
    """

    perimeter = 0
    nrows = len(grid)

    if grid != []:
        ncolumns = len(grid[0])

    for a in range(nrows):
        for b in range(ncolumns):
            if grid[a][b] == 1:
                if (a - 1) == -1 or grid[a - 1][b] == 0:
                    perimeter += 1
                if (a + 1) == nrows or grid[a + 1][b] == 0:
                    perimeter += 1
                if (b - 1) == -1 or grid[a][b - 1] == 0:
                    perimeter += 1
                if (b + 1) == ncolumns or grid[a][b + 1] == 0:
                    perimeter += 1

    return perimeter
