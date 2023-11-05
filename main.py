#You will create a desktop application with a Graphical User Interface (GUI)
# where you can upload an image and use Python to add a watermark logo/text.

import PIL.Image, PIL.ImageDraw, PIL.ImageFont
import os
from tkinter import *

def add_watermark():

    image_path = image_input.get()
    text = watermark_input.get()

    with PIL.Image.open("sample.png") as img:
        img.load()
        draw = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype("arial.ttf", 15)
        draw.text((10, 10), "hello", font=font)
        img.show()


window = Tk()
window.title("Watermark")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224)
canvas.grid(column=1, row=2)

image_input = Entry(width=50)
image_input.grid(column=2, row=1)

image_label = Label(text="Please input your file path here:")
image_label.grid(column=2, row=0)

watermark_input = Entry(width=50)
watermark_input.grid(column=0,row=1)

watermark_label = Label(text="Please chose your watermark text")
watermark_label.grid(column=0, row=0)

add_watermark = Button(text="Add watermark", command=add_watermark)
add_watermark.grid(column=1, row=2)

window.mainloop()