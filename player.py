import random, copy

class Player:
    def __init__(self, letter):
        #lettter is either x or o
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (1-9): ')
            try:
                val = int(square) - 1
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, try again")
        return val

# AI Player that never loses (either wins or ties) using Minimax algorithm
# @author Hyungsuk Choi (c)2024
class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # lookahead one move using sim, a copy of the current game
        max = float('-inf')
        ans = None
        opponent_letter = 'X' if self.letter == 'O' else 'O'
        for square in game.available_moves():
            sim = copy.deepcopy(game)
            sim.make_move(square, self.letter)
            # h() = MAX OWL (AI) - MIN OWL
            heuristic = sim.check_owl(self.letter) - sim.check_owl(opponent_letter)
            # print(square, heuristic) #for debugging purposes
            if heuristic > max:
                max = heuristic
                ans = square
        return ans
    





