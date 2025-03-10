import os
import logging
from passg import generate_password
from random import choice, shuffle

# Constants
LOG_FILE = "password_manager.log"
PASSWORD_FILE = "passwords.txt"

# Logging setup
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()

class FileHandler:
    """Handles reading and writing passwords to/from the file."""

    @staticmethod
    def read_passwords() -> list[str]:
        """Read the passwords file and return its content as a list of lines."""
        if not os.path.exists(PASSWORD_FILE):
            return []

        with open(PASSWORD_FILE, "r") as file:
            return file.readlines()

    @staticmethod
    def write_passwords(lines: list[str]) -> None:
        """Write a list of lines to the passwords file."""
        with open(PASSWORD_FILE, "w") as file:
            file.writelines(lines)


class PasswordManager:
    """Handles password management: adding, deleting, and replacing passwords."""

    def __init__(self):
        self.passwords = self.load_passwords()

    def load_passwords(self) -> dict:
        """Load passwords from the file and return them as a dictionary."""
        lines = FileHandler.read_passwords()
        passwords = {}
        for line in lines:
            prompt, password = map(str.strip, line.split(":"))
            passwords[prompt] = password
        return passwords

    def save_passwords(self) -> None:
        """Save the current passwords dictionary to the file."""
        lines = [
            f"{prompt}: {password}\n" for prompt, password in self.passwords.items()
        ]
        FileHandler.write_passwords(lines)

    def add_password(self, prompt: str) -> None:
        """Add a new password for the given prompt."""
        if prompt in self.passwords:
            print(f"Error: '{prompt}' already exists. Use replace or delete instead.")
            return

        password = generate_password()
        self.passwords[prompt] = password
        self.save_passwords()

        logger.info(f"Added password for '{prompt}'")
        print(f"Password for '{prompt}' has been added successfully.")

    def delete_password(self, prompt: str) -> None:
        """Delete the password associated with the given prompt."""
        if prompt not in self.passwords:
            print(f"Error: '{prompt}' not found.")
            return

        del self.passwords[prompt]
        self.save_passwords()

        logger.info(f"Deleted password for '{prompt}'")
        print(f"Password for '{prompt}' has been deleted successfully.")

    def replace_password(self, prompt: str) -> None:
        """Replace the password associated with the given prompt."""
        if prompt not in self.passwords:
            print(f"Error: '{prompt}' not found.")
            return

        new_password = generate_password()
        self.passwords[prompt] = new_password
        self.save_passwords()

        logger.info(f"Replaced password for '{prompt}'")
        print(f"Password for '{prompt}' has been replaced successfully.")

    def show_passwords(self) -> None:
        """Display all saved passwords."""
        if not self.passwords:
            print("No saved passwords.")
        else:
            print("\nSaved Passwords:")
            print("----------------------------")
            for prompt, password in self.passwords.items():
                print(f"{prompt}: {password}")
            print("----------------------------")

    def delete_all_passwords(self) -> None:
        """Delete all saved passwords."""
        if not self.passwords:
            print("No saved passwords.")
        else:
            user_validation = input(
                "Type 'yes' if you are sure you want to delete all the passwords? (you will never get them back!) : "
            )
            if user_validation.lower().strip() == "yes":
                self.passwords = {}
                self.save_passwords()
            logger.info(f"All passwords have been deleted")
            print(f"All passwords have been deleted successfully.")


class Main:
    """The entry point for the password manager application."""

    @staticmethod
    def display_menu() -> None:
        """Displays the available commands to the user."""
        print(
            """
        Password Manager Commands:
        add [prompt]      - Add a new password for the given prompt
        delete [prompt]   - Delete the password for the given prompt
        replace [prompt]  - Replaces the password for the given prompt
        show              - Shows all saved passwords
        delete all        - Deletes all saved passwords
        exit              - Exit the application
        """
        )

    @staticmethod
    def run():
        """Main loop to handle user input."""
        manager = PasswordManager()

        while True:
            Main.display_menu()
            command = input("Enter a command: ").strip().lower()

            if command.startswith("add "):
                prompt = command[4:].strip()
                manager.add_password(prompt)
            elif command == "delete all":
                manager.delete_all_passwords()
            elif command.startswith("delete "):
                prompt = command[7:].strip()
                manager.delete_password(prompt)
            elif command.startswith("replace "):
                prompt = command[8:].strip()
                manager.replace_password(prompt)
            elif command == "show":
                manager.show_passwords()
            elif command == "exit":
                print("Exiting password manager.")
                break
            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    Main.run()