import tkinter as tk       
root = tk.Tk()                             # cria uma janela
root.title('Exemplo 02')          #pedindo para renomear a janela      # configura o título da janela
widget = tk.Label(root)                    # cria um widget dentro da janela
widget.config(text='Hello GUI world!')  # configura o texto do widget (config permite que mude o visual instantaneamente)
widget.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)  # organiza o widget na janela
# o side diz onde o objeto deve ta na janela (sites geralmente usa TOP que é no topo da janela)
root.mainloop()               # inicia o loop de eventos