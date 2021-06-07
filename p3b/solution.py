def solution(x, y):
    steps = 0
    array_of_bombs = [int(x), int(y)]
    if 1 in array_of_bombs:
        return str(max(array_of_bombs) - 1)
    while array_of_bombs[0] != 1 and array_of_bombs[1] != 1:
        array_of_bombs = sorted(array_of_bombs)
        if 0 in array_of_bombs:
            return "impossible"
        leap_step = array_of_bombs[1] / array_of_bombs[0]
        array_of_bombs[1] = array_of_bombs[1] - (array_of_bombs[0] * leap_step)
        steps += leap_step
    return str(steps + max(array_of_bombs) - 1)
