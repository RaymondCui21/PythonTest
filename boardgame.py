class Robot:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.x = -1
        self.y = -1
        self.direction = ''
        self.directions = ('WEST', 'NORTH', 'EAST', 'SOUTH')

    def isValidPosition(self, x, y):
        return ( 0 <= x <= self.n) and ( 0< y <= self.m)

    def action(self, command):
        if command[0] == 'MOVE':
            self.move()
        elif command[0] == 'LEFT':
            self.direction = self.directions[self.directions.index(self.direction) - 1]
        elif command[0] == 'RIGHT':
            self.direction = self.directions[self.directions.index(self.direction) + 1]
        elif command[0] == 'PLACE':
            self.place(command)
        elif command[0] == 'REPORT':
            print("X: {} Y: {} Direction: {}".format(self.x, self.y, self.direction))

    def move(self):
        expectx = self.x
        expecty = self.y
        if self.direction == 'WEST':
            expectx = expectx -1
        elif self.direction == 'NORTH':
            expecty = expecty + 1
        elif self.direction == 'EAST':
            expectx = expectx + 1
        elif self.direction == 'SOUTH':
            expecty = expecty - 1
        if self.isValidPosition(expectx, expecty):
            self.x = expectx
            self.y = expecty

    def place(self, command):
        if self.isValidPlace(command):
            self.x = int(command[1])
            self.y = int(command[2])
            self.direction = command[3]

    def isValidPlace(self, command):
        if command[1].isdecimal() and command[2].isdecimal() and (command[3] in self.directions):
            if (int(command[1]) <= self.n) and (int(command[2]) <= self.m):
                return True


def main():
    n = m = 10  # assume n and m are 5
    robot = Robot(n, m)
    filename = "testcommands.txt"  # text file name is "testcommands.txt"
    inputFile = open(filename, "r")
    command = []
    for rawCommand in inputFile.readlines():
        if not rawCommand.isspace():
            command = rawCommand.strip().upper().split()
            if robot.direction == '' and (command[0] == 'PLACE'):
                robot.place(command)
            elif robot.direction != '':
                robot.action(command)
            else:
                continue
        else:
            continue
    inputFile.close()


if __name__ == "__main__":
    main()
