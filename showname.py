# Program to print your name in Python

def print_name():
    try:
        # Ask the user for their name
        name = input("Enter your name: ").strip()

        # Validate input
        if not name:
            print("You didn't enter a name.")
            return

        # Print the name
        print(f"Hello, {name}!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    print_name()
