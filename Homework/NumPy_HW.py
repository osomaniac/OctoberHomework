import numpy as np

## Create an empty board ##
gamearray = np.array([['','',''],['','',''],['','','']])

## Print to Screen
print(gamearray)

## get numbe
count_row = np.count_nonzero(gamearray=='X')
print(count_row)

count_col = np.count_nonzero(gamearray=='X',axis=1)
print(count_col)

## Initialize a Bool
repeat = True
win = False
while repeat:
    ## ask user for row and col
    print("Your turn!")
    row = int(input("Pick your row: "))
    col = int(input("Pick your column: "))
    ## place on board
    while(gamearray[row][col] != ''):
        print("This spot is already taken!")
        row = input("Pick your row: ")
        col = input("Pick your column: ")
    gamearray[row][col] = 'X'

    ## check for a win
    count_row = np.count_nonzero(gamearray=='X', axis=0)
    print(count_row)
    count_col = np.count_nonzero(gamearray=='X',axis=1)
    print(count_col)
    print(gamearray)
    for c in count_col:
        if(c == 3):
            win = True
    for r in count_row:
        if(r == 3):
            win = True
    if((gamearray[0][0] == 'X' and gamearray[1,1] == 'X' and gamearray[2,2] == 'X') or
        (gamearray[0][2] == 'X' and gamearray[1,1] == 'X' and gamearray[2,0] == 'X')):
        win = True
    if(win):
        print("Congrats! You have won!")
        again = input("Would you like to play again? (y/n) ")
        if(again not in ('Y','y','yes','Yes', 'YES')):
            repeat = False
        else:
            win = False
            gamearray = np.array([['','',''],['','',''],['','','']])
    ## print board
    ## so, if 1,1