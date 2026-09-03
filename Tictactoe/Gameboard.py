class Gameboard: 
    """A class to represent the gameboard of a tic-tac-toe game."""
    def __init__(self):
        self.board = {x:str(x) for x in range(1, 10)}
        #initialize the board with numbers 1-9 representing empty spaces


    def display_board(self):
        b = self.board
        print("\n")
        print(f"{b[1]} | {b[2]} | {b[3]}")
        print("--+---+--")       
        print(f"{b[4]} | {b[5]} | {b[6]}")
        print("--+---+--")
        print(f"{b[7]} | {b[8]} | {b[9]}")
        print("\n")

    def player_move(self, player, position):
        if self.board[position] not in ['X', 'O']:
            self.board[position] = player 
            message = f"Player {player} played at position {position}."
        else:
            message = f"Position {position} is already taken."
        return message

    def computer_move(self, player):
        """
        This method allows the computer to make a move on the gameboard.
        It randomly selects an empty position and places the player's symbol ('X' or 'O') there.
        """
        import random
        position = random.choice([k for k, v in self.board.items() if v not in ['X', 'O']])
        message = self.player_move(player, position)
        return message

if __name__ == "__main__":
    gameboard = Gameboard()
    gameboard.display_board()
    m = gameboard.player_move('X', 5)
    gameboard.display_board()
    print("-----------------")
    print(m)
    print("-----------------")
    m = gameboard.computer_move('O')
    gameboard.display_board()
    print("-----------------")
    print(m)
    print("-----------------")