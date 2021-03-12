from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image


root=Tk()
root.geometry("450x500")
root.title("Image Converter")


def png():
    filename=fd.askopenfilename()
    file_path = filename.split("/")
    file = file_path.pop(-1)
    Image.open(filename).save(f"{'/'.join(file_path)}/{file.split('.')[0]}.png")

def jpg():
    filename=fd.askopenfilename()
    file_path = filename.split("/")
    file = file_path.pop(-1)
    Image.open(filename).save(f"{'/'.join(file_path)}/{file.split('.')[0]}.jpg")

def jpeg():
    filename=fd.askopenfilename()
    file_path = filename.split("/")
    file = file_path.pop(-1)
    Image.open(filename).save(f"{'/'.join(file_path)}/{file.split('.')[0]}.jpeg")

def gif():
    filename=fd.askopenfilename()
    file_path = filename.split("/")
    file = file_path.pop(-1)
    Image.open(filename).save(f"{'/'.join(file_path)}/{file.split('.')[0]}.gif")

def webp():
    filename=fd.askopenfilename()
    file_path = filename.split("/")
    file = file_path.pop(-1)
    Image.open(filename).save(f"{'/'.join(file_path)}/{file.split('.')[0]}.webp")

def tiff():
    filename=fd.askopenfilename()
    file_path = filename.split("/")
    file = file_path.pop(-1)
    Image.open(filename).save(f"{'/'.join(file_path)}/{file.split('.')[0]}.tiff")

def pdf():
    filename=fd.askopenfilename()
    file_path = filename.split("/")
    file = file_path.pop(-1)
    Image.open(filename).save(f"{'/'.join(file_path)}/{file.split('.')[0]}.pdf")

Label_1=Label(root,text="Find your format and convert!", width=50, font=("bold",15))
Label_1.place(x=-50,y=50)

Button(root,text="PNG", width=20, height=2, bg="brown",fg="white",command=png).place(x=150,y=100)
Button(root,text="JPG", width=20, height=2, bg="brown",fg="white", command=jpg).place(x=150,y=150)
Button(root,text="JPEG", width=20, height=2, bg="brown",fg="white", command=jpeg).place(x=150,y=200)
Button(root,text="GIF", width=20, height=2, bg="brown",fg="white", command=gif).place(x=150,y=250)
Button(root,text="WEBP", width=20, height=2, bg="brown",fg="white", command=webp).place(x=150,y=300)
Button(root,text="TIFF", width=20, height=2, bg="brown",fg="white", command=tiff).place(x=150,y=350)
Button(root,text="PDF", width=20, height=2, bg="brown",fg="white", command=pdf).place(x=150,y=400)

root.mainloop()