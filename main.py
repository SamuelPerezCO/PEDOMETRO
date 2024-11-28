import tkinter as tk
from db_manager import *
from datetime import datetime, timedelta

# Inicializar la base de datos
inicializar_bd()

# Obtener el usuario conectado
usuario_actual = obtener_usuario_actual()

# Obtener los peo_contadores iniciales desde la base de datos
datos = obtener_peo_contadores()
contador_peos_hoy = datos['peos_dia'] if datos else 0
contador_peos_semana = datos['peos_semana'] if datos else 0
contador_peos_mes = datos['peos_mes'] if datos else 0
contador_peos_ano = datos['peos_ano'] if datos else 0

def contar_peo():
    """
    Incrementa los contadores de "peos" y actualiza la interfaz gráfica con los nuevos valores.
    
    Esta función incrementa los valores de los contadores de peos en el día, semana, mes y año. 
    Después de incrementar los contadores, los nuevos valores se muestran en la interfaz gráfica 
    y se guardan en la base de datos.
    """

    verificar_y_actualizar_contadores()
    
    global contador_peos_hoy, contador_peos_semana, contador_peos_mes, contador_peos_ano

    # Incrementa los peo_contadores
    contador_peos_hoy += 1
    contador_peos_semana += 1
    contador_peos_mes += 1
    contador_peos_ano += 1

    # Actualizar los campos en la interfaz
    entrada_peos_hoy.delete(0, tk.END)
    entrada_peos_hoy.insert(0, str(contador_peos_hoy))

    entrada_peos_semana.delete(0, tk.END)
    entrada_peos_semana.insert(0, str(contador_peos_semana))

    entrada_peos_mes.delete(0, tk.END)
    entrada_peos_mes.insert(0, str(contador_peos_mes))

    entrada_peos_ano.delete(0, tk.END)
    entrada_peos_ano.insert(0, str(contador_peos_ano))

    # Guardar los nuevos peo_contadores en la base de datos
    actualizar_peo_contadores(contador_peos_hoy, contador_peos_semana, contador_peos_mes, contador_peos_ano)

def verificar_y_actualizar_contadores():
    global contador_peos_hoy, contador_peos_semana, contador_peos_mes, contador_peos_ano

    # Obtener la fecha actual y la última actualización
    fecha_actual = datetime.now().date()
    ultima_actualizacion = obtener_ultima_actualizacion()

    if not ultima_actualizacion:
        actualizar_fecha_actualizacion(fecha_actual)
        return

    # Verifica si ha pasado un día
    if fecha_actual > ultima_actualizacion:
        contador_peos_semana += contador_peos_hoy
        contador_peos_hoy = 0

        # Verifica si ha pasado una semana (asumiendo inicio lunes)
        if fecha_actual.isocalendar()[1] > ultima_actualizacion.isocalendar()[1]:
            contador_peos_mes += contador_peos_semana
            contador_peos_semana = 0

        # Verifica si ha pasado un mes
        if fecha_actual.month > ultima_actualizacion.month or fecha_actual.year > ultima_actualizacion.year:
            contador_peos_ano += contador_peos_mes
            contador_peos_mes = 0

        # Actualiza la fecha en la base de datos
        actualizar_fecha_actualizacion(fecha_actual)

        # Guarda los contadores actualizados
        actualizar_peo_contadores(contador_peos_hoy, contador_peos_semana, contador_peos_mes, contador_peos_ano)


# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("PEDOMETRO")
ventana.geometry("300x300")
ventana.config(bg="#e0f7fa")  # Color de fondo de la ventana

# Mostrar el usuario conectado en la interfaz
etiqueta_usuario = tk.Label(
    ventana,
    text=f"Conectado como: {usuario_actual}",
    bg="#e0f7fa",
    fg="#004d40",
    font=("Arial", 10)
)
etiqueta_usuario.pack(pady=5)

# Etiqueta principal
etiqueta = tk.Label(ventana, text="PEDOMETRO", bg="#006064", fg="white", font=("Arial", 14))
etiqueta.pack(pady=10)

# Frame para la etiqueta "Peos hoy" y el campo de entrada
frame_entrada_peos_hoy = tk.Frame(ventana, bg="#e0f7fa")  
frame_entrada_peos_hoy.pack(pady=5)

etiqueta_peos_hoy = tk.Label(frame_entrada_peos_hoy, text="Peos hoy:", bg="#e0f7fa", fg="#004d40", font=("Arial", 14))
etiqueta_peos_hoy.pack(side="left")

entrada_peos_hoy = tk.Entry(frame_entrada_peos_hoy, bg="white", fg="black")
entrada_peos_hoy.pack(side="right")
entrada_peos_hoy.insert(0, str(contador_peos_hoy))

# Peos Semana
frame_entrada_peos_semana = tk.Frame(ventana, bg="#e0f7fa")
frame_entrada_peos_semana.pack(pady=5)

etiqueta_peos_semana = tk.Label(frame_entrada_peos_semana, text="Peos Semana:", bg="#e0f7fa", fg="#004d40", font=("Arial", 14))
etiqueta_peos_semana.pack(side="left")

entrada_peos_semana = tk.Entry(frame_entrada_peos_semana, bg="white", fg="black")
entrada_peos_semana.pack(side="right")
entrada_peos_semana.insert(0, str(contador_peos_semana))

# Peos Mes
frame_entrada_peos_mes = tk.Frame(ventana, bg="#e0f7fa")
frame_entrada_peos_mes.pack(pady=5)

etiqueta_peos_mes = tk.Label(frame_entrada_peos_mes, text="Peos mes:", bg="#e0f7fa", fg="#004d40", font=("Arial", 14))
etiqueta_peos_mes.pack(side="left")

entrada_peos_mes = tk.Entry(frame_entrada_peos_mes, bg="white", fg="black")
entrada_peos_mes.pack(side="right")
entrada_peos_mes.insert(0, str(contador_peos_mes))

# Peos Año
frame_entrada_peos_ano = tk.Frame(ventana, bg="#e0f7fa")
frame_entrada_peos_ano.pack(pady=5)

etiqueta_peos_ano = tk.Label(frame_entrada_peos_ano, text="Peos año:", bg="#e0f7fa", fg="#004d40", font=("Arial", 14))
etiqueta_peos_ano.pack(side="left")

entrada_peos_ano = tk.Entry(frame_entrada_peos_ano, bg="white", fg="black")
entrada_peos_ano.pack(side="right")
entrada_peos_ano.insert(0, str(contador_peos_ano))

# Botón para incrementar el contador
boton = tk.Button(
    ventana,
    text="¡ME TIRÉ UN PEDO!",
    bg="#00796b",
    fg="white",
    font=("Arial", 10, "bold"),
    command=contar_peo
)
boton.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
