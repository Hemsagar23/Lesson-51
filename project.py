import tkinter as tk
from tkinter import filedialog, scrolledtext

def open_file():
    global text_data
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as f:
        text_data = f.read()
    output.delete(1.0, tk.END)
    output.insert(tk.END, "File loaded successfully!")

def count_words():
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Total words: {len(text_data.split())}")

def count_lines():
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Total lines: {len(text_data.splitlines())}")

def uppercase():
    output.delete(1.0, tk.END)
    output.insert(tk.END, text_data.upper())

def reverse():
    output.delete(1.0, tk.END)
    output.insert(tk.END, text_data[::-1])

def find_word():
    word = entry.get()
    count = text_data.lower().count(word.lower())
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"'{word}' appears {count} times")

root = tk.Tk()
root.title("File Operations App")

tk.Button(root, text="Open File", command=open_file).pack()

tk.Button(root, text="Count Words", command=count_words).pack()
tk.Button(root, text="Count Lines", command=count_lines).pack()
tk.Button(root, text="Uppercase", command=uppercase).pack()
tk.Button(root, text="Reverse Text", command=reverse).pack()

entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Find Word", command=find_word).pack()

output = scrolledtext.ScrolledText(root, width=60, height=15)
output.pack()

root.mainloop()
