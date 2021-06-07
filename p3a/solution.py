import copy


class Node:
    def __init__(self, passable, x, y):
        self.passable = passable
        self.x = x
        self.y = y
        self.h = 1
        self.g = 0
        self.f = None
        self.parent = None


class Board:
    def __init__(self, map):
        self.map = map
        self.width = len(map[0])
        self.height = len(map)
        self.board = [[Node(map[y][x] == 0, x, y) for x in range(self.width)] for y in range(self.height)]
        self.last_node = self.board[self.height - 1][self.width - 1]
        self.first_node = self.board[0][0]
        self.first_node.h = abs(self.first_node.x - self.last_node.x) + abs(self.first_node.y - self.last_node.y)
        self.first_node.g = 1
        self.first_node.f = self.first_node.h + 1


def get_shortest_path(board):
    queue = []
    checked = []
    queue.append(board.first_node)
    while queue:
        current_node = queue.pop()
        checked.append(current_node)
        if current_node == board.last_node:
            break
        steps = get_adjacent_nodes(current_node, board)
        for step in steps:
            add_to_queue_flag = True
            if not step.passable:
                add_to_queue_flag = False
            else:
                for old in checked:
                    if old == step:
                        add_to_queue_flag = False
                for old in queue:
                    if old == step:
                        add_to_queue_flag = False
            if add_to_queue_flag:
                new = update(step, current_node, board.last_node)
                queue.append(new)
                queue.sort(key=get_f, reverse=True)
    return board.last_node.f


def get_f(node):
    return node.f


def update(n, cur, end):
    if n.g == 0:
        n.h = abs(n.x - end.x) + abs(n.y - end.y)
    # parent = cur
    n.g = cur.g + 1
    n.f = n.g + n.h
    return n


def get_adjacent_nodes(current_node, board):
    height, width = board.height, board.width
    map = board.board
    nodes = []
    if current_node.x < width - 1:
        nodes.append(map[current_node.y][current_node.x + 1])
    if current_node.x > 0:
        nodes.append(map[current_node.y][current_node.x - 1])
    if current_node.y < height - 1:
        nodes.append(map[current_node.y + 1][current_node.x])
    if current_node.y > 0:
        nodes.append(map[current_node.y - 1][current_node.x])
    return nodes


def solution(map):
    board = Board(map)
    blocks = [(y, x) for x in range(board.width) for y in range(board.height) if map[y][x] == 1]
    if blocks:
        shortest_path = 2 ** 32 - 1
        # Here, we need to replace each block and get list of shortest paths
        for (y, x) in blocks:
            temp_board = copy.deepcopy(board)
            temp_board.board[y][x].passable = True
            shortest_for_board_state = get_shortest_path(temp_board)
            if shortest_for_board_state is not None and shortest_for_board_state < shortest_path:
                shortest_path = shortest_for_board_state
    else:
        shortest_path = get_shortest_path(board)
    return shortest_path


print(solution([
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0]
]))  # 8

print(solution([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]
]))  # 9

print(solution([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]
]))  # 11

print(solution([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]
]))  # 14

print(solution([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0]
]))  # 13

print(solution([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]))  # 7

print(solution([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]))  # 11

print(solution([
    [0, 0],
    [0, 0]
]))  # 3

print(solution([
    [0, 0],
    [0, 1]
]))  # 3
