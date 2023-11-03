import tkinter as tk

def realizar_calculo():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacion = operaciones_var.get()

        if operacion == 'Suma':
            resultado = num1 + num2
        elif operacion == 'Resta':
            resultado = num1 - num2
        elif operacion == 'Multiplicación':
            resultado = num1 * num2
        elif operacion == 'División':
            if num2 == 0:
                resultado = "No se puede dividir por cero."
            else:
                resultado = num1 / num2
        else:
            resultado = "Operación no válida"

        etiqueta_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Entradas de números
etiqueta_num1 = tk.Label(ventana, text="Número 1:")
etiqueta_num1.grid(row=0, column=0)
entrada_num1 = tk.Entry(ventana)
entrada_num1.grid(row=0, column=1)

etiqueta_num2 = tk.Label(ventana, text="Número 2:")
etiqueta_num2.grid(row=1, column=0)
entrada_num2 = tk.Entry(ventana)
entrada_num2.grid(row=1, column=1)

# Selector de operación
operaciones = ['Suma', 'Resta', 'Multiplicación', 'División']
operaciones_var = tk.StringVar()
operaciones_var.set(operaciones[0])
operaciones_desplegable = tk.OptionMenu(ventana, operaciones_var, *operaciones)
operaciones_desplegable.grid(row=2, column=0, columnspan=2)

# Botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular", command=realizar_calculo)
boton_calcular.grid(row=3, column=0, columnspan=2)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=4, column=0, columnspan=2)

ventana.mainloop()