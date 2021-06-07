def solution(n):
    n = int(n)  # Convert it to integer. Questions constraints states that these are whole numbers
    steps = 0  # Initialize steps to 0
    # Continue loop till you reach 1
    while n > 1:
        # ===== Step 1. If number is divisible by 2, keep dividing it =====
        # The largest reduction of the number is division, and hence, keep on
        # performing that whenever the opportunity arises.
        if n % 2 == 0:
            n = n / 2
            steps += 1
            continue

        # ===== Step 2: Determine the path =====
        # Usually, if you have an odd number, say, something like 15, then there are two ways to
        # make it into an even number. Either add 1 to make it to 16 or subtract one to make it
        # to 14. One of those is the optimal path. We could compute both the paths, but the
        # optimal path lies in making it fall on the path of power of 2. To do so, we check the
        # mod of 4, hence, the answer could either be 3 or 1. If it's 1, then the number just
        # larger than a number closer to power of 2, and hence, subtract 1, else, add 1 to make
        # it fall on the path of power of 2.

        # There is an edge case for this though, if the number is 3. If that's the case, then
        # and addition of 1 will lead to 3 steps, and a subtraction will lead to 2 steps,
        # so add that edge case to the condition too.

        if n % 4 == 1 or n == 3:
            n -= 1
            steps += 1
            continue
        else:
            n += 1
            steps += 1
            continue

    return steps


print(solution('15'))