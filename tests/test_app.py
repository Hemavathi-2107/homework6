'''Test file for app'''
import unittest
from app.commands import CommandHandler
from app import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class TestCommandHandler(unittest.TestCase):
    ''''Class'''
    def setUp(self):
        """Initialize CommandHandler and register commands before each test."""
        self.command_handler = CommandHandler()
        self.command_handler.Register_Command("add", AddCommand())
        self.command_handler.Register_Command("subtract", SubtractCommand())
        self.command_handler.Register_Command("multiply", MultiplyCommand())
        self.command_handler.Register_Command("divide", DivideCommand())

    def test_registered_commands(self):
        """Ensure all commands are properly registered."""
        expected_commands = ["add", "subtract", "multiply", "divide"]
        self.assertListEqual(sorted(self.command_handler.get_registered_commands()), sorted(expected_commands))

    def test_execute_add(self):
        """Test addition command execution."""
        result = self.command_handler.Execute_Command("add", "3", "2")
        self.assertEqual(result, 5)

    def test_execute_subtract(self):
        """Test subtraction command execution."""
        result = self.command_handler.Execute_Command("subtract", "10", "4")
        self.assertEqual(result, 6)

    def test_execute_multiply(self):
        """Test multiplication command execution."""
        result = self.command_handler.Execute_Command("multiply", "3", "4")
        self.assertEqual(result, 12)

    def test_execute_divide(self):
        """Test division command execution."""
        result = self.command_handler.Execute_Command("divide", "10", "2")
        self.assertEqual(result, 5)

    def test_execute_divide_by_zero(self):
        """Ensure division by zero is handled properly."""
        result = self.command_handler.Execute_Command("divide", "5", "0")
        self.assertIsNone(result)

    def test_invalid_command(self):
        """Ensure an invalid command is not executed."""
        result = self.command_handler.Execute_Command("unknown_command", "5", "2")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
