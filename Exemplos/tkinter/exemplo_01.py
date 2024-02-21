from tkinter import Label       # importa um objeto widget específico (classe label é usada pra implementar textos em sua janela)
widget = Label(None, text='Olá Myllena!') # cria um widget
widget.pack()                   # organiza o widget na janela
widget.mainloop()               # inicia o loop de eventos