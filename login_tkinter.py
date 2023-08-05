import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta cuando se presiona el botón de inicio de sesión
def verificar_datos():
    correo = entrada_correo.get()
    contrasena = entrada_contrasena.get()
    if correo == "srjesusc@gmail.com" and contrasena == "admin":
        messagebox.showinfo("Login exitoso", "El login fue un éxito")

        # Ocultar la ventana de inicio de sesión
        ventana.withdraw()

        # Crear una nueva ventana
        nueva_ventana = tk.Toplevel()

        # Configurar la nueva ventana
        nueva_ventana.title("Comentarios")
        nueva_ventana.geometry("400x300")

        # Crear una caja de comentarios
        comentario_label = tk.Label(nueva_ventana, text="Escribe tu comentario:")
        comentario_label.pack(anchor="w", padx=20, pady=20)

        comentario_texto = tk.Text(nueva_ventana, height=10, width=40)
        comentario_texto.pack(anchor="w", padx=20)

        # Crear un botón para cerrar la sesión
        def cerrar_sesion():
            nueva_ventana.withdraw()
            ventana.deiconify()

        boton_cerrar_sesion = tk.Button(nueva_ventana, text="Cerrar sesión", command=cerrar_sesion)
        boton_cerrar_sesion.pack(side="right", padx=20, pady=20)

        # Mostrar la nueva ventana
        nueva_ventana.mainloop()
    else:
        messagebox.showwarning("Error en el login", "El correo o la contraseña ingresada no son correctos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Login")

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Establecer la geometría de la ventana
ventana.geometry("{}x{}".format(ancho_pantalla, alto_pantalla))

# Definir la función que se ejecuta cuando se presiona el botón de minimizar
def minimizar_ventana():
    ancho_ventana = int(ancho_pantalla * 0.3)
    alto_ventana = int(alto_pantalla * 0.3)
    ventana.geometry("{}x{}".format(ancho_ventana, alto_ventana))

# Configurar la acción para el botón de minimizar
ventana.protocol("WM_DELETE_WINDOW", minimizar_ventana)

# Etiquetas para indicar qué se debe ingresar en cada entrada
label_correo = tk.Label(ventana, text="Correo electrónico:")
label_correo.pack(anchor="center", pady=10)

# Entrada para el correo electrónico
entrada_correo = tk.Entry(ventana)
entrada_correo.pack(anchor="center", pady=10)

label_contrasena = tk.Label(ventana, text="Contraseña:")
label_contrasena.pack(anchor="center", pady=10)

# Entrada para la contraseña
entrada_contrasena = tk.Entry(ventana, show="*")
entrada_contrasena.pack(anchor="center", pady=10)

# Botón para verificar los datos ingresados
boton_verificar = tk.Button(ventana, text="Ingresar", command=verificar_datos)
boton_verificar.pack(anchor="center", pady=10)

# Configurar la acción para el botón de cerrar
def cerrar_programa():
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_programa)

ventana.mainloop()