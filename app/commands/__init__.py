from abc import ABC, abstractmethod

class Command(ABC):
    '''This is the abstract base class for commands.'''
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    '''This is the CommandHandler class.'''
    def __init__(self):
        self.commands = {}

    def Register_Command(self, command_name: str, command: Command):
        '''This function registers a command.'''
        self.commands[command_name] = command
        print(f"Registered command: {command_name}")

    def Execute_Command(self, command_name: str, *args):
        '''Executes a registered command if it exists.'''
        try:
            if command_name in self.commands:
                return self.commands[command_name].execute(*args)
            else:
                print(f"{command_name}: Command not found")
        except (KeyError, TypeError):
            print(f"{command_name}: Invalid command or incorrect arguments provided")

    def get_registered_commands(self):
        '''Returns a list of registered commands.'''
        return list(self.commands.keys())

# Initialize the command handler
command_handler = CommandHandler()
