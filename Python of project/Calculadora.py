import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Expresión inválida")
    else:
        entry_var.set(entry_var.get() + button_text)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")
root.resizable(False, False)

# Variable para mostrar los números ingresados
entry_var = tk.StringVar()

# Campo de entrada
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right", bd=10)
entry.pack(fill="both", padx=10, pady=10)

# Definir botones
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Crear la cuadrícula de botones
for row_values in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for value in row_values:
        button = tk.Button(frame, text=value, font=("Arial", 18), command=lambda v=value: on_click(v))
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()

# En este script, hemos creado una calculadora simple con una interfaz de usuario gráfica utilizando la biblioteca Tkinter. La calculadora tiene un campo de entrada donde se pueden ingresar los números y operadores. Los botones numéricos y de operadores se utilizan para ingresar los números y operadores en el campo de entrada. 
# Cuando se hace clic en el botón “C”, se borra el contenido del campo de entrada. Cuando se hace clic en el botón “=”, se evalua la expresión matemática ingresada en el campo de entrada y se muestra el resultado. 
# Ejecutar el script de la calculadora 
# Para ejecutar el script de la calculadora, simplemente guarde el código en un archivo con extensión .py y ejecútelo utilizando el comando python. 
# python calculadora.py
# Cuando ejecute el script, verá una ventana de la calculadora con botones numéricos y de operadores. Puede hacer clic en los botones para ingresar números y operadores en el campo de entrada y realizar cálculos matemáticos. 
# Conclusión 
# En este artículo, hemos discutido cómo crear una calculadora simple con una interfaz de usuario gráfica utilizando la biblioteca Tkinter en Python. Hemos creado una calculadora con un campo de entrada y botones numéricos y de operadores para ingresar números y operadores. 
# Si desea aprender más sobre la biblioteca Tkinter, consulte la documentación oficial de Tkinter en  https://docs.python.org/3/library/tkinter.html. 
