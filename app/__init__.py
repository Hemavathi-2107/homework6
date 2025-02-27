from app.commands import Command, CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

# Initialize the CommandHandler
command_handler = CommandHandler()

# Register all available commands
# command_handler.Register_Command("add", AddCommand())
# command_handler.Register_Command("subtract", SubtractCommand())
# command_handler.Register_Command("multiply", MultiplyCommand())
# command_handler.Register_Command("divide", DivideCommand())

# Expose relevant components for external use
__all__ = ["command_handler", "Command"]
