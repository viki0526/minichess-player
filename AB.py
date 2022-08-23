
### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove

class Piece:
    @staticmethod
    def positionsThreatened(position, gameboard) :
        return [position]
        

def helper(gameboard, position, newPos, states, piece, player):
        newBoard = gameboard.copy()
        if((newPos not in gameboard) or gameboard[newPos][1] != player):
            newBoard.pop(position)
            newBoard[newPos] = piece
            states.append((position, newPos, newBoard))

class King(Piece):

    @staticmethod
    def generateStates(position, gameboard, player):
        row = position[0]
        col = position[1]
        states = []
        piece = gameboard[position]
        if(row != 0):
            helper(gameboard, position, (row - 1, col), states, piece, player)
        if(col != 0):
            helper(gameboard, position, (row, col - 1), states, piece, player)
        if(row != 0 and col != 0):
            helper(gameboard, position, (row - 1, col - 1), states, piece, player)
        if(row < 4):
            helper(gameboard, position, (row + 1, col), states, piece, player)
        if(col < 4):
            helper(gameboard, position, (row, col + 1), states, piece, player)
        if(row < 4 and col < 4):
            helper(gameboard, position, (row + 1, col + 1), states, piece, player)
        if(row < 4 and col != 0):
            helper(gameboard, position, (row + 1, col - 1), states, piece, player)
        if(row != 0 and col < 4):
            helper(gameboard, position, (row - 1, col + 1), states, piece, player)
        
        return states

class Queen(Piece):
    @staticmethod
    def generateStates(position, gameboard, player):
        row = position[0]
        col = position[1]
        states = []
        piece = gameboard[position]

        i = col + 1
        while i < 5:
            if (row, i) in gameboard:
                helper(gameboard, position, (row, i), states, piece, player)
                break
            helper(gameboard, position, (row, i), states, piece, player)
            i += 1
        i = col - 1
        while i >= 0:
            if (row, i) in gameboard:
                helper(gameboard, position, (row, i), states, piece, player)
                break
            helper(gameboard, position, (row, i), states, piece, player)
            i -= 1
        i = row + 1
        while i < 5:
            if (i, col) in gameboard:
                helper(gameboard, position, (i, col), states, piece, player)
                break
            helper(gameboard, position, (i, col), states, piece, player)
            i += 1
        i = row - 1
        while i >= 0:
            if (i, col) in gameboard:
                helper(gameboard, position, (i, col), states, piece, player)
                break
            helper(gameboard, position, (i, col), states, piece, player)
            i -= 1

        i = row + 1
        j = col + 1
        while i < 5 and j < 5:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i += 1
            j += 1
        i = row + 1
        j = col - 1
        while i < 5 and j >= 0:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i += 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < 5:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i -= 1
            j += 1
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i -= 1
            j -= 1
        
        return states

class Bishop(Piece):
    @staticmethod
    def generateStates(position, gameboard, player):
        row = position[0]
        col = position[1]
        states = []
        piece = gameboard[position]

        i = row + 1
        j = col + 1
        while i < 5 and j < 5:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i += 1
            j += 1
        i = row + 1
        j = col - 1
        while i < 5 and j >= 0:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i += 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < 5:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i -= 1
            j += 1
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if (i, j) in gameboard:
                helper(gameboard, position, (i, j), states, piece, player)
                break
            helper(gameboard, position, (i, j), states, piece, player)
            i -= 1
            j -= 1
        
        return states

class Rook(Piece):
    @staticmethod
    def generateStates(position, gameboard, player):
        row = position[0]
        col = position[1]
        states = []
        piece = gameboard[position]

        i = col + 1
        while i < 5:
            if (row, i) in gameboard:
                helper(gameboard, position, (row, i), states, piece, player)
                break
            helper(gameboard, position, (row, i), states, piece, player)
            i += 1
        i = col - 1
        while i >= 0:
            if (row, i) in gameboard:
                helper(gameboard, position, (row, i), states, piece, player)
                break
            helper(gameboard, position, (row, i), states, piece, player)
            i -= 1
        i = row + 1
        while i < 5:
            if (i, col) in gameboard:
                helper(gameboard, position, (i, col), states, piece, player)
                break
            helper(gameboard, position, (i, col), states, piece, player)
            i += 1
        i = row - 1
        while i >= 0:
            if (i, col) in gameboard:
                helper(gameboard, position, (i, col), states, piece, player)
                break
            helper(gameboard, position, (i, col), states, piece, player)
            i -= 1

        return states

class Knight(Piece):
    @staticmethod
    def generateStates(position, gameboard, player):
        row = position[0]
        col = position[1]
        states = []
        piece = gameboard[position]

        if row + 2 < 5 and col + 1 < 5:
            helper(gameboard, position, (row + 2, col + 1), states, piece, player)
        if row + 1 < 5 and col + 2 < 5:
            helper(gameboard, position, (row + 1, col + 2), states, piece, player)
        if row + 2 < 5 and col - 1 >= 0:
            helper(gameboard, position, (row + 2, col - 1), states, piece, player)
        if row + 1 < 5 and col - 2 >= 0:
            helper(gameboard, position, (row + 1, col - 2), states, piece, player)
        if row - 2 >= 0 and col + 1 < 5:
            helper(gameboard, position, (row - 2, col + 1), states, piece, player)
        if row - 1 >= 0 and col + 2 < 5:
            helper(gameboard, position, (row - 1, col + 2), states, piece, player)
        if row - 2 >= 0 and col - 1 >= 0:
            helper(gameboard, position, (row - 2, col - 1), states, piece, player)
        if row - 1 >= 0 and col - 2 >= 0:
            helper(gameboard, position, (row - 1, col - 2), states, piece, player)

        return states
        
class Pawn(Piece):

    @staticmethod
    def generateStates(position, gameboard, player):
        row = position[0]
        col = position[1]
        states = []
        piece = gameboard[position]

        if(player == "White"):
            if(row < 4) and (row + 1, col) not in gameboard:
                helper(gameboard, position, (row + 1, col), states, piece, player)
            if(row < 4 and col < 4) and (row + 1, col + 1) in gameboard:
                helper(gameboard, position, (row + 1, col + 1), states, piece, player)
            if(row < 4 and col != 0) and (row + 1, col - 1) in gameboard:
                helper(gameboard, position, (row + 1, col - 1), states, piece, player)
        if(player == "Black"):
            if(row != 0) and (row - 1, col) not in gameboard:
                helper(gameboard, position, (row - 1, col), states, piece, player)
            if(row != 0 and col < 4) and (row - 1, col + 1) in gameboard:
                helper(gameboard, position, (row - 1, col + 1), states, piece, player)
            if(row != 0 and col != 0) and (row - 1, col - 1) in gameboard:
                helper(gameboard, position, (row - 1, col - 1), states, piece, player)
        
        return states

def sortKey(state):
    return utility(state[2])

def utility(board):
    res = 0
    for pos in board:
        piece = board[pos]
        if(piece[1] == "White"):
            if(piece[0] == "King"):
                res += 20
            if(piece[0] == "Queen"):
                res += 9
            if(piece[0] == "Bishop"):
                res += 3
            if(piece[0] == "Rook"):
                res += 5
            if(piece[0] == "Knight"):
                res += 3
            if(piece[0] == "Pawn"):
                res += 1
        if(piece[1] == "Black"):
            if(piece[0] == "King"):
                res -= 20
            if(piece[0] == "Queen"):
                res -= 9
            if(piece[0] == "Bishop"):
                res -= 3
            if(piece[0] == "Rook"):
                res -= 5
            if(piece[0] == "Knight"):
                res -= 3
            if(piece[0] == "Pawn"):
                res -= 1
    return res

x = None
#Implement your minimax with alpha-beta pruning algorithm here.
def ab(board, depth, alpha, beta, isWhite, parent, utilities):
    if depth == 0:
        global x
        x = (board[0], board[1])
        return utility(board[2])
    if isWhite:
        states = []
        gameboard = board[2]
        for pos in gameboard:
            piece = gameboard[pos]
            if(piece[1] == "White"):
                if(piece[0] == "King"):
                    states.extend(King.generateStates(pos, gameboard, "White"))
                if(piece[0] == "Queen"):
                    states.extend(Queen.generateStates(pos, gameboard, "White"))
                if(piece[0] == "Bishop"):
                    states.extend(Bishop.generateStates(pos, gameboard, "White"))
                if(piece[0] == "Rook"):
                    states.extend(Rook.generateStates(pos, gameboard, "White"))
                if(piece[0] == "Knight"):
                    states.extend(Knight.generateStates(pos, gameboard, "White"))
                if(piece[0] == "Pawn"):
                    states.extend(Pawn.generateStates(pos, gameboard, "White"))
                states.sort(key=sortKey, reverse=True)
        maxUtility = -9999
        for child in states:
            parent[(child[0], child[1])] = (board[0], board[1])
            curr = ab(child, depth - 1, alpha, beta, False, parent, utilities)
            if depth == 4:
                utilities[(child[0], child[1])] = curr
            maxUtility = max(curr, maxUtility)
            alpha = max(maxUtility, alpha)
            if beta <= alpha:
                break
        return maxUtility

    else:
        states = []
        gameboard = board[2]
        for pos in gameboard:
            piece = gameboard[pos]
            if(piece[1] == "Black"):
                if(piece[0] == "King"):
                    states.extend(King.generateStates(pos, gameboard, "Black"))
                if(piece[0] == "Queen"):
                    states.extend(Queen.generateStates(pos, gameboard, "Black"))
                if(piece[0] == "Bishop"):
                    states.extend(Bishop.generateStates(pos, gameboard, "Black"))
                if(piece[0] == "Rook"):
                    states.extend(Rook.generateStates(pos, gameboard, "Black"))
                if(piece[0] == "Knight"):
                    states.extend(Knight.generateStates(pos, gameboard, "Black"))
                if(piece[0] == "Pawn"):
                    states.extend(Pawn.generateStates(pos, gameboard, "Black"))
                states.sort(key= sortKey)
        minUtility = 9999
        for child in states:
            parent[(child[0], child[1])] = (board[0], board[1])
            curr = ab(child, depth - 1, alpha, beta, True, parent, utilities)
            minUtility = min(curr, minUtility)
            beta = min(minUtility, beta)
            if beta <= alpha:
                break
        return minUtility


### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    board = {}
    for pos in gameboard:
        board[parseCoord(pos)] = gameboard[pos]

    startState = (None, None, board)
    parent = {}
    utilities = {}
    ab(startState, 4, -9999, 9999, True, parent, utilities)
    
    maxU = -9999
    move = None
    for x in utilities:
        if utilities[x] > maxU:
            move = x
            maxU = utilities[x]
    
    return (unparseCoord(move[0]), unparseCoord(move[1])) #Format to be returned (('a', 0), ('b', 3))

def parseCoord(coord):
    return (coord[1], ord(coord[0]) - ord('a'))

def unparseCoord(coord):
    return (chr(coord[1] + ord('a')), coord[0])
