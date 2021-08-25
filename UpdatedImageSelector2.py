from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.geometry("300x390")
root.title("Touch Paradise")
root.iconbitmap('C:/Users/dhaka/Downloads/Touch_Paradise.ico')

image_list = []
final_image_list = []
final_list = []
my_img_list = []
img_list = []
def addApp():
    global image_list
    global final_image_list
    global my_img_list
    global img_list
    global final_list
    filename = filedialog.askopenfilenames(initialdir="/Test1/Nikesh", title="Select file",
                                          filetypes=(("jpg images", ".jpg"), ("png images", ".png"), ("all files", "*.*")))
    """filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                          filetypes=(("png images", ".jpg"), ("all files", "*.*")))
    for widget in my_img.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.jpg"), ("*allfiles", "*.*")))"""
    image_list.append(filename)
    for i in image_list:
        for x in i:
            final_image_list.append(x)

    if not filename:
        return

    new_window = Toplevel(root)
    new_window.geometry("300x390")
    new_window.title("Image Viewer")
    new_window.iconbitmap('C:/Users/dhaka/Downloads/Touch_Paradise.ico')

    """for list in image_list:
        # The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
        # Widgets are standard graphical user interface (GUI) elements, like different kinds of buttons and menus.
        label = Label(list, text=list, bg="gray")
        label.pack()"""


    # image_list = ["Nikesh/1.jpg", "Nikesh/2.jpg", "Nikesh/3.jpg", "Nikesh/4.jpg"]
    num = len(final_image_list) + 1
    loop = True
    while loop == True:

        for i in range(1, num):
            my_img = "my_img" + str(i)
            my_img_list.append(my_img)
        break

    while loop == True:
        for x in range(1, num):
            img = "img_" + str(x)
            img_list.append(img)
        break


    while loop == True:

        for (i, x, z) in zip(my_img_list, img_list, final_image_list):
            size = (300, 250)
            i = Image.open(z, "r")
            # here the r represent the read and the syntax of the open the file is " var = Image.open(filename, "r") "
            # i = Image.open("'%s'" % term)
            resize = i.resize(size)
            x = ImageTk.PhotoImage(resize)
            final_list.append(x)
            """my_img_list[i] = Image.open(image_list[z])
            resize = my_img_list[i].resize(size)
            img_list[x] = ImageTk.PhotoImage(resize)"""
        break
    my_img = Label(new_window, image=final_list[0])
    my_img.grid(row=0, column=0, columnspan=3, pady=30)

    def forward(img_num):
        global my_img
        global image_list
        global button_forward
        global button_back
        global final_list

        my_img.grid_forget()

        my_img = Label(new_window, image=final_list[img_num - 1])
        my_img.grid(row=0, column=0, columnspan=3, pady=30)

        button_forward = Button(new_window, text=">>", command=lambda: forward(img_num + 1))
        button_forward.grid(row=1, column=2)

        button_back = Button(new_window, text="<<", command=lambda: back(img_num - 1))
        button_back.grid(row=1, column=0)

        if img_num == len(image_list):
            button_forward = Button(new_window, text=">>", state=DISABLED)
            button_forward.grid(row=1, column=2)

    def back(img_num):
        global my_img
        global image_list
        global button_forward
        global button_back
        global final_list

        my_img.grid_forget()

        my_img = Label(new_window, image=final_list[img_num - 1])
        my_img.grid(row=0, column=0, columnspan=3, pady=30)

        button_forward = Button(new_window, text=">>", command=lambda: forward(img_num + 1))
        button_forward.grid(row=1, column=2)

        button_back = Button(new_window, text="<<", command=lambda: back(img_num - 1))
        button_back.grid(row=1, column=0)

        if img_num == 1:
            button_back = Button(new_window, text="<<", state=DISABLED)
            button_back.grid(row=1, column=0)

    button_forward = Button(new_window, text=">>", command=lambda: forward(2))

    button_back = Button(new_window, text="<<", command=back, state=DISABLED)

    button_exit = Button(new_window, text="Exit", command=root.quit)

    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)

size = (300, 350)
my_frame = Image.open("Nikesh/Welcome2.png")
resize = my_frame.resize(size)
final_frame = ImageTk.PhotoImage(resize)

my_label = Label(root, image=final_frame)
my_label.grid(row=0, column=0, columnspan=3)

openfile = Button(root, text="Open File", padx=20, pady=1, fg="white", bg="#263D42", bd=9,  relief=SUNKEN, command=addApp)
openfile.grid(row=1, column=0, columnspan=3, sticky=W+E)

root.mainloop()


