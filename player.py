import random

class Player:
    def __init__(self, letter):
        #lettter is either X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

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
    
    def get_move(self, sim):

        opponent = 'X' if self.letter == 'O' else 'O'

        # edge case #1, N/A priority
        if sim.board[2::4] == ['X', 'X'] and sim.board[4] == 'O' and sim.num_empty_squares(sim) == 6:
            return random.choice([1,3,5,7])
        
        # edge case #2, N/A priority
        if sim.board[0:5:4] == ['X', 'X'] and sim.board[8] == 'O' and sim.num_empty_squares(sim) == 6:
            return random.choice([2, 6])

        # simulate a move, guarantee win, highest priority
        for square in sim.available_moves():
            sim.sim_move(square, self.letter)
            if sim.winner(square, self.letter):
                sim.return_state(square)
                return square
            # return to state before simulation
            sim.return_state(square)
           
        # block opponent win, second highest priority
        for square in sim.available_moves():
            sim.sim_move(square, opponent)
            if sim.winner(square, opponent):
                sim.return_state(square)
                return square
            sim.return_state(square)

        # create fork, third highest priority
        for square in sim.available_moves():
            sim.sim_move(square, self.letter)
            if sim.get_owl(self.letter) == 2:
                sim.return_state(square)
                return square
            sim.return_state(square)

        # block opponent's fork, fourth highest priority
        for square in sim.available_moves():
            sim.sim_move(square, opponent)
            if sim.get_owl(opponent) == 2:
                sim.return_state(square)
                # square (intersection space) is empty
                for square2 in sim.available_moves():
                    sim.sim_move(square2, self.letter)
                    two_in_row, square3 = sim.check_two_in_row(self.letter, square2)
                    valid = sim.sim_move(square3, opponent)
                    if two_in_row and sim.get_owl(opponent) != 2:
                            sim.return_state(square2)
                            if valid:
                                sim.return_state(square3)
                            return square2
                    else:   
                        sim.return_state(square2)
                        if valid:
                            sim.return_state(square3)
                        return square
            sim.return_state(square)

        # play the center, fifth highest priority
        # however, if the board is completely empty, playing an edge induces more mistakes from opponent
        if sim.num_empty_squares(sim) == 9:
            return random.choice([1,3,5,7])
        elif sim.board[4] == ' ':
            return 4

        # play the opposite empty corner, sixth highest priority
        if sim.board[0] == opponent and sim.board[8] == ' ':
            return 8
        if sim.board[8] == opponent and sim.board[0] == ' ':
            return 0
        if sim.board[2] == opponent and sim.board[6] == ' ':
            return 6
        if sim.board[6] == opponent and sim.board[2] == ' ':
            return 2
        
        # play an empty corner, seventh highest priority
        empty_corner = [x for x in [0,2,6,8] if sim.board[x] == ' ']
        if empty_corner != []:
            return random.choice(empty_corner)

        # play an empty side, last highest priority
        empty_side = [y for y in [1,3,5,7] if sim.board[y] == ' ']
        if empty_side != []:
            return random.choice(empty_side)
    
        # if none of the above cases apply, just pick any square in random
        for square in sim.available_moves():
            return square






