from tkinter import *
from PIL import ImageTk, Image
from random import randint

def cambia_img():
    numero = str(randint(1, 43))
    nombreImagen = "logo" + numero + ".jpg"
    imagen = Image.open(nombreImagen)
    new_img = imagen.resize((100, 100))
    render = ImageTk.PhotoImage(new_img)
    label = Label(ventana, image=render)
    label.image = render
    label.place(x=80,y=40)

ventana = Tk()
ventana.title("Simulador de autos")
ventana.geometry("260x220")
ventana.resizable(False, False)

label = Label(ventana, text="Presione el botón para empezar")
label.pack()

imagenDefault = ImageTk.PhotoImage(Image.open("logo21.jpg").resize((100, 100)))
label = Label(ventana, image=imagenDefault)
label.place(x=80, y=40)

btn = Button(ventana, command=cambia_img, width=8, height=1)
btn.config(text='Presionar')
btn.place(x=100, y=170)

ventana.mainloop()