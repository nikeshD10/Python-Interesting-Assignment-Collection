import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("List")
root.geometry("400x400+300+300")
def insertitem(arg=None):
    listbox.insert(tk.END, content.get())
    entry.delete(0, END)
root.bind('<Return>', insertitem)
def deletelist(arg=None):
    listbox.delete(0, tk.END)
root.bind('<BackSpace>', deletelist)
def deleteselecteditem():
    listbox.delete(tk.ANCHOR)

label = tk.Label(root, text="Enter the any item")
label.pack()

button = tk.Button(root, text="Insert Item", command=insertitem)
button.pack()

button_delete = tk.Button(root, text="Delete List", command=deletelist)
button_delete.pack()

button_delete_selected = tk.Button(root, text="Delete Selected Item", command=deleteselecteditem)
button_delete_selected.pack()

content = tk.StringVar()
entry = tk.Entry(root, textvariable=content)
entry.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()
