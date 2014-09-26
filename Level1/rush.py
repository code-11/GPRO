#!/usr/bin/env python
import sys

#
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#
# Assignment completed by Alex Adkins and Brendan Ritter

class car:
    def __init__(self, name, initPos, length, up):
        self.name = name        #name of car
        self.up = up

        #pos = list of tuples of all filled spaces
        self.pos = []
        self.pos.append(initPos)
        for i in range(length - 1):
            if self.up:
                nextPos = (initPos[0], initPos[1] + 1)
            else:
                nextPos = (initPos[0] + 1, initPos[1])
            self.pos.append(nextPos)
            initPos = nextPos

    #function to check if point is colliding with car
    def collide(self, point):
        return point in self.pos


# fail somewhat gracefully
def fail (msg):
    raise StandardError(msg)


GRID_SIZE = 6


def outOfBound(car, carDirection, carDistance):
    boundAdder = {"U": (0,-carDistance), "D": (0, carDistance), "R": (carDistance, 0), "L": (-carDistance, 0)}
    boundaryValid = True
    for point in car.pos:
        boundary = tuple(map(sum, zip(point, boundAdder[carDirection])))
        if (boundary[0] not in range(1,7)) or (boundary[1] not in range(1,7)):
            boundaryValid = False

    return boundaryValid

def existing_piece_check(brd, move):
    for car in brd:
        if car.name == move[0]:
            return car
    return None

def direction_check(brd, car, move):
    validDirections = [("U", True),("D",True),("L",False),("R",False)]
    return (move[1], car.up) in validDirections

def slide_check(brd, car, move):
    noCollision = True
    for i in range(move[2] + 1):
        adder = {"U": (0,-i), "D": (0, i), "R": (i, 0), "L": (-i, 0)}
        for point in car.pos:
            intermediaryPt = tuple(map(sum, zip(point, adder[move[1]])))
            for otherCar in brd:
                if (otherCar.collide(intermediaryPt)) and (otherCar.name != car.name):
                    noCollision = False
    return noCollision


def validate_move (brd,move):
    validMove = False
    car = existing_piece_check(brd, move)
    if car != None:
        directionValid = direction_check(brd, car, move)
        inBounds = outOfBound(car, move[1], move[2])
        slideValid = slide_check(brd, car, move)
        validMove = directionValid and inBounds and slideValid
    else:
        validMove = False
        print "Not a valid piece."
    return validMove


def read_player_input (brd):
    var = raw_input("Enter car name, direction, and slide distance (e.g. ou2 or cr1)\n")
    carName = var[0].upper()
    carDirection = var[1].upper()
    try:
        carDistance = int(var[2])
    except:
        print "Not an integer."
    move = (carName, carDirection, carDistance)
    if validate_move(brd, move):
        return move
    else:
        print "Not a valid move."


def update_board (brd,move):
    # move is lr3
    if move != None:
        car = existing_piece_check(brd, move)
        i = move[2]
        adder = {"U": (0,-i), "D": (0, i), "R": (i, 0), "L": (-i, 0)}
        newPosition = []

        for position in car.pos:
            newTuple = tuple(map(sum, zip(position, adder[move[1]])))
            newPosition.append(newTuple)

        car.pos = newPosition
    return brd


def print_board (brd):
    for y in range(1,7):
        for x in range(1,7):
            carThere = False
            for car in brd:
                if car.collide((x,y)):
                    carThere = True
                    sys.stdout.write(" " + car.name + " ")
            if not carThere:
                sys.stdout.write(" . ")
        if y == 3:
            sys.stdout.write(" ==>")
        sys.stdout.write("\n")

    
def done (brd):
    if ((6,3) in brd[0].pos) and ((5,3) in brd[0].pos):
        return True
    else:
        return False


# initial board:
# Board positions (1-6,1-6), directions 'r' or 'd'
#
# X @ (2,3) r
# A @ (2,4) r
# B @ (2,5) d
# C @ (3,6) r
# O @ (4,3) d
# P @ (6,4) d


def create_initial_level ():
    # def __init__(self, name, initPos, length, up):
    # true = up/down, false = right/left

    X = car("X", (2,3), 2, False)
    A = car("A", (2,4), 2, False)
    B = car("B", (2,5), 2, True)
    C = car("C", (3,6), 2, False)
    O = car("O", (4,3), 3, True)
    P = car("P", (6,4), 3, True)
    carList = [X, A, B, C, O, P]
    return carList


def main ():
    brd = create_initial_level()

    print_board(brd)

    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'


def main_with_initial (desc):
    carList = []
    carLengths = {"X": 2, "A": 2, "B": 2, "C": 2, "D": 2, "E": 2, "F": 2, 
    "G": 2, "H": 2, "I": 2, "J": 2, "K": 2, 
    "O": 3, "P": 3, "Q": 3, "R": 3}
    for i in range(len(desc)/4):
        j = 4 * i
        # We know there is more checking we could do, but it wasn't assigned.
        carName = desc[j].upper()
        carX = int(desc[j+1])
        carY = int(desc[j+2])

        if desc[j+3] == "r" or desc[j+3] == "l":
            carDir = False
        elif desc[j+3] == "d" or desc[j+3] == "u":
            carDir = True
        else:
            print "A piece does not have a valid direction."
        
        carList.append(car(carName, (carX, carY), carLengths[carName], carDir))

    brd = carList

    print_board(brd)

    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'


# testString = "X23rA24rB25dC36rO43dP64d"
        

if __name__ == '__main__':
    # main()
    if len(sys.argv) > 1:
        main_with_initial(sys.argv[1])
    else: 
        main()
