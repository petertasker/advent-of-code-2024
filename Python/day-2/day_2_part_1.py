
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

            # If all in ascending or descending series and each neighbour is 1 <= i <= 3
            if (sorted(splt) == splt or sorted(splt, reverse=True) == splt) \
                    and adjacent_is_near(splt):
                print(f"{splt}. SORTED!")
                total += 1
            else:
                print(f"{splt}. NOT SORTED!")
        print(total)


if __name__ == '__main__':
    main()
