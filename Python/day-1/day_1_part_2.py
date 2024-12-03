def main():
    sum = 0
    leftLst = []
    dct = {}

    # Parse file into two lists.
    with open("input") as f:
        for line in f.readlines():
            splt = line.split()
            leftLst.append(int(splt[0]))
            rightNum = int(splt[1])
            # Increment dict value or set new value to 1
            dct[rightNum] = dct.get(rightNum, 0) + 1

    # Access key value
    for num in leftLst:
        sum += num * dct.get(num, 0)
        print(f"leftLst[i] = {num}, times this number has been seen = {dct.get(num)}, sum = {sum}")

    print(f"sum = {sum}")


if __name__ == '__main__':
    main()
