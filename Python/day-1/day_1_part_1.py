def main():
    sum = 0
    leftLst = []
    rightLst = []

    # Parse file into two lists.
    with open("input") as f:
        for line in f.readlines():
            splt = line.split()
            leftLst.append(int(splt[0]))
            rightLst.append(int(splt[1]))
    leftLst.sort()
    rightLst.sort()

    # Sum the absolute difference between each index of the two lists.
    for i in range(len(leftLst)):
        ans = (abs(leftLst[i] - rightLst[i]))
        sum += ans
        print(f"leftLst[i] - rightLst[i] = {ans}, sum = {sum}")

    print(f"Final sum = {sum}")


if __name__ == '__main__':
    main()
