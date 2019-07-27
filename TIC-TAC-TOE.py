# Here are the requirements:
# 
# * 2 players should be able to play the game (both sitting at the same computer)
# * The board should be printed out every time a player makes a move
# * You should be able to accept input of the player position and then place a symbol on the board
# 

# replace "os.system('cls')" wiht "clear_output()" if you need to run in Jupyter Notebook


from IPython.display import clear_output
import os

def rules():
    os.system('cls') 
    print('\tTIC-TAC-TOE\n\n*It is a 2 player game\n\n*Player1 gets to select the MARKER(X/O)\n\n*Use your NUMPAD 1 to 9 to place your marker\n\n')

def displayBoard(x):
    os.system('cls')
    print(' {:1} | {:1} | {:1} '.format(x[7],x[8],x[9]))
    print('---+---+---')
    print(' {:1} | {:1} | {:1} '.format(x[4],x[5],x[6]))
    print('---+---+---')
    print(' {:1} | {:1} | {:1} '.format(x[1],x[2],x[3]))
        

def select():
    while True:
        player1 = input("Please select your marker 'O' or 'X': ").upper()
        if player1!='X' and player1!='O':
            print("\nPlease select either 'X' or 'O'")
        else:
            break
    player2 = None                
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    print(f'\n\nPlayer1 is {player1}\nPlayer2 is {player2} ')
    return player1, player2

def game(lst, player1, player2):
    flag = 1
    i=1
    if input('\n\nAre you ready? "Yes" or "No": ').lower() == 'yes':
        os.system('cls')
        while flag:
            displayBoard(lst)
            if i%2:
                while True:
                    while True:
                        try:
                            pos = int(input('\nPlayer1: Where do you want to place your marker?\t: '))
                            if 1<=pos<=9:
                                break
                            else:
                                raise ValueError
                        except:
                            print('Invalid Choice of place. Choose number between 1 to 9')
                    if not lst[pos]:
                        lst[pos] = player1
                        break
                    else:
                        print('Place already occupied!')
                displayBoard(lst)
            else:
                while True:
                    while True:
                        try:
                            pos = int(input('\nPlayer2: Where do you want to place your marker?\t: '))
                            if 1<=pos<=9:
                                break
                            else:
                                raise ValueError
                        except:
                            print('Invalid Choice of place. Choose number between 1 to 9')
                    if not lst[pos]:
                        lst[pos] = player2
                        break
                    else:
                        print('Place already occupied!')
                displayBoard(lst)
            i += 1
            finish = finished(lst) 
            if finish == 'W':
                print('Player{} Wins!!'.format((i%2)+1))
                flag = 0
            elif finish == 'D':
                print('\nDRAW!')
                flag = 0
            

def finished(lst):
    if lst[1]==lst[4]==lst[7]!='' or lst[1]==lst[5]==lst[9]!='' or lst[1]==lst[2]==lst[3]!='' or lst[9]==lst[8]==lst[7]!='' or lst[9]==lst[6]==lst[3]!='' or lst[7]==lst[5]==lst[3]!='' or lst[2]==lst[5]==lst[8]!='' or lst[4]==lst[5]==lst[6]!='':
        return 'W'
    elif '' not in lst:
        return 'D'
    else:
        return False

while True:
    #Rules
    rules()

    #Select Players
    p1,p2 = select()

    #Begin Game
    lst = ['']*10
    lst[0] = '#'
    game(lst,p1,p2) 
    
    H = input('\n\nDo you want to play next game? Press Y/N : ')
    if H=='Y' or H=='y':
        continue
    else:
        print('THANK YOU FOR PLAYING!!')
        break

