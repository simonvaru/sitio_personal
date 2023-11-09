import tkinter as tk
from tkinter import filedialog 
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="white")


pen_color = "black"
pen_size = 5
file_path = ""


# FUNCTIONS###########################
def add_image():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="..\ejercicios_varios_3")
    image = Image.open(file_path)
    # x=(image.height/100)*40
    # x=int(x)
    width, height = int(image.width*0.4), int(image.height*0.4)
    # width, height=int(image.width/2), int(image.height/2)
    image = image.resize((width, height), Image.ANTIALIAS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(400, 300, image=image, anchor="center")


def change_color_pen():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


def draw_pen(event):
    x1, y1 = (event.x-pen_size), (event.y-pen_size)
    x2, y2 = (event.x+pen_size), (event.y+pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')


def change_size_pen(size):
    global pen_size
    pen_size.select = size


def clear_canvas():
    canvas.delete("all")
    canvas.create_image(400, 300, image=canvas.image, anchor="center")


def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width*0.4), int(image.height*0.4)
    image = image.resize((width, height), Image.ANTIALIAS)
    canvas.config(width=image.width, height=image.height)
    if filter == "Black & White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(400, 300, image=image, anchor="center")


# FRAMES###########################
left_frame = tk.Frame(root, width=200, height=600, bg="gray")
left_frame.pack(side="left", fill="y")

left_top_frame = tk.Frame(left_frame, width=200, height=100, bg="#878E61")
left_top_frame.pack(side="top", fill="x")

left_top_frame_2 = tk.Frame(left_frame, width=200, height=100, bg="#CED5A7")
left_top_frame_2.pack(side="top", fill="x")

left_top_frame_3 = tk.Frame(left_frame, width=200, height=100, bg="#878E61")
left_top_frame_3.pack(side="top", fill="x")

left_top_frame_4 = tk.Frame(left_frame, width=200, height=100, bg="#CED5A7")
left_top_frame_4.pack(side="top", fill="x")

left_top_frame_5 = tk.Frame(left_frame, width=200, height=100, bg="#878E61")
left_top_frame_5.pack(side="top", fill="x")

left_top_frame_6 = tk.Frame(left_frame, width=200, height=100, bg="#CED5A7")
left_top_frame_6.pack(side="top", fill="x")

# BUTTONS###########################
image_button = tk.Button(left_top_frame, text="Add Image",
                         command=add_image, bg="white")
image_button.pack(pady=38, padx=10)


color_button = tk.Button(
    left_top_frame_2, text="Change Pen Color", command=change_color_pen, bg="white")
color_button.pack(pady=38, padx=10)


pen_size_frame = tk.Frame(left_top_frame_3, bg="white")
pen_size_frame.pack(pady=38, padx=10)


pen_size_1 = tk.Radiobutton(pen_size_frame, text="Small",
                            value=3, command=lambda: change_size_pen(3), bg="white")
pen_size_1.pack(side="left")


pen_size_2 = tk.Radiobutton(pen_size_frame, text="Medium",
                            value=5, command=lambda: change_size_pen(5), bg="white")
pen_size_2.pack(side="left")


pen_size_3 = tk.Radiobutton(pen_size_frame, text="Big",
                            value=7, command=lambda: change_size_pen(7), bg="white")
pen_size_3.pack(side="left")


clear_button = tk.Button(left_top_frame_4, text="Clear Screen",
                         command=clear_canvas, bg="#FF9797").pack(pady=38, padx=10)


filter_label = tk.Label(left_top_frame_5, text="Select Filter", bg="white")
filter_label.pack(pady=10, padx=10)
filter_combobox = ttk.Combobox(left_top_frame_5, values=[
                               "Black & White", "Blur", "Emboss", "Sharpen", "Smooth"])
filter_combobox.pack(pady=10, padx=10)
filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_filter(filter_combobox.get()))


# CANVAS##########################
canvas = tk.Canvas(root, width=750, height=500)
canvas.pack(fill="both", expand=True)

canvas.bind("<B1-Motion>", draw_pen)  # drawing pen activation

root.mainloop()
