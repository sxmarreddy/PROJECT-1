import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Happy", "Cool", "Funky", "Brave", "Mysterious", "Epic", "Wild", "Clever", "Sneaky", "Crazy"]
nouns = ["Tiger", "Dragon", "Warrior", "Wizard", "Ninja", "Shadow", "Pirate", "Phoenix", "Knight", "Panther"]

def generate_username(add_numbers=True, add_special_chars=True, length=None):
    """
    Generates a random username by combining an adjective and a noun.
    
    Args:
        add_numbers (bool): Whether to add a random number at the end.
        add_special_chars (bool): Whether to include a special character.
        length (int, optional): Desired length of the username.
    
    Returns:
        str: The generated username.
    """
    # Select a random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Base username
    username = adjective + noun

    # Add a random number (1-999) if enabled
    if add_numbers:
        username += str(random.randint(1, 999))

    # Add a random special character if enabled
    if add_special_chars:
        username += random.choice(string.punctuation)

    # Adjust length if specified
    if length and len(username) > length:
        username = username[:length]  # Trim username to desired length

    return username

def save_usernames(usernames, filename="usernames.txt"):
    """
    Saves a list of generated usernames to a text file.
    
    Args:
        usernames (list): A list of generated usernames.
        filename (str): The filename to save the usernames.
    """
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"\n✅ Usernames saved to '{filename}'")

def main():
    """
    Main function to interact with the user and generate usernames based on preferences.
    """
    print("\n===== Random Username Generator =====")
    
    # User input for preferences
    num_usernames = int(input("How many usernames do you want to generate? "))
    add_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
    add_special_chars = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"
    
    length = input("Enter max length of username (or press Enter to skip): ").strip()
    length = int(length) if length.isdigit() else None  # Convert to integer if input is valid

    usernames = [generate_username(add_numbers, add_special_chars, length) for _ in range(num_usernames)]

    # Display generated usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(f"- {username}")

    # Save usernames to file
    save_to_file = input("\nDo you want to save these usernames to a file? (yes/no): ").strip().lower()
    if save_to_file == "yes":
        save_usernames(usernames)

if __name__ == "__main__":
    main()
