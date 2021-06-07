class Space:
    def __init__(self, open, x, y):
        self.open = open
        self.x = x
        self.y = y
        self.h = 1
        self.g = 0
        self.f = None
        self.parent = None

    def id(self):
        return str(("f(" + str(self.f) + ")=g(" + str(self.g) + ")+h(" + str(self.h) + ")", self.y, self.x))

    def __eq__(self, a):
        return a.x == self.x and a.y == self.y


class Grid:
    def __init__(self, matrix):
        self.matrix = matrix
        self.w = len(matrix[0])
        self.l = len(matrix)
        self.data = [[Space(matrix[y][x] == 0, x, y) for x in range(self.w)] for y in range(self.l)]
        self.end = self.data[self.l - 1][self.w - 1]
        self.first = self.data[0][0]
        self.first.h = abs(0 - self.end.x) + abs(0 - self.end.y)
        self.first.g = 1
        self.first.f = self.first.h + 1

    def clone(self):
        return Grid(self.matrix)


def solution(matrix):
    grid = Grid(matrix)
    ones = [(y, x) for x in range(grid.w) for y in range(grid.l) if matrix[y][x] == 1]
    if ones:
        shortest = 500
        for (y, x) in ones:
            temp = grid.clone()
            temp.data[y][x].open = True
            short = getShortest(temp)
            if short != None and short < shortest:
                shortest = short
    else:
        shortest = getShortest(grid)
    print shortest
    return shortest


def getShortest(grid):
    q = []
    checked = []
    q.append(grid.first)
    while q:
        cur = q.pop()
        checked.append(cur)
        if cur == grid.end:
            break
        steps = getSurroundingSpaces(cur, grid)
        for step in steps:
            shouldAddToQ = True
            if not step.open:
                shouldAddToQ = False
            else:
                for old in checked:
                    if old == step:
                        shouldAddToQ = False
                for old in q:
                    if old == step:
                        shouldAddToQ = False
            if shouldAddToQ:
                new = update(step, cur, grid.end)
                q.append(new)
                q.sort(key=getF, reverse=True)
    return grid.end.f


def getF(a):
    return a.f


def getSurroundingSpaces(cur, grid):
    l, w = grid.l, grid.w
    matrix = grid.data
    spaces = []
    if cur.x < w - 1:
        spaces.append(matrix[cur.y][cur.x + 1])
    if cur.x > 0:
        spaces.append(matrix[cur.y][cur.x - 1])
    if cur.y < l - 1:
        spaces.append(matrix[cur.y + 1][cur.x])
    if cur.y > 0:
        spaces.append(matrix[cur.y - 1][cur.x])
    return spaces


def isSpace(x):
    return x.open


def update(n, cur, end):
    if n.g == 0:
        n.h = abs(n.x - end.x) + abs(n.y - end.y)
    parent = cur
    n.g = cur.g + 1
    n.f = n.g + n.h
    return n

    # 0 0 0 0 0 0
    # 0 1 1 1 1 0
    # 0 0 0 0 0 0
    # 0 1 1 1 1 1
    # 0 1 1 1 1 1
    # 0 0 0 0 0 0


def test_solution():
    assert solution([
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0]
    ]) == 8

    assert solution([
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 9

    # assert solution([
    #     [0, 1, 0, 0, 0],
    #     [0, 0, 0, 1, 0],
    #     [0, 0, 1, 1, 1],
    #     [0, 1, 1, 0, 0],
    #     [0, 1, 1, 0, 0]
    # ]) == 11

    assert solution([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 14

    assert solution([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0]
    ]) == 13

    assert solution([
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]) == 7

    assert solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 11

    assert solution([
        [0, 0],
        [0, 0]
    ]) == 3

    assert solution([
        [0, 0],
        [0, 1]
    ]) == 3


test_solution()


# 0 0 0 0 0 0
# 0 1 1 1 1 0
# 0 0 0 0 0 0
# 0 1 1 1 1 1
# 0 1 1 1 1 1
# 0 0 0 0 0 0

def test_solution():
    assert solution([
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0]
    ]) == 8

    assert solution([
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 9

    assert solution([
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 11

    assert solution([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 14

    assert solution([
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0]
    ]) == 13

    assert solution([
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]) == 7

    assert solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 11

    assert solution([
        [0, 0],
        [0, 0]
    ]) == 3

    assert solution([
        [0, 0],
        [0, 1]
    ]) == 3


test_solution()
