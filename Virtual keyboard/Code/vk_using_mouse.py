import tkinter as tk
from tkinter import ttk

def key_press(event):
    """Function to handle key press event"""
    key = event.widget.cget("text")
    if key == "Quit":
        root.quit()
    else:
        print(f"Key pressed: {key}")

root = tk.Tk()
root.title("Virtual Keyboard")

# Create a frame for the keyboard
keyboard_frame = ttk.Frame(root)
keyboard_frame.grid(row=0, column=0, padx=10, pady=10)

# Define the keys on the keyboard
keys = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M"],
    ["Quit"]
]

# Create the keys on the keyboard frame
for i, row in enumerate(keys):
    for j, key in enumerate(row):
        key_button = ttk.Button(keyboard_frame, text=key, width=5)
        key_button.grid(row=i, column=j, padx=3, pady=3)
        key_button.bind("<Button-1>", key_press)

root.mainloop()
