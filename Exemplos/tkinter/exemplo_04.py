import sys
import tkinter as tk
root = tk.Tk()   
root.title('Exemplo 04')
widget = tk.Button(root, text='Hello widget world', command=sys.exit) # criou um botão que quando clicado fecha a janela 
widget.pack()
widget.mainloop()

