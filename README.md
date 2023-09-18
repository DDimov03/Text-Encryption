# Text Encryption Application

## Overview
This Python application provides a simple graphical user interface (GUI) for text encryption using the Advanced Encryption Standard (AES) algorithm in Cipher Block Chaining (CBC) mode. It utilizes the Tkinter library for GUI development and the cryptography library for AES encryption.

![Encryption](https://github.com/DDimov03/Text-Encryption/assets/110220663/ba0b504e-0d32-4f23-aa25-84a77e34c1f4)


## Features
- User-friendly GUI for text input and encryption.
- Generates a random AES key for each encryption session.
- Encrypts user-provided text and displays the encrypted text along with the AES key used.

## Getting Started (If you are not on Windows)
1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:
```
pip install tkinter cryptography
```
4. Clone this repository to your local machine:
```
git clone https://github.com/yourusername/text-encryption-app.git
```
5. Navigate to the project directory:
```
cd text-encryption-app
```
6. Run the application by executing the script:
```
   python text_encryption.py
   ```


## Usage
1. Launch the application.
2. Enter the text you want to encrypt in the input field.
3. Click the "Encrypt" button to perform encryption.
4. The encrypted text and the AES key used for encryption will be displayed in the output field.

**Note:** The AES key is generated randomly for each encryption session and is essential for decryption. Ensure you securely store the AES key if you plan to decrypt the text later.

## Customization
- You can modify the appearance of the GUI by adjusting the style settings in the code, such as font size, padding, and button size.
- To add additional functionality or integrate this code into a larger project, you can extend the codebase as needed.

## Dependencies
- Python 3.x
- Tkinter (for GUI development)
- cryptography (for AES encryption)

## Credits
This Text Encryption Application was created by Denis Dimov.
