import re
import numpy as np

def count_totals(lines):
    total = 0
    # Forwards

    total += count_horizontal(lines)
    total += count_vertical(lines)
    total += count_diagonal(lines)

    total += count_horizontal_reversed(lines)
    total += count_vertical_reversed(lines)
    total += count_diagonal_reversed(lines)
    return total


def count_horizontal(lines):
    count = 0
    for line in lines:
        count += sum(1 for m in re.finditer("XMAS", line))
    return count


def count_horizontal_reversed(lines):
    count = 0
    for line in lines:
        count += sum(1 for m in re.finditer("XMAS", line[::-1]))
    return count


def count_vertical(lines):
    count = 0
    # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    rotated = ["".join(line) for line in list(zip(*lines[::-1]))]
    return count_horizontal(rotated)


def count_vertical_reversed(lines):
    reversed_lines = [line[::-1] for line in lines]  # Reverse each line
    rotated = ["".join(line) for line in zip(*reversed_lines)]
    return count_horizontal(rotated)


def count_diagonal(lines):
    count = 0
    # Matrix of all diagonals
    matrix = [list(line) for line in lines]
    matrix = np.array(matrix)
    diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1] - 1, -matrix.shape[0], -1))

    # print([n.tolist() for n in diags])
    for diag in diags:
        diag_str = "".join(diag)
        count += sum(1 for m in re.finditer("XMAS", diag_str))
    return count


def count_diagonal_reversed(lines):
    reversed_lines = [line[::-1] for line in lines]
    return count_diagonal(reversed_lines)


def main():
    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]
    total = count_totals(lines)
    print(total)

if __name__ == '__main__':
    main()
