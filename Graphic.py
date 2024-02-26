import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from Logica import SyntaxAnalizer

def proccess():
    analizer = SyntaxAnalizer()
    entry = texto_entrada.get("1.0", tk.END)
    result = analizer.syntax_analyzer(entry)
    texto_salida.delete("1.0", tk.END)
    texto_salida.insert(tk.END, result)



ventana = tk.Tk()
ventana.title("Tabla")

ventana.geometry("800x600")

texto_entrada = ScrolledText(ventana, height=15)
texto_entrada.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

boton_procesar = tk.Button(ventana, text="Procesar", command=proccess)
boton_procesar.pack(pady=5)

texto_salida = ScrolledText(ventana, height=15)
texto_salida.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

ventana.mainloop()