# Password Manager

Welcome to the **Password Manager**, a simple and secure tool to manage your passwords. This Python-based application allows you to add, delete, replace, and view passwords with ease. All passwords are stored locally in a file, and the application logs all actions for security and tracking purposes.

---

## Features

- **Add Passwords**: Generate and store a new password for a given prompt (e.g., a website or service name).
- **Delete Passwords**: Remove a password associated with a specific prompt.
- **Replace Passwords**: Replace an existing password with a new one.
- **Show Passwords**: View all saved passwords.
- **Delete All Passwords**: Clear all saved passwords (with user confirmation).
- **Secure Password Generation**: Uses the `passg` library to generate strong, random passwords.
- **Logging**: All actions are logged in a file (`password_manager.log`) for accountability.

---

## How to Use

1. **Install Dependencies**: Ensure you have Python installed. Install the required library using pip:

   ```bash
   pip install passg
   ```

2. **Run the Application**: Execute the script to start the password manager:

   ```bash
   python password_manager.py
   ```

3. **Follow the Menu**: Use the following commands to manage your passwords:
   - `add [prompt]`: Add a new password for the given prompt.
   - `delete [prompt]`: Delete the password for the given prompt.
   - `replace [prompt]`: Replace the password for the given prompt.
   - `show`: Display all saved passwords.
   - `delete all`: Delete all saved passwords (requires confirmation).
   - `exit`: Exit the application.

---

## File Structure

- **`passwords.txt`**: Stores all saved passwords in the format `prompt: password`.
- **`password_manager.log`**: Logs all actions performed by the user.

---

## Example Usage

```bash
Password Manager Commands:
add [prompt]      - Add a new password for the given prompt
delete [prompt]   - Delete the password for the given prompt
replace [prompt]  - Replaces the password for the given prompt
show              - Shows all saved passwords
delete all        - Deletes all saved passwords
exit              - Exit the application

Enter a command: add email
Password for 'email' has been added successfully.
```

---

## Notes

- **Security**: Passwords are stored in plaintext in `passwords.txt`. For enhanced security, consider encrypting the file or using a dedicated password manager.
- **Logs**: The `password_manager.log` file records all actions, including additions, deletions, and replacements.
- **Dependencies**: This application relies on the `passg` library for password generation. Make sure it is installed before running the script.

---

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

---

Thank you for using the **Password Manager**! If you have any questions or suggestions, please feel free to reach out. :)
