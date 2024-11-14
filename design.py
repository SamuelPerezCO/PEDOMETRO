import tkinter as tk
import funciones
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("PEDOMETRO")
ventana.geometry("300x270")
ventana.config(bg="#e0f7fa")  # Color de fondo de la ventana

# Etiqueta principal
etiqueta = tk.Label(ventana, text="PEDOMETRO", bg="#006064", fg="white", font=("Arial", 14))
etiqueta.pack(pady=10)

# Frame para la etiqueta "Peos hoy" y el campo de entrada
frame_entrada_peos_hoy = tk.Frame(ventana, bg="#e0f7fa")  # Fondo del frame
frame_entrada_peos_hoy.pack(pady=5)

# Etiqueta "Peos hoy"
etiqueta_peos_hoy = tk.Label(frame_entrada_peos_hoy, text="Peos hoy:", bg="#e0f7fa", fg="#004d40" , font=("Arial", 14))
etiqueta_peos_hoy.pack(side="left")

# Campo de entrada
entrada_peos_hoy = tk.Entry(frame_entrada_peos_hoy, bg="white", fg="black")
entrada_peos_hoy.pack(side="right")

# Peos Semana
frame_entrada_peos_semana = tk.Frame(ventana, bg="#e0f7fa")
frame_entrada_peos_semana.pack(pady=5)

etiqueta_peos_semana = tk.Label(frame_entrada_peos_semana, text="Peos Semana:", bg="#e0f7fa", fg="#004d40" , font=("Arial", 14))
etiqueta_peos_semana.pack(side="left")

entrada_peos_semana = tk.Entry(frame_entrada_peos_semana, bg="white", fg="black")
entrada_peos_semana.pack(side="right")

# Peos Mes
frame_entrada_peos_mes = tk.Frame(ventana, bg="#e0f7fa")
frame_entrada_peos_mes.pack(pady=5)

etiqueta_peos_mes = tk.Label(frame_entrada_peos_mes, text="Peos mes:", bg="#e0f7fa", fg="#004d40" , font=("Arial", 14))
etiqueta_peos_mes.pack(side="left")

entrada_peos_mes = tk.Entry(frame_entrada_peos_mes, bg="white", fg="black")
entrada_peos_mes.pack(side="right")

# Peos Año
frame_entrada_peos_ano = tk.Frame(ventana, bg="#e0f7fa")
frame_entrada_peos_ano.pack(pady=5)

etiqueta_peos_ano = tk.Label(frame_entrada_peos_ano, text="Peos año:", bg="#e0f7fa", fg="#004d40" , font=("Arial", 14))
etiqueta_peos_ano.pack(side="left")

entrada_peos_ano = tk.Entry(frame_entrada_peos_ano, bg="white", fg="black")
entrada_peos_ano.pack(side="right")

# Botón
boton = tk.Button(ventana, text="¡ME TIRE UN PEDO!", bg="#00796b", fg="white", font=("Arial", 10, "bold"))
boton.pack(pady=20)

# Iniciar el bucle principal
ventana.mainloop()
