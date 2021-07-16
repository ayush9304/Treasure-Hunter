class Queue:
    def __init__(self):
        self.list = []
        self.front = 0
        self.last = -1

    def add(self, node):
        self.list.append(node)
        self.last = self.last + 1

    def remove(self):
        if self.front > self.last:
            raise Exception("Underflow!")
        else:
            self.front = self.front + 1
            return self.list[self.front-1]

    def isEmpty(self):
        if self.front > self.last:
            return True
        else:
            return False


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node:
    def __init__(self, coordinates, previous):
        self.state = coordinates
        self.previous = previous

class Maze:
    matrix = []
    visited = []
    row = 0
    column = 0
    start = Coordinate(-1, -1)
    goal = Coordinate(-1, -1)

    def __init__(self, matrix, row, column):
        self.matrix = matrix
        self.visited = matrix
        self.row = row
        self.column = column

    def load(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.matrix[i][j] == 'S':
                    self.start.x = j
                    self.start.y = i
                if self.matrix[i][j] == 'D':
                    self.goal.x = j
                    self.goal.y = i
                if self.matrix[i][j] == '1':
                    self.visited[i][j] = '2'
                else:
                    self.visited[i][j] = '0'

    def checkNeighbour(self, state, dir):
        var = Coordinate(-1, -1)
        if dir == 0:
            if state.x-1 >= 0:
                if self.visited[state.y][state.x-1] == '0':
                    var.x = state.x-1
                    var.y = state.y

        if dir == 1:
            if state.x+1 < self.column:
                if self.visited[state.y][state.x+1] == '0':
                    var.x = state.x+1
                    var.y = state.y

        if dir == 2:
            if state.y-1 >= 0:
                if self.visited[state.y-1][state.x] == '0':
                    var.x = state.x
                    var.y = state.y-1

        if dir == 3:
            if state.y+1 < self.row:
                if self.visited[state.y+1][state.x] == '0':
                    var.x = state.x
                    var.y = state.y+1

        return var


def bfs(matrix, row, column):

    queue = Queue()
    path = []
    maze = Maze(matrix, row, column)
    maze.load()
    start = Node(maze.start, None)
    goal = Node(Coordinate(-1, -1), None)
    queue.add(start)
    maze.visited[maze.start.y][maze.start.x] = '1'

    while not queue.isEmpty():
        current = queue.remove()
        for i in range(4):
            neighbour = maze.checkNeighbour(current.state, i)
            if not (neighbour.x == -1) and not (neighbour.y == -1):
                temp = Node(neighbour, queue.front-1)
                queue.add(temp)
                maze.visited[neighbour.y][neighbour.x] = '1'
                if maze.goal.x == neighbour.x and maze.goal.y == neighbour.y:
                    goal = temp
                    break

    if goal.state.x == -1 or goal.state.y == -1:
        raise Exception("No solution found!")
    else:
        current = goal
        while current.previous is not None:
            path.append((current.state.x, current.state.y))
            maze.matrix[current.state.y][current.state.x] = 'P'
            current = queue.list[current.previous]
        path.append((maze.start.x, maze.start.y))
        maze.matrix[maze.start.y][maze.start.x] = 'S'
        maze.matrix[maze.goal.y][maze.goal.x] = 'D'

    return maze.matrix, reversed(path)



row = 5
column = 5
maze = [
    ['S', '1', '0', '0', '0'],
    ['0', '1', '0', '1', '0'],
    ['0', '1', '0', '1', '0'],
    ['0', '0', '0', '1', '0'],
    ['1', '0', '0', '1', 'D']
]

matrix, path = bfs(maze, row, column)

for i in range(row):
    print(matrix[i])

print("\n")

for elem in path:
    print(elem)
