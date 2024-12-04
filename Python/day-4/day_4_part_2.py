def rotate(lines):
    return ["".join(line) for line in list(zip(*lines[::-1]))]

def main():
    count = 0

    with open("input") as f:
        lines = [line.strip() for line in f.readlines()]

    # Rotate three times
    for i in range(4):
        this_pass = 0
        for y in range(len(lines) - 2):
            for x in range(len(lines[y]) - 2):

                # M . M
                # . A .
                # S . S
                if lines[y][x] == "M" and lines[y][x + 2] == "M" \
                        and lines[y + 1][x + 1] == "A" \
                        and lines[y + 2][x] == "S" and lines[y + 2][x + 2] == "S":
                    # print("")
                    # print(lines[y][x], lines[y][x+1], lines[y][x+2])
                    # print(lines[y+1][x], lines[y+1][x+1], lines[y+1][x+2])
                    # print(lines[y+2][x], lines[y+2][x+1], lines[y+2][x+2])

                    this_pass += 1

        lines = rotate(lines)
        count += this_pass
        print(f"Count for pass {i}: {this_pass}. Total: {count}")
    print(count)
if __name__ == '__main__':
    main()
