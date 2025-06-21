# filepath: /Users/sumitkumarshukla/Team-3/new.py

def greet_user(name=""):
    """
    Function to greet the user with their name
    If no name is provided, asks for the name
    """
    if name == "":
        name = input("Please enter your name: ")
    
    print(f"Hello, {name}! Welcome to our application.")
    return f"Hello, {name}! Welcome to our application."

# Example usage
if __name__ == "__main__":
    user_name = input("Please enter your name (or press Enter to skip): ")
    greet_user(user_name)