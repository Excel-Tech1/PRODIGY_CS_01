from tkinter import *
from tkinter import ttk

# Variables for both uppercase and lowercase letters
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

# Creates Tkinter window
root = Tk()
root.title('GUI Caesar Cipher')
root.resizable(True, True)

# Setting a background color for the entire window
root.configure(background='lightblue')

root.frame_header = ttk.Frame(root)
root.frame_header.grid(row=0, column=0)

# Style for labels (to apply background color)
label_style = {'bg': 'lightblue', 'fg': 'black', 'font': ('Arial', 12)}

# Header label for Caesar Cipher title
ttk.Label(root.frame_header, text='Caesar Cipher', style='Header.TLabel').grid(row=0, column=1)

# Labels with custom colors
Label(root.frame_header, text='Enter Number (1-25):', **label_style).grid(row=1, column=0, sticky='W')
Label(root.frame_header, text='Text:', **label_style).grid(row=2, column=0, sticky='W')
Label(root.frame_header, text='Encrypted/Decrypted Text:', **label_style).grid(row=4, column=0, sticky='W')

# Encrypted/Decrypted text field
enc_dec_text = ttk.Entry(root.frame_header, width=110)
enc_dec_text.grid(row=4, column=1)

# Cipher shift drop down with background color
cipher_shift_menu = StringVar()
Spinbox(root.frame_header, from_=1, to=25, textvariable=cipher_shift_menu, bg='white').grid(row=1, column=1)

# Text entry field with background color
text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2, column=1)

# Encryption function with case sensitivity
def encrypt_text():
    enc_dec_text.delete(0, END)  # Clear output field
    stringtoencrypt = text_entry.get()  # Keep case sensitivity intact
    ciphershift = int(cipher_shift_menu.get())  # Get cipher shift
    stringencrypted = ""
    
    for character in stringtoencrypt:
        if character in uppercase_letters:
            position = uppercase_letters.find(character)
            newposition = (position + ciphershift) % 26  # Wrap around the alphabet
            stringencrypted += uppercase_letters[newposition]
        elif character in lowercase_letters:
            position = lowercase_letters.find(character)
            newposition = (position + ciphershift) % 26  # Wrap around the alphabet
            stringencrypted += lowercase_letters[newposition]
        else:
            stringencrypted += character  # Preserve non-alphabetic characters

    enc_dec_text.insert(0, stringencrypted)  # Display result

# Decryption function with case sensitivity
def decrypt_text():
    enc_dec_text.delete(0, END)  # Clear output field
    stringtodecrypt = text_entry.get()  # Keep case sensitivity intact
    ciphershift = int(cipher_shift_menu.get())  # Get cipher shift
    stringdecrypted = ""
    
    for character in stringtodecrypt:
        if character in uppercase_letters:
            position = uppercase_letters.find(character)
            newposition = (position - ciphershift) % 26  # Wrap around the alphabet
            stringdecrypted += uppercase_letters[newposition]
        elif character in lowercase_letters:
            position = lowercase_letters.find(character)
            newposition = (position - ciphershift) % 26  # Wrap around the alphabet
            stringdecrypted += lowercase_letters[newposition]
        else:
            stringdecrypted += character  # Preserve non-alphabetic characters

    enc_dec_text.insert(0, stringdecrypted)  # Display result

# Function to close the application
def end_application():
    root.destroy()  # Close the application window

# Buttons with color
encrypt_button = Button(root.frame_header, text='Encrypt', command=encrypt_text, bg='green', fg='white', font=('Arial', 10))
encrypt_button.grid(row=3, column=0)

decrypt_button = Button(root.frame_header, text='Decrypt', command=decrypt_text, bg='red', fg='white', font=('Arial', 10))
decrypt_button.grid(row=3, column=1)

# End button to close the application
end_button = Button(root.frame_header, text='End', command=end_application, bg='black', fg='white', font=('Arial', 10))
end_button.grid(row=5, column=1)  # Place this below the Encrypt/Decrypt buttons

root.frame_header.pack(pady=20)  # Adding some padding to the top
root.mainloop()
