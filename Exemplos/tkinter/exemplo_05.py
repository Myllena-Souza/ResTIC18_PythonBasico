import tkinter as tk
root = tk.Tk()   
root.title('Exemplo 05')
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT) # o botão de fechar ta do lado esquerdo
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES) # o botão expande junto com a pagina mas não preenche
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)  # o botão expande juntamente com a página    
tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)  # o botão so expande na direção X    
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES, fill=tk.Y)   # o botão expande na direção Y  
root.mainloop()