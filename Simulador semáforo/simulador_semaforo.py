from tkinter import Tk, Label, Button
from PIL import ImageTk, Image
from time import sleep
import threading

def inicio():
    btn["state"] = "disabled"
    thread = threading.Thread(target=luzRoja)
    thread.start()

def contador(segundos):
    for i in range (segundos):
        tiempo.config(text=f"Segundos: {i + 1}")
        sleep(1)

def luzVerde():
    imgAmarillo = ImageTk.PhotoImage(Image.open(r"imagenes\amarillo0.png").resize((100, 100)))
    label2 = Label(ventana, image=imgAmarillo)
    label2.image = imgAmarillo
    label2.place(x=80,y=130)

    imgVerde = ImageTk.PhotoImage(Image.open(r"imagenes\verde1.png").resize((100, 100)))
    label3 = Label(ventana, image=imgVerde)
    label3.image = imgVerde
    label3.place(x=80,y=230)
    contador(27)
    thread3 = threading.Thread(target=luzRoja)
    thread3.start()

def luzAmarilla():
    imgRojo = ImageTk.PhotoImage(Image.open(r"imagenes\rojo0.png").resize((100, 100)))
    label1 = Label(ventana, image=imgRojo)
    label1.image = imgRojo
    label1.place(x=80,y=30)

    imgAmarillo = ImageTk.PhotoImage(Image.open(r"imagenes\amarillo1.png").resize((100, 100)))
    label2 = Label(ventana, image=imgAmarillo)
    label2.image = imgAmarillo
    label2.place(x=80,y=130)
    contador(3)
    thread2 = threading.Thread(target=luzVerde)
    thread2.start()

def luzRoja():
    imgVerde = ImageTk.PhotoImage(Image.open(r"imagenes\verde0.png").resize((100, 100)))
    label3 = Label(ventana, image=imgVerde)
    label3.image = imgVerde
    label3.place(x=80,y=230)

    imgRojo = ImageTk.PhotoImage(Image.open(r"imagenes\rojo1.png").resize((100, 100)))
    label1 = Label(ventana, image=imgRojo)
    label1.image = imgRojo
    label1.place(x=80,y=30)
    contador(30)
    thread1 = threading.Thread(target=luzAmarilla)
    thread1.start()

ventana = Tk()
ventana.title("Simulador de semáforo")
ventana.geometry("260x380")
ventana.resizable(False, False)

tiempo = Label(ventana, text="Segundos: 0")
tiempo.pack()

rojo = ImageTk.PhotoImage(Image.open(r"imagenes\rojo0.png").resize((100, 100)))
labelRojo = Label(ventana, image=rojo)
labelRojo.place(x=80, y=30)

amarillo = ImageTk.PhotoImage(Image.open(r"imagenes\amarillo0.png").resize((100, 100)))
labelAmarillo = Label(ventana, image=amarillo)
labelAmarillo.place(x=80, y=130)

verde = ImageTk.PhotoImage(Image.open(r"imagenes\verde0.png").resize((100, 100)))
labeluzVerde = Label(ventana, image=verde)
labeluzVerde.place(x=80, y=230)

btn = Button(ventana, command = inicio, width = 8, height = 1)
btn.config(text='Comenzar')
btn.place(x=98, y=340)

ventana.mainloop()