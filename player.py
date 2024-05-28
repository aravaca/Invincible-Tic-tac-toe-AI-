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
            square = input('Your turn (\'X\'). Input move (1-9): ')
            try:
                val = int(square) - 1
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Please try again")
        return val

class AI_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        max = float('-inf')
        ans = None
        opponent_letter = 'X' if self.letter == 'O' else 'O'
        for square in game.available_moves():
            # sim is a copy of the current game that allows the AI to simulate the next move.
            # It does not affect the current status of the game
            sim = copy.deepcopy(game)
            sim.make_move(square, self.letter)
            # The heuristic function is calculated by subtracting the minimizer's(HumanPlayer) # of OWLs 
            # from the maximizer's(AI) # of OWLs. An OWL is a line which contains at least one of the 
            # player’s marks and none of the opponent’s
            heuristic = sim.get_owl(self.letter) - sim.get_owl(opponent_letter)
            if heuristic > max or (heuristic == max and square % 2 == 0): # the mod here prioritizes moves in diagonal squares
                max = heuristic
                ans = square
        return ans
    





