"""main module for the Tic Tac Toe game."""
from Gameboard import Gameboard

def get_players():
    """Prompt the user to choose their symbol (X or O) and return the player symbols."""
    while True:
        mode = input("Choose game mode:\n1. Player vs computer\n2. Player vs player")
        p = int(mode) if mode.isdigit() else None
        if p in [1, 2]:
            return p
        else:
            print("Invalid input. Please enter 1 or 2.")    

def main():
    """Main function to run the Tic Tac Toe game."""

    gameboard = Gameboard()
    players = get_players()
    current_player = 'X'

    while True:
        gameboard.display_board()
        if players == 1 and current_player == 'O':
            message = gameboard.computer_move(current_player)
        else:
            position = input(f"Player {current_player}, enter your move (1-9): ")
            position = int(position) if position.isdigit() else None
            if position not in range(1, 10):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            message = gameboard.player_move(current_player, position)
        print(message)
        winner = gameboard.check_winner()
        if winner:
            gameboard.display_board()
            status = {"X": "Player X won!", "O": "Player O won!", "-": "Draw!"}
            print(status[winner])
            gameboard.update_score(winner)
            print(f"Scoreboard: {gameboard.score}")
            break   
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()