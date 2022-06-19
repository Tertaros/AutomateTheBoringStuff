#Chess board  rules
# All pieces must be on a valid space from '1a' to '8h'
# The pieces name must begin with either 'w' or 'b' followed by their full name 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
# A player can not have more than 16 pieces (so not more than 16 black or white)
# At most 8 pawns, 2 bishops, 2 rooks, 2 knights, 1 queen and 1 king

#Standard starting position topdown
examplechessBoard = {'8a':'brook', '8b':'bknight', '8c':'bbishop', '8d':'bqueen', '8e':'bking', '8f':'bbishop', '8g':'bknight', '8h':'brook',
                    '7a':'bpawn', '7b':'bpawn', '7c':'bpawn', '7d':'bpawn', '7e':'bpawn', '7f':'bpawn', '7g':'bpawn', '7h':'bpawn',
                    '2a':'wpawn', '2b':'wpawn', '2c':'wpawn', '2d':'wpawn', '2e':'wpawn', '2f':'wpawn', '2g':'wpawn', '2h':'wpawn',
                    '1a':'wrook', '1b':'wknight', '1c':'wbishop', '1d':'wqueen', '1e':'wking', '1f':'wbishop', '1g':'wknight', '1h':'wrook'}


def isValidChessBoard(chessBoard):
    if(len(chessBoard)>32):
        print(str(len(chessBoard))+ ' Invalid length, number of pieces can not exceed 32.')
        return False #There are more than 32 pieces,

    nWhitePieces = 0
    nBlackPieces = 0
    nWhitePawns = 0
    nBlackPawns = 0
    nWhiteRooks = 0
    nBlackRooks = 0
    nWhiteBishops = 0
    nBlackBishops = 0
    nWhiteKnights = 0
    nBlackKnights = 0
    nWhiteQueen = 0
    nBlackQueen = 0
    nWhiteKing = 0
    nBlackKing = 0

    boardColumns = ['a','b','c','d','e','f','g','h']
    for k,v in chessBoard.items():

        if((int(k[0]) not in range(1,9)) or k[1] not in boardColumns): #Check if valid row position
            print(k + ' invalid position.')
            return False

        if(v[0] == 'w'):  #Check if white piece
            nWhitePieces += 1
        elif(v[0] == 'b'): # Check if black piece
            nBlackPieces += 1
        else:
            print(v + ' is not valid value, needs to start with "b" or "w"')
            return False #Invalid value, inputs

        #Count each type of piece
        if(v == 'wpawn'):
            nWhitePawns += 1
            if(nWhitePawns > 8):
                print('Invalid number of white pawns')
                return False
        elif(v == 'bpawn'):
            nBlackPawns += 1
            if(nBlackPawns > 8):
                print('Invalid number of black pawns')
                return False
        elif(v == 'brook'):
            nBlackRooks += 1
            if(nBlackRooks > 2):
                print('Invalid number of black rooks')
                return False
        elif(v == 'wrook'):
            nWhiteRooks += 1
            if(nWhiteRooks > 2):
                print('Invalid number of white rooks')
                return False
        elif(v == 'bbishop'):
            nBlackBishops += 1
            if(nBlackBishops > 2):
                print('Invalid number of black bishops')
                return False
        elif(v == 'wbishop'):
            nWhiteBishops += 1
            if(nWhiteBishops > 2):
                print('Invalid number of white bishops')
                return False
        elif(v == 'bknight'):
            nBlackKnights += 1
            if(nBlackKnights > 2):
                print('Invalid number of black knights')
                return False
        elif(v == 'wknight'):
            nWhiteKnights += 1
            if(nWhiteKnights > 2):
                print('Invalid number of white knights')
                return False
        elif(v == 'bqueen'):
            nBlackQueen += 1
            if(nBlackQueen > 1):
                print('Invalid number of black queens')
                return False
        elif(v == 'wqueen'):
            nWhiteQueen += 1
            if(nWhiteQueen > 1):
                print('Invalid number of white queens')
                return False
        elif(v == 'bking'):
            nBlackKing += 1
            if(nBlackKing > 1):
                print('Invalid number of black kings')
                return False
        elif(v == 'wking'):
            nWhiteKing += 1
            if(nWhiteKing> 1):
                print('Invalid number of white kings')
                return False
        else:
            print(v + ' is not valid value.')
            return False

    return True

if(isValidChessBoard(examplechessBoard)):
    print('Valid chess board!')

