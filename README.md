# 🔐 Secure Password Vault CLI

A professional, high-security command-line tool designed to manage your credentials with military-grade encryption and a sleek user interface. Use this tool to store, generate, and manage your passwords safely on your local machine.

## 🌟 Key Features

- **🛡️ AES Encryption**: All passwords are encrypted using **Fernet (AES-128)** symmetric encryption before being saved to disk.
- **👁️ Stealth Input**: Uses secure terminal overrides (`getpass`) so your passwords are never displayed as you type them.
- **📊 Password Strength Indicator**: Real-time validation ensures your passwords follow best practices (length, casing, digits, and special characters).
- **📋 Management Suite**: Add, Update, Delete, and Search credentials by Website, Username, or ID.
- **📈 Summary Statistics**: Get a quick overview of your vault, including total entries and unique websites protected.
- **🎨 Premium UI**: Beautifully formatted tables and color-coded feedback powered by `colorama` and `tabulate`.
- **🚫 Duplicate Prevention**: Internal logic prevents accidental duplicate entries for the same website and username.

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- Active virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MIHMahmudEli/PasswordVault.git
   cd PasswordVault
   ```

2. **Set up a virtual environment (Optional but Recommended):**
   - **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## 🛠️ Tech Stack

- **[Cryptography](https://cryptography.io/)**: For robust Fernet encryption.
- **[Colorama](https://pypi.org/project/colorama/)**: For cross-platform terminal colors.
- **[Tabulate](https://pypi.org/project/tabulate/)**: For clean, grid-style data representation.
- **[GetPass](https://docs.python.org/3/library/getpass.html)**: For secure hidden password input.

## 🏗️ Project Structure

```text
├── main.py              # Entry point
├── menu.py              # High-level Menu logic (Inherited from UI)
├── ui.py                # User Interface & interaction logic
├── service.py           # Business logic & Crypto integration
├── storage.py           # JSON Persistence layer
├── crypto_manager.py    # AES Encryption/Decryption engine
├── models.py            # Credential data models
├── utils.py             # Validation helpers (Strength, Duplicates)
└── passwords.json       # Encrypted data storage
```

## 📜 Usage Guide

- **Searching**: Use Option 3 to find accounts by website name, username, or even specific ID.
- **Updating**: Option 6 allows you to modify existing accounts. Leave fields blank to keep current values.
- **Generation**: Don't have a secure password? Leave the password field blank when adding to generate a strong, 16-character secret automatically.

## ⚠️ Security Warning

The application generates a file named `secret.key` upon first run. **NEVER share OR push this file to Git.** Without this key, your `passwords.json` file becomes unrecoverable. It is highly recommended to keep a backup of your key in a safe, offline location.

---
*Developed with ❤️ by Mih Mahmud*
