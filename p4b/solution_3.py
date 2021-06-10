import itertools


def answer(num_buns, num_required):
    r = []

    # Applying pegion rule
    f = list(itertools.combinations(range(num_buns), num_required))
    total = len(f) * num_required
    repeat_times = num_buns - num_required + 1
    f1 = list(itertools.combinations(range(num_buns), repeat_times))
    for i in range(num_buns):
        r.append([])

    for i in range(total / repeat_times):
        for j in f1[i]:
            r[j].append(i)

    return r


print(answer(5, 3))
