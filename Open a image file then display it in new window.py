from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

window = Tk()

"""---------------------------Best Option is we pass all button which we are going to show in next window we pass those in file reading or opening file function------------"""
"""---------------------------Then the function we created as "opening" we pass in command of main window where button for opening file is created--------------------------"""
def open_img_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("png images", ".jpg"), ("all files", "*.*")))
    if not filename:
        return
    # setup new window
    new_window = Toplevel(window)
    # get image
    image = ImageTk.PhotoImage(Image.open(filename))
    # load image
    panel = Label(new_window, image=image)
    panel.image = image
    panel.pack()


window.title("Pattern Matching")
window.minsize(200, 200)
button = Button(text="Open file", width=10, height=10, command=open_img_file)
button.pack()

window.mainloop()

"""-------------------------------------------------------------OR---------------------------------------------------"""

"""from tkinter import *

def makeLabel(parent, image):
    # Make label to display the image
    label = Label(parent, image=image)
    label.pack()
    #------------------------------------------------Note: Below code also show how to use function inside function------------------------------------

def showImg():
    # Define root window!
    root = Tk()

    # Bring the image to the script!
    img = PhotoImage(file='YOUR_PIC.png')

    # Show image as label
    makeLabel(root, img)           #Here you can see

    # Update root (GUI)
    root.mainloop()

if __name__ == '__main__':
     showImg()"""