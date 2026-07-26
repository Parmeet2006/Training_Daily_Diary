black_space='■'
black_pawn='♟'
black_rook='♜'
black_knight='♞'
black_bishop='♝'
black_queen='♛'
black_king='♚'
white_space='□'
white_pawn='♙'
white_rook='♖'
white_knight='♘'
white_bishop='♗'
white_queen='♕'
white_king='♔'

for outer in range(8):
    for index in range(8):
        if (outer+index)%2==0:
            if (outer==0)and(index==4):
                print(white_queen,end=' ')
                continue
            if (outer==7)and(index==3):
                print(black_queen,end=' ')
                continue
            if (outer==0)and(index==2):
                print(white_bishop,end=' ')
                continue
            if (outer==7)and(index==5):
                print(black_bishop,end=' ')
                continue
            if (outer==0)and(index==6):
                print(white_knight,end=' ')
                continue
            if (outer==7)and(index==1):
                print(black_knight,end=' ')
                continue
            if (outer==0)and(index==0):
                print(white_rook,end=' ')
                continue
            if (outer==7)and(index==7):
                print(black_rook,end=' ')
                continue 
            if outer==1:
                print(white_pawn,end=' ')
                continue
            elif outer==6:
                print(black_pawn,end=" ")
                continue
            print(white_space,end=' ')
        else:
            if (outer==0)and(index==3):
                print(white_king,end=' ')
                continue
            if (outer==7)and(index==4):
                print(black_king,end=' ')
                continue
            if (outer==0)and(index==5):
                print(white_bishop,end=' ')
                continue
            if (outer==7)and(index==2):
                print(black_bishop,end=' ')
                continue
            if (outer==0)and(index==1):
                print(white_knight,end=' ')
                continue
            if (outer==7)and(index==6):
                print(black_knight,end=' ')
                continue
            if (outer==0)and(index==7):
                print(white_rook,end=' ')
                continue
            if (outer==7)and(index==0):
                print(black_rook,end=' ')
                continue
            if outer==1:
                print(white_pawn,end=' ')
                continue
            elif outer==6:
                print(black_pawn,end=" ")
                continue
            print(black_space,end=' ')
    print()
    
