def check_valid(arr):
    return (sorted(arr) == arr or sorted(arr, reverse=True) == arr) \
        and adjacent_is_near(arr)


def adjacent_is_near(arr):
    for i in range(len(arr) - 1):
        if not 1 <= abs(arr[i] - arr[i + 1]) <= 3:
            return False
    return True


def main():
    total = 0

    with open("input") as f:
        for line in f.readlines():
            # Turn line into array of integers
            splt = [int(x) for x in line.split()]
            if check_valid(splt):
                total += 1

            # If not valid, check if any permutation satisfies
            else:
                for i in range(len(splt)):
                    temp = splt[0:i] + splt[i + 1:]
                    if check_valid(temp):
                        total += 1
                        break
        print(total)


if __name__ == '__main__':
    main()
