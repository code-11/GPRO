#!/usr/bin/env python
# 

#
# Game Programming, Level 2 Project
#
# TIC-TAC-TOE 4
#
# A simple input_strategy game, an extension of the standard 3x3 tic-tac-toe
#

import sys, cProfile
from graphics import *
size = 200
minDict = {}
maxDict = {}

WIN_SEQUENCES = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
    [0,4,8,12],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [0,5,10,15],
    [3,6,9,12]
]

MARK_VALUE = {
    'O': 1,
    '.': 0,
    'X': 10
}

def fail (msg):
    raise StandardError(msg)


def create_board (input_str):
    # FIX ME
    #
    # Take a description of the board as input and create the board
    #  in your representation
    #
    # The input_string description is a sequence of 16 characters,
    #   each either X or O, or . to represent a free space
    # It is allowed to pass in a input_string describing a board
    #   that would never arise in legal play starting from an empty

    return list(input_str.upper())

    #   board
    # return None

def has_mark (board,x,y):
    # FIX ME
    #
    # Take a board representation and checks if there's a mark at
    #    position x, y (each between 1 and 4)
    # Return 'X' or 'O' if there is a mark
    # Return False if there is not
    return None

def has_win_old (board):
    # FIX ME
    # 
    # Check if a board is a win for X or for O.
    # Return 'X' if it is a win for X, 'O' if it is a win for O,
    # and False otherwise
    for positions in WIN_SEQUENCES:
        s = sum(MARK_VALUE[board[pos]] for pos in positions)
        if s == 4:
            return 'O'
        if s == 40:
            return 'X'
    return False

def has_win (board):
    b=board

    if b[0] != '.':
        if (b[0] == b[1] and b[0]==b[2] and b[0]==b[3]):
            return b[0]
    if b[4] != '.':
        if (b[4] == b[5] and b[4]==b[6] and b[4]==b[7]):
            return b[4]
    if b[8] != '.':
        if (b[8] == b[9] and b[8]==b[10] and b[8]==b[11]):
            return b[8]
    if b[12] != '.':
        if (b[12] == b[13] and b[12]==b[14] and b[12]==b[15]):
            return b[12]
    if b[0] != '.':
        if (b[0] == b[4] and b[0]==b[8] and b[0]==b[12]):
            return b[0]
    if b[1] != '.':
        if (b[1] == b[5] and b[1]==b[9] and b[1]==b[13]):
            return b[1]
    if b[2] != '.':
        if (b[2] == b[6] and b[2]==b[10] and b[2]==b[14]):
            return b[2]
    if b[3] != '.':
        if (b[3] == b[7] and b[3]==b[11] and b[3]==b[15]):
            return b[3]
    if b[0] != '.':
        if (b[0] == b[5] and b[0]==b[10] and b[0]==b[15]):
            return b[0]
    if b[3] != '.':
        if (b[3] == b[6] and b[3]==b[9] and b[3]==b[12]):
            return b[3]
    return False
    

def done (board):
    return (has_win(board) or not [ e for e in board if (e == '.')])
    # FIX ME
    #
    # Check if the board is done, either because it is a win or a draw
    # return True

def utility (board,player):
    if has_win(board) == player:
        return 1
    elif has_win(board) == other(player):
        return -1
    elif has_win(board) == False:
        return 0

def possible_moves (board):
    return [i for (i,e) in enumerate(board) if e == '.']

def draw_board(win, brd):
    # size = 200
    blank = Rectangle(Point(0,0), Point(size+10,size+10))
    blank.setFill("white")
    blank.draw(win)

    line1 = Line(Point(0,size/4),Point(size,size/4))
    line2 = Line(Point(0,size/4*2),Point(size,size/4*2))
    line3 = Line(Point(0,size/4*3),Point(size,size/4*3))
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4 = Line(Point(size/4,0),Point(size/4,size))
    line5 = Line(Point(size/4*2,0),Point(size/4*2,size))
    line6 = Line(Point(size/4*3,0),Point(size/4*3,size))
    line4.draw(win)
    line5.draw(win)
    line6.draw(win)

    for i in xrange(16):
        # print brd[i]
        xPos = (i%4+1)*50-25
        yPos = (i/4+1)*50-25
        text = Text(Point(xPos,yPos),brd[i])
        text.draw(win)

def print_board (board):
    # FIX ME
    #
    # Display a board on the console
    for i in range(0,4):
        print '  ',board[i*4],board[i*4+1],board[i*4+2],board[i*4+3] 
    # return None

def read_player_input (board, player, win):
    valid = [ i for (i,e) in enumerate(board) if e == '.']
    while True:
        # move = raw_input('Position (0-15)? ')
        playerMove = win.getMouse()
        xMove = playerMove.getX()/(size/4)
        yMove = playerMove.getY()/(size/4)
        move = yMove*4 + xMove
        # if move == 'q':
        #     exit(0)
        if int(move) in valid:
            return int(move)
    # FIX ME
    #
    # Read player input when playing as 'player' (either 'X' or 'O')
    # Return a move (a tuple (x,y) with each position between 1 and 4)
    # return None

def make_move (board,move,player):
    # FIX ME
    #
    # Returns a board where 'move' has been performed on 'board' by 
    #    'player'
    # Change can be done in place in 'board' or a new copy created

    # returns a copy of the board with the move recorded
    # print board, move, player
    new_board = board[:]
    new_board[move] = player
    return new_board
    # return None

#make the board into a string!!
def min_value (board,player):
    boardString = ''.join(board)
    if done(board):
        return utility(board,player)
    elif boardString in minDict:
        return minDict[boardString]
    else:
        successor_moves = []
        for i in possible_moves(board):
            new_board = make_move(board, i, other(player))
            successor_moves.append(max_value(new_board,player))
        minDict[boardString] = min(successor_moves)
        # print "min: ", min(successor_moves)
        return min(successor_moves)

def max_value (board,player):
    # print "computer_move player: ", player
    boardString = ''.join(board)
    if done(board):
        return utility(board,player)
    elif boardString in maxDict:
        return maxDict[boardString]
    else:
        successor_moves = []
        for i in possible_moves(board):
            new_board = make_move(board, i, player)
            successor_moves.append(min_value(new_board,player))
        maxDict[boardString] = max(successor_moves)
        # print "max: ", max(successor_moves)
        return max(successor_moves)

def computer_move (board,player,win):
    print "computer_move player: ", player
    scores = []
    possible_moves_array = possible_moves(board)
    # print "possible_moves_array: ", possible_moves_array
    for i in range(len(possible_moves_array)):
        # new_board = make_move(board, possible_moves_array[i], 'O')
        new_board = make_move(board, possible_moves_array[i], player)
        scores.append(min_value(new_board,player))
    print "Scores: ", scores
    return possible_moves_array[scores.index(max(scores))]
    # FIX ME
    #
    # Select a move for the computer, when playing as 'player' (either 
    #   'X' or 'O')
    # Return the selected move (a tuple (x,y) with each position between 
    #   1 and 4)

    # return 15
    # return None


def other (player):
    if player == 'X':
        return 'O'
    return 'X'


def run (input_str,player,playX,playO): 

    board = create_board(input_str)

    win = GraphWin("Rush Board", size, size)
    draw_board(win, board)

    print_board(board)

    while not done(board):
        print "Player: ", player
        if player == 'X':
            move = playX(board,player,win)
        elif player == 'O':
            move = playO(board,player,win)
        else:
            fail('Unrecognized player '+player)
        board = make_move(board,move,player)
        # print_board(board)
        draw_board(win,board)
        player = other(player)

    winner = has_win(board)
    if winner:
        print winner,'wins!'
        win.getMouse()
    else:
        print 'Draw'
        win.getMouse()
        
def main ():
    run('.' * 16, 'X', read_player_input, computer_move)


PLAYER_MAP = {
    'human': read_player_input,
    'computer': computer_move
}

if __name__ == '__main__':
  # print sys.argv
  try:
      input_str = sys.argv[1] if len(sys.argv)>1 else '.' * 16
      player = sys.argv[2].upper() if len(sys.argv)>3 else 'X'
      playX = PLAYER_MAP[sys.argv[3]] if len(sys.argv)>3 else read_player_input
      playO = PLAYER_MAP[sys.argv[4]] if len(sys.argv)>4 else computer_move
  except:
    print 'Usage: %s [starting board] [X|O] [human|computer] [human|computer]' % (sys.argv[0])
    exit(1)
  cProfile.run('run(input_str,player,playX,playO)')
