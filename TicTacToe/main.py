
theBoard = {
    '7' : ' ', '8': ' ', '9': ' ',
    '4' : ' ', '5': ' ', '6': ' ',
    '1' : ' ', '2': ' ', '3': ' ',
}


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def playerWon(turn):
    printBoard(theBoard)
    print("\nGame Over. \n")
    print("********* " + turn + " worn . **********")



def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)

        print("It is your turn " + turn + " move to which place? ")

        move = input()

        if move not in theBoard:
            print("Invalid input, please try again with other? ")
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1

        else:
            print("That place is already filled, please try again with other? ")
            continue

        if count >= 5:

            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                playerWon(turn)
                break

            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                playerWon(turn)
                break

            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                playerWon(turn)
                break

            if theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                playerWon(turn)
                break

            if theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                playerWon(turn)
                break

        
            if theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                playerWon(turn)
                break
                    
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                playerWon(turn)
                break

            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                playerWon(turn)
                break

        if count == 9:
            print("Game Over")
            print("It is a tie")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    restart = input("Do you want to play again?(y/n) ")
    if restart == 'y' or restart == 'Y':
        for key in theBoard:
            theBoard[key] = ' '
        
        game()
    
if __name__ == "__main__":
    game()

        
    