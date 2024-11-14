import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("PEDOMETRO")
ventana.geometry("300x270")

# Etiqueta principal
etiqueta = tk.Label(ventana, text="PEDOMETRO")
etiqueta.pack(pady=10)

# Frame para la etiqueta "Pasos hoy" y el campo de entrada
frame_entrada_peos_hoy = tk.Frame(ventana)
frame_entrada_peos_hoy.pack(pady=5)

# Etiqueta "Pasos hoy"
etiqueta_peos_hoy = tk.Label(frame_entrada_peos_hoy, text="Peos hoy:")
etiqueta_peos_hoy.pack(side="left")

# Campo de entrada
entrada_peos_hoy = tk.Entry(frame_entrada_peos_hoy)
entrada_peos_hoy.pack(side="right")

#Peos Semana

#Frame para la etiqueta "Peos Semana" y el campo de entrada
frame_entrada_peos_semana = tk.Frame(ventana)
frame_entrada_peos_semana.pack(pady=5)

etiqueta_peos_semana = tk.Label(frame_entrada_peos_semana, text="Peos Semana:")
etiqueta_peos_semana.pack(side="left")

entrada_peos_semana = tk.Entry(frame_entrada_peos_semana)
entrada_peos_semana.pack(side="right")

#Peos Mes

#Frame para la etiqueta "Peos Mes" y el campo de entrada
frame_entrada_peos_mes = tk.Frame(ventana)
frame_entrada_peos_mes.pack(pady=5)

etiqueta_peos_mes = tk.Label(frame_entrada_peos_mes , text = "Peos mes:")
etiqueta_peos_mes.pack(side="left")

entrada_peos_mes = tk.Entry(frame_entrada_peos_mes)
entrada_peos_mes.pack(side="right")

#Peos Año
frame_entrada_peos_ano = tk.Frame(ventana)
frame_entrada_peos_ano.pack(pady=5)

etiqueta_peos_ano = tk.Label(frame_entrada_peos_ano , text="Peos año")
etiqueta_peos_ano.pack(side="left")

entrada_peos_ano = tk.Entry(frame_entrada_peos_ano)
entrada_peos_ano.pack(side="right")

boton = tk.Button(ventana , text="¡ME TIRE UN PEDO!")
boton.pack(pady=20)


# Iniciar el bucle principal
ventana.mainloop()
