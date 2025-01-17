import random
import os
import oxo_data  # Assuming this module handles saving and restoring the game state.


class TicTacToe:
    def __init__(self):
        self.game = [" "] * 9  # Initializes a new empty game board.
        self.wins = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)             # Diagonal
        )

    def new_game(self):
        """Start a new game by resetting the board."""
        self.game = [" "] * 9

    def save_game(self):
        """Save the current game state to disk."""
        oxo_data.saveGame(self.game)

    def restore_game(self):
        """Restore a saved game from disk or start a new game if restoration fails."""
        try:
            restored_game = oxo_data.restoreGame()
            if len(restored_game) == 9:
                self.game = restored_game
            else:
                self.new_game()
        except IOError:
            self.new_game()

    def _generate_move(self):
        """Generate a random valid move from available cells."""
        options = [i for i, cell in enumerate(self.game) if cell == " "]
        return random.choice(options) if options else -1

    def _is_winning_move(self):
        """Check if the current game state contains a winning line."""
        for a, b, c in self.wins:
            chars = self.game[a] + self.game[b] + self.game[c]
            if chars == "XXX" or chars == "OOO":
                return True
        return False

    def user_move(self, cell):
        """Make a move for the user at the specified cell."""
        if self.game[cell] != " ":
            raise ValueError("Invalid cell")
        self.game[cell] = "X"
        return "X" if self._is_winning_move() else ""

    def computer_move(self):
        """Make a random move for the computer."""
        cell = self._generate_move()
        if cell == -1:
            return "D"  # Draw
        self.game[cell] = "O"
        return "O" if self._is_winning_move() else ""

    def display_board(self):
        """Print the current game board."""
        board = "\n".join([
            f" {self.game[i]} | {self.game[i + 1]} | {self.game[i + 2]} "
            for i in range(0, 9, 3)
        ])
        separator = "\n---+---+---\n"
        print(board.replace("\n", separator))
        print()


def test():
    game = TicTacToe()
    game.new_game()  # Start a new game
    result = ""

    while not result:
        game.display_board()
        try:
            result = game.user_move(game._generate_move())
        except ValueError:
            print("Oops, invalid move.")
        if not result:
            result = game.computer_move()

    game.display_board()
    if result == "D":
        print("It's a draw!")
    else:
        print(f"Winner is: {result}")


if __name__ == "__main__":
    test()
