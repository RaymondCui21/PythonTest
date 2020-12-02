
def input_commands(filename):
    commands = []
    inputFile = open(filename, "r")
    for rawCommand in inputFile.readlines():
        if rawCommand.isspace():
            continue
        else:
            commands.append(rawCommand.strip().upper())
    inputFile.close()
    return commands


class Robot:
    def __init__(self, n, m, command):
        self.n = n
        self.m = m
        initposition = command.split()
        self.x = int(initposition[1])
        self.y = int(initposition[2])
        self.direction = initposition[3]
        self.directions = ('WEST', 'NORTH', 'EAST', 'SOUTH')
        self.expectx = self.x
        self.expecty = self.y

    def action(self, command):
        command = command.split()
        if command[0] == 'MOVE':
            if self.direction == 'WEST':
                self.expectx = self.expectx - 1
            elif self.direction == 'NORTH':
                self.expecty = self.expecty + 1
            elif self.direction == 'EAST':
                self.expectx = self.expectx + 1
            elif self.direction == 'SOUTH':
                self.expecty = self.expecty - 1
            else:
                pass
        elif command[0] == 'LEFT':
            self.direction = self.directions[self.directions.index(self.direction) - 1]
        elif command[0] == 'RIGHT':
            self.direction = self.directions[self.directions.index(self.direction) + 1]
        elif command[0] == 'PLACE' and command[1].isdecimal() and command[2].isdecimal() and (
                    command[3] in self.directions):
            self.x = command[1]
            self.y = command[2]
            self.direction = command[3]
        elif command[0] == 'REPORT':
            print("X: {} Y: {} Direction: {}".format(self.x, self.y, self.direction))
        else:
            pass

        if self.expectx in range(0, self.n) and self.expecty in range(0, self.m):
            self.x = self.expectx
            self.y = self.expecty
        else:
            pass


class Board:
    def __init__(self, n, m, commands):
        self.n = n
        self.m = m
        self.directions = ('WEST', 'NORTH', 'EAST', 'SOUTH')
        self.commands = commands

    def initrobot(self):
        result = -1
        for commandLine in self.commands:
            # print(commandLine)
            command = commandLine.split()
            if command[0] == 'PLACE' and command[1].isdecimal() and command[2].isdecimal() and (
                    command[3] in self.directions):
                if int(command[1]) in range(0, self.n) and int(command[2]) in range(0, self.m):
                    result = self.commands.index(commandLine)
                    break
            else:
                continue
        if result == -1:
            print('Did not find available Place commands.')
        else:
            pass
        return result


def main():
    # text file name is "testcommands.txt"
    commands = input_commands("testcommands.txt")
    # assume n and m are 10
    n = 10
    m = 10
    board = Board(n, m, commands)
    index = board.initrobot()
    if index != -1:
        robot = Robot(n, m, commands[index])
        if index+1 <= len(commands):
            for command in commands[index+1:]:
                robot.action(command)


if __name__ == "__main__":
    main()
