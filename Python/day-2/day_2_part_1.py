
def adjacent_is_near(arr):
    for i in range(len(arr) - 1):
        if not 1 <= abs(arr[i] - arr[i + 1]) <= 3:
            return False
    return True


def main():

    total = 0

    with open("input") as f:
        for line in f.readlines():
            splt = [int(x) for x in line.split()]
            if (sorted(splt) == splt or sorted(splt, reverse=True) == splt) \
                    and adjacent_is_near(splt):
                print(f"{splt}. SORTED!")
                total += 1
            else:
                print(f"{splt}. NOT SORTED!")
        print(total)

if __name__ == '__main__':
    main()