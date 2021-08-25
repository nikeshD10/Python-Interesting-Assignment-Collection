from tkinter import *
from PIL import ImageTk, Image
import urllib


root = Tk()
root.geometry("300x350")
root.title("Touch Paradise")
root.iconbitmap('C:/Users/dhaka/Downloads/Touch_Paradise.ico')


image_list = ["Nikesh/1.jpg", "Nikesh/2.jpg", "Nikesh/3.jpg", "Nikesh/4.jpg"]
num = len(image_list)+1
my_img_list = []
img_list = []
loop = True
while loop == True:
    for i in range(1, num):
        my_img = "my_img"+str(i)
        my_img_list.append(my_img)
    break

while loop == True:
    for x in range(1, num):
        img = "img_"+str(x)
        img_list.append(img)
    break

final_list = []
while loop== True:
    for (i, x, z) in zip(my_img_list, img_list, image_list):

        size = (300, 250)
        i = Image.open(z, "r")
        # here the r represent the read and the syntax of the open the file is " var = Image.open(filename, "r") "
        #i = Image.open("'%s'" % term)
        resize = i.resize(size)
        x = ImageTk.PhotoImage(resize)
        final_list.append(x)
        """my_img_list[i] = Image.open(image_list[z])
        resize = my_img_list[i].resize(size)
        img_list[x] = ImageTk.PhotoImage(resize)"""
    break

my_img = Label(root, image=final_list[0])
my_img.grid(row=0, column=0, columnspan=3, pady=30)


def forward(img_num):
    global my_img
    global image_list
    global button_forward
    global button_back
    my_img.grid_forget()
    my_img = Label(root, image=final_list[img_num - 1])
    my_img.grid(row=0, column=0, columnspan=3, pady=30)
    button_forward = Button(root, text=">>", command=lambda: forward(img_num + 1))
    button_forward.grid(row=1, column=2)

    button_back = Button(root, text="<<", command=lambda: back(img_num - 1))
    button_back.grid(row=1, column=0)

    if img_num == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
        button_forward.grid(row=1, column=2)


def back(img_num):
    global my_img
    global image_list
    global button_forward
    global button_back
    my_img.grid_forget()
    my_img = Label(root, image=final_list[img_num - 1])
    my_img.grid(row=0, column=0, columnspan=3, pady=30)
    button_forward = Button(root, text=">>", command=lambda: forward(img_num + 1))
    button_forward.grid(row=1, column=2)

    button_back = Button(root, text="<<", command=lambda: back(img_num - 1))
    button_back.grid(row=1, column=0)

    if img_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)
        button_back.grid(row=1, column=0)


button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back = Button(root, text="<<", command=back, state=DISABLED)

button_exit = Button(root, text="Exit", command=root.quit)

button_forward.grid(row=1, column=2)
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)

root.mainloop()
