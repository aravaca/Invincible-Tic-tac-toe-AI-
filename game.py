import time
from player import HumanPlayer, RandomComputerPlayer, AIPlayer

class TicTacToe:
    def __init__(self):
        #initialize two new variables board and current_winner` W`
        self.board = [' ' for _ in range(9)] # 0-8
        self.current_winner = None

    def print_board(self):
                                #from 0 to 2, 3 to 5, 6 to 8
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            #row here would be [' ',' ',' '] each
            print('| ' + ' | '.join(row) + ' |') 
            # .join([' ',' ',' ']) would automatically print _ | _ | _

    @staticmethod # the only static method here
    def print_board_nums(): # 0 | 1 | 2 
        number_board = [[str(i) for i in range(j*3+1, (j+1)*3+1)] for j in range(3)] # STR(INT) returns str('int')
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "] #enumerate returns list of tuples like (0, ), (1, ), (2, ), ...
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        #The all() function returns True if all items in an iterable are true, otherwise it returns False.
        #If the iterable object is empty, the all() function also returns True.
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    # instance function that calculates the OWL for each player
    # OWL = num of opened(empty or unobstructed) winning lines 
    # @author Hyungsuk Choi (c)2024
    def check_owl(self, letter):
        count = 0
        opponent_letter = 'X' if letter == 'O' else 'O'
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            #check owl
            if letter in row and opponent_letter not in row:
                count+=1
            #prevent loss
            if row.count(opponent_letter) == 2 and letter in row:
                count+=10
            #guarantee win
            if row.count(letter) == 3:
                count+=100
        for col in [self.board[i::3] for i in range(3)]:        
            if letter in col and opponent_letter not in col:
                count+=1
            if col.count(opponent_letter) == 2 and letter in col:
                count+=10
            if col.count(letter) == 3:
                count+=100
        for diagonal1 in [self.board[::4]]:           
            if letter in diagonal1 and opponent_letter not in diagonal1:
                count+=1
            if diagonal1.count(opponent_letter) == 2 and letter in diagonal1:
                count+=10
            if diagonal1.count(letter) == 3:
                count+=100
        for diagonal2 in [self.board[2:7:2]]:
            if letter in diagonal2 and opponent_letter not in diagonal2:
                count+=1
            if diagonal2.count(opponent_letter) == 2 and letter in diagonal2:
                count+=10
            if diagonal2.count(letter) == 3:
                count+=100
        return count


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__': #main method in python 
    x_player = HumanPlayer('X')
    o_player = AIPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)