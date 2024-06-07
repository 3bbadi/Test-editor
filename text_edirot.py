import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                text_editor.delete(1.0, tk.END)
                text_editor.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text_editor.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")

# Set up the layout using a grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0, sticky="ns")

open_button = tk.Button(button_frame, text="Open", command=open_file)
open_button.pack(fill=tk.X, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(fill=tk.X, padx=5, pady=5)

# Create the text editor
text_editor = tk.Text(root)
text_editor.grid(row=0, column=1, sticky="nsew")

# Run the application
root.mainloop()
