import random
class Gameboard: 
    """A class to represent the gameboard of a tic-tac-toe game."""

    winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9],[1, 5, 9], [3, 5, 7]]
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

    def check_winner(self):
        """
        This method checks if there is a winner on the gameboard.
        It returns 'X' if player X has won, 'O' if player O has won, or None if there is no winner yet.
        """
        board = self.board
        for combo in self.winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]]:
                return f"{board[combo[0]]}"
        if all(v in ['X', 'O'] for v in board.values()):
            return "-" #"Draw!"
        return None # No winner yet

    def update_score(self, player):
        """
        This method updates the score of the player who won the game.
        It increments the score of the winning player by 1.
        """
        if player is not None:
            self.score[player] += 1
        

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
    status = {"X": "Player X won!", "O": "Player O won!", "-": "Draw!", None: "No winner yet."}
    result = gameboard.check_winner()
    print(status[result])
