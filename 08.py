from typing import List

from utils import read_file

data = [[int(ch) for ch in list(s)] for s in read_file('08')]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

num_rows, num_cols = len(data), len(data[0])


def tree_is_visible(grid: List[List[int]], i: int, j: int, tree: int) -> bool:
    def up():
        for k in range(i - 1, -1, -1):
            if grid[k][j] >= tree:
                return False
        return True

    def down():
        for k in range(i + 1, num_rows):
            if grid[k][j] >= tree:
                return False
        return True

    def left():
        for k in range(j - 1, -1, -1):
            if grid[i][k] >= tree:
                return False
        return True

    def right():
        for k in range(j + 1, num_cols):
            if grid[i][k] >= tree:
                return False
        return True

    return any([up(), down(), left(), right()])


def get_scenic_score(grid: List[List[int]], i: int, j: int, tree: int) -> int:
    def up():
        score = 0
        for k in range(i - 1, -1, -1):
            score += 1
            if grid[k][j] >= tree:
                break
        return score

    def down():
        score = 0
        for k in range(i + 1, num_rows):
            score += 1
            if grid[k][j] >= tree:
                break
        return score

    def left():
        score = 0
        for k in range(j - 1, -1, -1):
            score += 1
            if grid[i][k] >= tree:
                break
        return score

    def right():
        score = 0
        for k in range(j + 1, num_cols):
            score += 1
            if grid[i][k] >= tree:
                break
        return score

    return up() * down() * left() * right()


def get_num_visible_trees(grid: List[List[int]]) -> int:
    total_visible = 0
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            tree = grid[i][j]
            if tree_is_visible(grid, i, j, tree):
                total_visible += 1

    return total_visible + (num_rows * 2) + ((num_cols - 2) * 2)


def get_max_scenic_score(grid: List[List[int]]) -> int:
    max_scenic_score = 0
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            tree = grid[i][j]
            max_scenic_score = max(max_scenic_score, get_scenic_score(grid, i, j, tree))
    return max_scenic_score


p1 = get_num_visible_trees(data)
p2 = get_max_scenic_score(data)

print(p1)
print(p2)
