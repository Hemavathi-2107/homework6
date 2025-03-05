# pylint: disable=missing-class-docstring
'''This is the test_command file'''

from unittest.mock import Mock, patch
import pytest
from app.plugins.addcommand import Add
from app.plugins.subtractcommand import Subtract
from app.plugins.multiplycommand import Multiply
from app.plugins.dividecommand import Divide
from app.plugins.menucommand import Menu

@pytest.fixture
def mock_command_handler():
    '''Mock command handler'''
    mock_handler = Mock()
    mock_handler.Register_Command = Mock()
    mock_handler.Execute_Command = Mock()
    return mock_handler

@pytest.fixture
def add_command(mock_command_handler):
    '''Fixture for Add command'''
    return Add(command_handler=mock_command_handler)

@pytest.fixture
def subtract_command(mock_command_handler):
    '''Fixture for Subtract command'''
    return Subtract(command_handler=mock_command_handler)

@pytest.fixture
def multiply_command(mock_command_handler):
    '''Fixture for Multiply command'''
    return Multiply(command_handler=mock_command_handler)

@pytest.fixture
def divide_command(mock_command_handler):
    '''Fixture for Divide command'''
    return Divide(command_handler=mock_command_handler)

@pytest.fixture
def menu_command(mock_command_handler):
    '''Fixture for Menu Command'''
    # Mock command handler to return the list of commands
    mock_command_handler.Get_Registered_Commands = Mock(return_value=["Add", "Subtract", "Multiply", "Divide", "Menu"])
    return Menu(command_handler=mock_command_handler)


# Testing the Add Command
class TestAddCommand:
    '''Test the Add command'''
    def test_add(self, add_command, capsys):
        '''Test successful addition'''
        add_command.execute('2', '3')
        captured = capsys.readouterr()
        assert "2 + 3 = 5" in captured.out

    def test_add_one_argument(self, add_command, capsys):
        '''Test when only one argument is given'''
        add_command.execute('2')
        captured = capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_add_invalid_args(self, add_command, capsys):
        '''Test invalid arguments'''
        add_command.execute('x', '2')
        captured = capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_add_error(self, add_command, capsys):
        '''Test when the calculator throws an error'''
        with patch('app.plugins.addcommand.Calculator.add', side_effect=ValueError("Error")):
            add_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out


# Testing the Subtract Command
class TestSubtractCommand:
    '''Test the Subtract command'''
    def test_subtract(self, subtract_command, capsys):
        '''Test successful subtraction'''
        subtract_command.execute('4', '2')
        captured = capsys.readouterr()
        assert "4 - 2 = 2" in captured.out

    def test_subtract_one_argument(self, subtract_command, capsys):
        '''Test when only one argument is given'''
        subtract_command.execute('4')
        captured = capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_subtract_invalid_args(self, subtract_command, capsys):
        '''Test invalid arguments'''
        subtract_command.execute('x', '3')
        captured = capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_subtract_negative_numbers(self, subtract_command, capsys):
        '''Test subtraction with negative numbers'''
        subtract_command.execute('-5', '3')
        captured = capsys.readouterr()
        assert "-5 - 3 = -8" in captured.out

    def test_subtract_error(self, subtract_command, capsys):
        '''Test when the calculator throws an error'''
        with patch('app.plugins.subtractcommand.Calculator.subtract', side_effect=ValueError("Error")):
            subtract_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out


# Testing the Multiply Command
class TestMultiplyCommand:
    '''Test the Multiply command'''
    def test_multiply(self, multiply_command, capsys):
        '''Test successful multiplication'''
        multiply_command.execute('4', '2')
        captured = capsys.readouterr()
        assert "4 * 2 = 8" in captured.out

    def test_multiply_one_argument(self, multiply_command, capsys):
        '''Test when only one argument is given'''
        multiply_command.execute('4')
        captured = capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_multiply_invalid_args(self, multiply_command, capsys):
        '''Test invalid arguments'''
        multiply_command.execute('x', '3')
        captured = capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_multiply_error(self, multiply_command, capsys):
        '''Test when the calculator throws an error'''
        with patch('app.plugins.multiplycommand.Calculator.multiply', side_effect=ValueError("Error")):
            multiply_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out


# Testing the Divide Command
class TestDivideCommand:
    '''Test the Divide command'''
    def test_divide(self, divide_command, capsys):
        '''Test successful division'''
        divide_command.execute('4', '2')
        captured = capsys.readouterr()
        assert "4 / 2 = 2" in captured.out

    def test_divide_one_argument(self, divide_command, capsys):
        '''Test when only one argument is given'''
        divide_command.execute('4')
        captured = capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_divide_invalid_args(self, divide_command, capsys):
        '''Test invalid arguments'''
        divide_command.execute('x', '3')
        captured = capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_divide_by_zero(self, divide_command, capsys):
        '''Test division by zero'''
        divide_command.execute('9', '0')
        captured = capsys.readouterr()
        assert "Error: Cannot divide by zero" in captured.out

    def test_divide_error(self, divide_command, capsys):
        '''Test when the calculator throws an error'''
        with patch('app.plugins.dividecommand.Calculator.divide', side_effect=ValueError("Error")):
            divide_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out


# Testing the Menu Command
class TestMenuCommand:
    '''Test the Menu command'''
    def test_menu_command(self, menu_command, capsys):
        '''Test that the Menu command displays the list of available commands'''
        menu_command.execute()
        captured = capsys.readouterr()
        assert "Commands Available:" in captured.out, "MenuCommand should display the available commands"
        assert "Add" in captured.out
        assert "Subtract" in captured.out
        assert "Multiply" in captured.out
        assert "Divide" in captured.out
        assert "Menu" in captured.out
