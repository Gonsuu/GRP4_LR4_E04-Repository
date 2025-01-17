import unittest
from unittest.mock import patch, MagicMock
import oxo_dialog_ui

class TestTicTacToeConsoleApp(unittest.TestCase):
    
    def test_get_menu_choice_valid(self):
        """Test getMenuChoice with valid input."""
        menu = ["Option 1", "Option 2", "Option 3"]
        with patch('builtins.input', side_effect=['2']):
            choice = oxo_dialog_ui.getMenuChoice(menu)
        self.assertEqual(choice, 2)

    def test_get_menu_choice_invalid_then_valid(self):
        """Test getMenuChoice handles invalid input gracefully."""
        menu = ["Option 1", "Option 2", "Option 3"]
        with patch('builtins.input', side_effect=['5', '0', '2']):
            choice = oxo_dialog_ui.getMenuChoice(menu)
        self.assertEqual(choice, 2)

    def test_start_game(self):
        """Test startGame calls mocked oxo_logic.newGame."""
        with patch('oxo_dialog_ui.oxo_logic.newGame', return_value=[' '] * 9) as mock_new_game:
            game = oxo_dialog_ui.startGame()
        mock_new_game.assert_called_once()
        self.assertEqual(game, [' '] * 9)

    def test_resume_game(self):
        """Test resumeGame calls mocked oxo_logic.restoreGame."""
        with patch('oxo_dialog_ui.oxo_logic.restoreGame', return_value=['X', 'O', ' '] * 3) as mock_restore_game:
            game = oxo_dialog_ui.resumeGame()
        mock_restore_game.assert_called_once()
        self.assertEqual(game, ['X', 'O', ' '] * 3)

    def test_display_help(self):
        """Test displayHelp outputs help message."""
        with patch('builtins.print') as mock_print:
            oxo_dialog_ui.displayHelp()
        mock_print.assert_called()

    def test_quit(self):
        """Test quit raises SystemExit."""
        with self.assertRaises(SystemExit):
            oxo_dialog_ui.quit()

    def test_execute_choice_play_game(self):
        """Test executeChoice calls the correct function and handles play."""
        with patch('oxo_dialog_ui.startGame', return_value=[' '] * 9) as mock_start_game, \
             patch('oxo_dialog_ui.playGame') as mock_play_game:
            oxo_dialog_ui.executeChoice(1)
        mock_start_game.assert_called_once()
        mock_play_game.assert_called_once_with([' '] * 9)

    def test_print_game(self):
        """Test printGame formats the board correctly."""
        game = ['X', 'O', ' ', ' ', 'X', ' ', 'O', ' ', ' ']
        with patch('builtins.print') as mock_print:
            oxo_dialog_ui.printGame(game)
        mock_print.assert_called()

    def test_play_game_user_move(self):
        """Test playGame processes a user move."""
        game = [' '] * 9
        with patch('oxo_dialog_ui.oxo_logic.userMove', return_value=None) as mock_user_move, \
             patch('oxo_dialog_ui.oxo_logic.computerMove', return_value=None), \
             patch('oxo_dialog_ui.printGame'), \
             patch('builtins.input', side_effect=['1', 'q']), \
             patch('tkinter.messagebox.askyesno', return_value=False):
            oxo_dialog_ui.playGame(game)
        mock_user_move.assert_called_with(game, 0)

    def test_play_game_quit(self):
        """Test playGame saves game on quit."""
        game = [' '] * 9
        with patch('oxo_dialog_ui.oxo_logic.saveGame') as mock_save_game, \
             patch('oxo_dialog_ui.printGame'), \
             patch('builtins.input', side_effect=['q']), \
             patch('tkinter.messagebox.askyesno', return_value=True):
            with self.assertRaises(SystemExit):
                oxo_dialog_ui.playGame(game)
        mock_save_game.assert_called_once_with(game)

if __name__ == '__main__':
    unittest.main()
