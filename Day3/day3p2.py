
import re

def mul(match):
    return int(match[0]) * int(match[1])


def tuple_to_str(match):
    return f"mul({match[0]},{match[1]})"


def main():
    total = 0
    current_do_i = -0
    current_dont_i = -0

    with open("input") as f:
        text = f.read()
        matches = re.findall(r"\bmul\((\d{1,3}),(\d{1,3})\)", text)
        do_indices = [m.start() for m in re.finditer(r"\bdo\(\)", text)]
        dont_indices = [m.start() for m in re.finditer(r"\bdon't\(\)", text)]

    for match in matches:
        match_str = tuple_to_str(match)

        match_i = text.find(match_str)
        product = (mul(match))

        print(f"match = {match}, index = {match_i} product = {product}")


        while do_indices and do_indices[0] < match_i:
            current_do_i = do_indices.pop(0)

        while dont_indices and dont_indices[0] < match_i:
            current_dont_i = dont_indices.pop(0)

        print(f"current_do_i = {current_do_i}, current_dont_i = {current_dont_i}")

        if current_do_i >= current_dont_i:
            total += product
    print(total)


if __name__ == '__main__':
    main()