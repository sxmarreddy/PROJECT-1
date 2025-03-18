import random
import string

adjectives = ["Happy", "Cool", "Funky", "Brave", "Mysterious", "Epic", "Wild", "Clever", "Sneaky", "Crazy"]
nouns = ["Tiger", "Dragon", "Warrior", "Wizard", "Ninja", "Shadow", "Pirate", "Phoenix", "Knight", "Panther"]

def generate_username(add_numbers=True, add_special_chars=True, length=None):
   
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = adjective + noun

    if add_numbers:
        username += str(random.randint(1, 999))

    if add_special_chars:
        username += random.choice(string.punctuation)

    if length and len(username) > length:
        username = username[:length]

    return username

def save_usernames(usernames, filename="usernames.txt"):
    
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"\n✅ Usernames saved to '{filename}'")

def main():
    print("\n===== Random Username Generator =====")
    
    num_usernames = int(input("How many usernames do you want to generate? "))
    add_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
    add_special_chars = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"
    
    length = input("Enter max length of username (or press Enter to skip): ").strip()
    length = int(length) if length.isdigit() else None  # Convert to integer if input is valid

    usernames = [generate_username(add_numbers, add_special_chars, length) for _ in range(num_usernames)]

    print("\nGenerated Usernames:")
    for username in usernames:
        print(f"- {username}")

    save_to_file = input("\nDo you want to save these usernames to a file? (yes/no): ").strip().lower()
    if save_to_file == "yes":
        save_usernames(usernames)

if __name__ == "__main__":
    main()
