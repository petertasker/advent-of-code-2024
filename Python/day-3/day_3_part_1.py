import re


def mul(match):
    # Turn tuple into two ints and multiply
    return int(match[0]) * int(match[1])


def main():
    total = 0
    with open("input") as f:
        text = f.read()
        # "mul(s,s)" s = {n, nn, nnn} n = {0,1,...,9}
        matches = re.findall(r"\bmul\((\d{1,3}),(\d{1,3})\)", text)

    for match in matches:
        product = (mul(match))
        print(f"match = {match}, product = {product}")
        total += product
    print(total)


if __name__ == '__main__':
    main()
