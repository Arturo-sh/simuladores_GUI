from tkinter import *
from PIL import ImageTk, Image
from random import randint

def cambia_img():
    numero1 = str(randint(1, 6))
    nombreImagen1 = "dado" + numero1 + ".png"
    imagen1 = Image.open(nombreImagen1)
    new_img1 = imagen1.resize((100, 100))
    render1 = ImageTk.PhotoImage(new_img1)
    label1 = Label(ventana, image=render1)
    label1.image = render1
    label1.place(x=20,y=40)

    numero2 = str(randint(1, 6))
    nombreImagen2 = "dado" + numero2 + ".png"
    imagen2 = Image.open(nombreImagen2)
    new_img2 = imagen2.resize((100, 100))
    render2 = ImageTk.PhotoImage(new_img2)
    label2 = Label(ventana, image=render2)
    label2.image = render2
    label2.place(x=130,y=40)

ventana = Tk()
ventana.title("Simulador de dado")
ventana.geometry("260x220")
ventana.resizable(False, False)

label = Label(ventana, text="Presione el botón para lanzar los dados")
label.pack()

imagenDefault1 = ImageTk.PhotoImage(Image.open("default.jpg").resize((100, 100)))
label1 = Label(ventana, image=imagenDefault1)
label1.place(x=20, y=40)

imagenDefault2 = ImageTk.PhotoImage(Image.open("default.jpg").resize((100, 100)))
label2 = Label(ventana, image=imagenDefault2)
label2.place(x=130, y=40)

btn = Button(ventana, command=cambia_img, width=6, height=1)
btn.config(text='lanzar')
btn.place(x=105, y=170)

ventana.mainloop()