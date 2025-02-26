from commands import Command

class AddCommand(Command):
    '''This class implements the addition command.'''
    def execute(self, *args):
        try:
            return sum(map(float, args))
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
            return None
