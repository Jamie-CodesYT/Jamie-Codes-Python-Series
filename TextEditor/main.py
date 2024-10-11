import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.filedialog import SaveFileDialog

def main():
    window = Tk()
    window.title("Text Editor")
    window.geometry("720x360")

    text_edit = Text(window, font="Arial 18")
    text_edit.grid(row=0, column=1)
    wrap = tk.WORD
    text_edit.pack()
    menu = Menu(window)
    window.config(menu=menu)

    fileMenu = Menu(menu)
    menu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Save File", command = lambda: savefileas(window, text_edit))
    fileMenu.add_command(label="Open File", command = lambda: openfile(window, text_edit))

    window.bind("<Control-s>", lambda x: savefileas(window, text_edit))
    window.bind("<Control-o>", lambda y: openfile(window, text_edit))

    window.mainloop()

def savefileas(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    

    with open(filepath, "w") as file:
        file_content = text_edit.get(1.0, tk.END)
        file.write(file_content)
    window.title(f"Editing file:  {filepath}")

def openfile(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as file:
        file_content = file.read()
        text_edit.insert(tk.END, file_content)
    window.title(f"Editing file: {filepath}")



main()