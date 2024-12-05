from itertools import permutations

def main():
    # In rules X|Y, X must be printed before Y
    rules = []
    updates = []
    with open("input") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if "|" in line:
                rule = line.split("|")
                rules.append((int(rule[0]), int(rule[1])))
            elif line:
                update = line.split(",")
                updates.append([int(x) for x in update])

    # Find correct Orders
    for rule in rules:
        print(rule)
    # print(updates)



    good_updates = []
    bad_updates = []
    for update in updates:
        is_valid = True
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    is_valid = False
                    break
        if not is_valid:
            bad_updates.append(update)

    # Check all permutations of bad updates
    for update in bad_updates:
        perms = list(permutations(update))
        for perm in perms:
            is_valid = True
            for x, y in rules:
                if x in perm and y in perm:
                    if perm.index(x) > perm.index(y):
                        is_valid = False
                        break
            if is_valid:
                good_updates.append(update)
    print(f"Good updates: {good_updates}")
    middle_pages = [order[len(order) // 2] for order in good_updates]

    print(sum(middle_pages))

if __name__ == '__main__':
    main()