import time, random
from player import HumanPlayer, AI_Player

class TicTacToe:

    # global variables that represent the scoreboard
    win = 0
    loss = 0
    tie = 0

    def __init__(self):
        #initialize two variables board and current_winner
        self.board = [' ' for _ in range(9)] # 0-8
        self.current_winner = None

    def print_board(self):
                                #from 0 to 2, 3 to 5, 6 to 8
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            #row here would be [' ',' ',' '] each
            print('| ' + ' | '.join(row) + ' |') 
            # .join([' ',' ',' ']) would automatically print _ | _ | _

    @staticmethod
    def print_board_nums(): # 0 | 1 | 2 
        number_board = [[str(i) for i in range(j*3+1, (j+1)*3+1)] for j in range(3)] # str(INT) returns str('INT')
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "] #enumerate returns list of tuples like (0, ), (1, ), (2, ), ...
    
    def empty_squares(self):
        return ' ' in self.board
    
    @staticmethod
    def num_empty_squares(self):
        return self.board.count(' ')
    
    # simulate a move for the AI
    def sim_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        return False
    
    # return to state before simulation for the AI
    def return_state(self, square):
        self.board[square] = ' '
    
    # actually make a move for the HumanPlayer
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # check the row if the player for letter has won
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        # The all() function returns True if all items in an iterable are true, otherwise it returns False.
        # If the iterable object is empty, the all() function also returns True.
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    # This function calculates the number of OWLs of 2 for a specified player
    # OWLs of count stand for opened (non-blocked) winning lines of two
    def get_owl(self, letter):
        owl = 0
        opponent_letter = 'X' if letter == 'O' else 'O'

        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            #check number of OWLs, lowest priority
            if row.count(letter) == 2 and opponent_letter not in row:
                owl+=1

        for col in [self.board[i::3] for i in range(3)]:        
            if col.count(letter) == 2 and opponent_letter not in col:
                owl+=1

        for diagonal1 in [self.board[::4]]:           
            if diagonal1.count(letter) == 2 and opponent_letter not in diagonal1:
                owl+=1

        for diagonal2 in [self.board[2:7:2]]:
            if diagonal2.count(letter) == 2 and opponent_letter not in diagonal2:
                owl+=1

        return owl

    # This function checks whether there exists a row/col/diagonal with
    # two 'letter's and a blank and returns the boolean value with the 
    # index of the blank square 
    def check_two_in_row(self, letter, square):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if row.count(letter) == 2 and ' ' in row:
            return (True, row.index(' ') + (3 * row_ind))
        
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if col.count(letter) == 2 and ' ' in col:
            return (True, (col.index(' ') * 3) + col_ind)
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if diagonal1.count(letter) == 2 and ' ' in diagonal1:
                return (True, diagonal1.index(' ') * 4)
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if diagonal2.count(letter) == 2 and ' ' in diagonal2:
                return (True, (diagonal2.index(' ') * 2) + 2)
            
        return (False, 0)


def play(game, x_player, o_player, print_game=True, init=True):

    if print_game:
        game.print_board_nums()

    letter = 'X' if init == True else 'O'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                if letter == 'O':
                    time.sleep(0.8) #delay execution to imitate an AI feel
                    script = random.randint(0,3)
                    match script:
                        case 0:
                            print('Hmm.. I\'ll move to square {}.'.format(square + 1))
                        case 1:
                            print('I\'ll pick square {}.'.format(square + 1))
                        case 2:
                            print('I\'ll take square {}!'.format(square + 1))
                        case _:
                            print('I\'ll choose square {}.'.format(square + 1))
                # else:
                #     print('You made a move to square {}.'.format(square + 1))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    if letter == 'O':
                        TicTacToe.loss+=1
                        print('I win!')
                    else:
                        TicTacToe.win+=1
                        print("You win!!! (How though?? lol)")
                return letter  # ends the loop and exits the game
            
            letter = 'O' if letter == 'X' else 'X'  # switches player
    # end of while loop

    if print_game:
        TicTacToe.tie+=1
        print('It\'s a tie!')

if __name__ == '__main__':
    
    x_player = HumanPlayer('X')
    o_player = AI_Player('O')
    again = True

    print("Hi, I am your smart Tic-tac-toe AI. Try your best to win against me!")

    while again:
        t = TicTacToe() # generate a new game board every attempt
        valid_input = False
        while not valid_input:
            try:
                print("")
                ans = str(input("Would you like to go first? (y/n): "))
                if "y" in ans.lower():
                    valid_input = True
                    play(t, x_player, o_player, print_game=True, init=True)    
                elif "n" in ans.lower():
                    valid_input = True
                    play(t, x_player, o_player, print_game=True, init=False)    
                else:
                    raise TypeError
            except TypeError:
                print("\nInvalid input. Please type y/n")
        
        print("\nCurrent record: {}W-{}L-{}D".format(TicTacToe.win, TicTacToe.loss, TicTacToe.tie))
        print('')
        valid_input = False
        while not valid_input:
            try:
                # this if statement prevents possible stack overflow and limits the maximum # of losses/ties to 100
                if TicTacToe.loss < 100 and TicTacToe.tie < 100:
                    ans = str(input("Would you like to play again? (y/n): "))
                    if "y" in ans.lower():
                        valid_input = True
                        pass
                    elif "n" in ans.lower():
                        valid_input = True
                        again = False
                        time.sleep(0.8)
                        print("\nThanks for playing with me!\n")
                        time.sleep(0.4)
                        print("Final record: {}W-{}L-{}D".format(TicTacToe.win, TicTacToe.loss, TicTacToe.tie))
                        time.sleep(3)
                        print('')
                    else:
                        raise TypeError
                else:
                    valid_input = True
                    again = False
                    time.sleep(0.8)
                    print("\nThanks for playing with me!\n")
                    time.sleep(0.4)
                    print("Final record: {}W-{}L-{}D".format(TicTacToe.win, TicTacToe.loss, TicTacToe.tie))
                    time.sleep(3)
                    print('')
                    
            except TypeError:
                print("\nInvalid input. Please type y/n\n")
