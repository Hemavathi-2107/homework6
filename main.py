from app.commands import command_handler

def main():
    print("Welcome to the Command Pattern Calculator!")
    print("Type 'menu' to see the available commands.")
    
    while True:
        # Ask the user for a command input
        command_name = input("\nEnter command (or 'exit' to quit): ").strip().lower()

        if command_name == "exit":
            print("Exiting... Goodbye!")
            break
        elif command_name == "menu":
            # Display all registered commands
            print("Available commands:", ", ".join(command_handler.get_registered_commands()))
        elif command_name in command_handler.get_registered_commands():
            try:
                # Ask for numbers from the user
                args = input("Enter the numbers separated by space: ").strip().split()
                # Execute the command with the provided arguments
                result = command_handler.Execute_Command(command_name, *args)
                if result is not None:
                    print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"{command_name}: Command not found. Type 'menu' to see available commands.")

if __name__ == "__main__":
    main()
