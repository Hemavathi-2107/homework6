'''Test file for commands'''
import unittest
from app import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class TestCommands(unittest.TestCase):
    '''class'''
    def test_add_command(self):
        """Test the addition command."""
        command = AddCommand()
        self.assertEqual(command.execute("3", "2"), 5)
        self.assertEqual(command.execute("3.5", "2.5"), 6)
        self.assertEqual(command.execute("10", "-5"), 5)

    def test_subtract_command(self):
        """Test the subtraction command."""
        command = SubtractCommand()
        self.assertEqual(command.execute("10", "4"), 6)
        self.assertEqual(command.execute("5", "10"), -5)
        self.assertEqual(command.execute("5.5", "2.5"), 3)

    def test_multiply_command(self):
        """Test the multiplication command."""
        command = MultiplyCommand()
        self.assertEqual(command.execute("3", "4"), 12)
        self.assertEqual(command.execute("5", "-2"), -10)
        self.assertEqual(command.execute("1.5", "2"), 3)

    def test_divide_command(self):
        """Test the division command."""
        command = DivideCommand()
        self.assertEqual(command.execute("10", "2"), 5)
        self.assertEqual(command.execute("9", "3"), 3)
        self.assertEqual(command.execute("5", "2"), 2.5)  # Decimal result expected

    def test_divide_by_zero(self):
        """Ensure division by zero is handled."""
        command = DivideCommand()
        self.assertIsNone(command.execute("5", "0"))

    def test_invalid_input(self):
        """Ensure non-numeric inputs are handled gracefully."""
        command = AddCommand()
        self.assertIsNone(command.execute("five", "three"))

if __name__ == "__main__":
    unittest.main()
