import itertools


def solution(num_buns, num_required):
    # Your code here
    bunnies = [[]] * num_buns
    bunnies = [[] for _ in range(num_buns)]
    distinct_copies = num_buns - num_required + 1

    for key, combo_bun in enumerate(itertools.combinations(range(num_buns), distinct_copies)):
        for bunny in combo_bun:
            bunnies[bunny].append(key)

    return bunnies


print(solution(5, 3))
