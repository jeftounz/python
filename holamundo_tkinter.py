import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi ventana")


def cambiar_texto():
    boton.config(text="¡Hola, mundo!")

boton = tk.Button(ventana, text="Presioname", command=cambiar_texto)
boton.pack()


ventana.mainloop()