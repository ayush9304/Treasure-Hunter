import random

class Maze:
    def __init__(self, width, height):

        self.width = width // 2 * 2 + 1
        self.height = height // 2 * 2 + 1
        self.start = [-1, -1]
        self.goal = [-1, -1]
        self.quad = random.choice(range(4))
        if self.quad == 0:
            self.start = [width-1, 0]
            self.goal = [width, 0]
        if self.quad == 1:
            self.start = [0, 0]
            self.goal = [0, 0]
        if self.quad == 2:
            self.start = [0, height-1]
            self.goal = [0, height]
        if self.quad == 3:
            self.start = [width-1, height-1]
            self.goal = [width, height]

        # this creates a 2d-array for your maze data (False: path, True: wall)
        self.cells = [
                      [True for x in range(self.width)]
                      for y in range(self.height)
                     ]
        self.create_maze(self.start[0], self.start[1])

    def set_path(self, x, y):
        self.cells[y][x] = False

    def set_wall(self, x, y):
        self.cells[y][x] = True

    # a function to return if the current cell is a wall,
    #  and if the cell is within the maze bounds
    def is_wall(self, x, y):
        # checks if the coordinates are within the maze grid
        if 0 <= x < self.width and 0 <= y < self.height:
            # if they are, then we can check if the cell is a wall
            return self.cells[y][x]
        # if the coordinates are not within the maze bounds, we don't want to go there
        else:
            return False

    def create_maze(self, x, y):
        # set the current cell to a path, so that we don't return here later
        self.set_path(x, y)
        # we create a list of directions (in a random order) we can try
        all_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        random.shuffle(all_directions)

        # we keep trying the next direction in the list, until we have no directions left
        while len(all_directions) > 0:

            # we remove and return the last item in our directions list
            direction_to_try = all_directions.pop()

            # calculate the new node's coordinates using our random direction.
            # we *2 as we are moving two cells in each direction to the next node
            node_x = x + (direction_to_try[0] * 2)
            node_y = y + (direction_to_try[1] * 2)

            # check if the test node is a wall (eg it hasn't been visited)
            if self.is_wall(node_x, node_y):
                # success code: we have found a path

                # set our linking cell (between the two nodes we're moving from/to) to a path
                link_cell_x = x + direction_to_try[0]
                link_cell_y = y + direction_to_try[1]

                if self.quad == 0:
                    if ((self.width - self.goal[0]) + self.goal[1]) < ((self.width - link_cell_x) + link_cell_y):
                        self.goal[0] = link_cell_x
                        self.goal[1] = link_cell_y
                if self.quad == 1:
                    if (self.goal[0] + self.goal[1]) < (link_cell_x + link_cell_y):
                        self.goal[0] = link_cell_x
                        self.goal[1] = link_cell_y
                if self.quad == 2:
                    if (self.goal[0] + (self.height - self.goal[1])) < (link_cell_x + (self.height - link_cell_y)):
                        self.goal[0] = link_cell_x
                        self.goal[1] = link_cell_y
                if self.quad == 3:
                    if (self.goal[0] + self.goal[1]) > (link_cell_x + link_cell_y):
                        self.goal[0] = link_cell_x
                        self.goal[1] = link_cell_y

                self.set_path(link_cell_x, link_cell_y)

                # "move" to our new node. remember we are calling the function every
                #  time we move, so we call it again but with the updated x and y coordinates
                self.create_maze(node_x, node_y)
        return

    def matrix(self):
        matrix = [['1'] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x]:
                    matrix[y][x] = '1'
                else:
                    matrix[y][x] = '0'

        matrix[self.goal[1]][self.goal[0]] = "D"
        matrix[self.start[1]][self.start[0]] = "S"

        return matrix

    def __str__(self):
        string = ""
        conv = {
            True: "1",
            False: "0"
        }
        for y in range(self.height):
            for x in range(self.width):
                if x == self.goal[0] and y == self.goal[1]:
                    string += "D"
                elif x == self.start[0] and y == self.start[1]:
                    string += "S"
                else:
                    string += conv[self.cells[y][x]]
            string += "\n"
        return string