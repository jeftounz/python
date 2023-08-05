import tkinter as tk

ventana = tk.Tk()
ventana.title("Ingreso de datos")

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Establecer la geometría de la ventana
ventana.geometry("{}x{}".format(ancho_pantalla, alto_pantalla))

# Función que se ejecuta cuando se presiona el botón
def mostrar_datos():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    cedula = entrada_cedula.get()
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Cédula:", cedula)

# Etiquetas para indicar qué se debe ingresar en cada entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()

# Entrada para el nombre
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack()

# Entrada para el apellido
entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack()

label_cedula = tk.Label(ventana, text="Cédula:")
label_cedula.pack()

# Entrada para la cédula
entrada_cedula = tk.Entry(ventana)
entrada_cedula.pack()

# Botón para mostrar los datos ingresados
boton_mostrar = tk.Button(ventana, text="Mostrar datos", command=mostrar_datos)
boton_mostrar.pack()

ventana.mainloop()