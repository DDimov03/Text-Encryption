import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet

# Generate a random AES key
def generate_aes_key():
    return Fernet.generate_key()

# Initialize the cipher suite with a given key
def initialize_cipher_suite(key):
    return Fernet(key)

# Encrypt text using AES-CBC
def encrypt_text(text, cipher_suite):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

# Function to perform encryption and update the result container
def perform_encryption():
    input_text = entry.get()
    aes_key = generate_aes_key()
    cipher_suite = initialize_cipher_suite(aes_key)
    encrypted_text = encrypt_text(input_text, cipher_suite)
    
    # Insert the encrypted text and AES key into the Text widget
    output_text.config(state=tk.NORMAL)  # Enable editing
    output_text.delete(1.0, tk.END)  # Clear existing content
    output_text.insert(tk.END, f"Encrypted Text: {encrypted_text.decode()}\nAES Key: {aes_key.decode()}")
    output_text.config(state=tk.DISABLED)  # Disable editing

# Create the main window
window = tk.Tk()
window.title("Text Encryption")

# Set window size and make it unresizable
window.geometry("350x400")  # Fixed window size
window.resizable(False, False)  # Disable resizing

# Create a themed style
style = ttk.Style()

# Configure the style for the input field
style.configure("TEntry",
                font=("Arial", 24),  # Increase font size
                padding=15,  # Add padding
                width=40)  # Decrease width for a longer input field

# Create an input frame to hold the input field and button
input_frame = ttk.Frame(window)
input_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create an input field with a watermark for encryption
entry = ttk.Entry(input_frame, justify="center", style="TEntry")
entry.insert(0, "Enter the text")
entry.bind("<FocusIn>", lambda event: entry.delete(0, "end"))  # Clear the watermark on focus
entry.pack(side="left", padx=5, pady=10)  # Increase padding

# Create a themed button to trigger encryption
encrypt_button = ttk.Button(input_frame, text="Encrypt", command=perform_encryption, style="TButton")
encrypt_button.pack(side="left", padx=10, pady=10)  # Increase padding for a slightly larger button

# Create a Text widget to display the output
output_text = tk.Text(window, wrap=tk.WORD, font=("Arial", 14), height=8)  # Increase font size and set height
output_text.pack(fill="both", expand=True, padx=20, pady=20)
output_text.config(state=tk.DISABLED)  # Make the Text widget read-only

# Create a label for the watermark
watermark_label = ttk.Label(window, text="Created by Denis Dimov", font=("Arial", 10), foreground="gray")
watermark_label.place(x=10, y=10)  # Adjust the position of the watermark label

# Start the GUI main loop
window.mainloop()
