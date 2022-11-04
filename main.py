from gerador import gera_senha
from tkinter import *
from webbrowser import open_new_tab



# Tela
master = Tk()
largura=400
altura=300
largura_tela=master.winfo_screenwidth()
altura_tela=master.winfo_screenheight()
x=(largura_tela/2) - (largura/2)
y=(altura_tela/2) - (altura/2)
master.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
master.title('Gerador de Senhas')
master.resizable(False, False)
label = Label(master, text='Gerador de Senhas')
img = PhotoImage(file='imagens/plano_de_fundo.png')
fundo = Label(master, image=img).place(relx=0.5, rely=0.5, anchor=CENTER)




#senha gerada
passw = StringVar()
passw.set('A senha gerada aparecerá aqui.')
senha_gerada = Label(master, textvariable=passw, background='black', font=20, foreground='white')
senha_gerada.place(relx=0.5, rely=0.5, anchor=CENTER , width=350, height=40)

# tamanho senha
label1 = Label(master, text='Tamanho da senha:', background='black', foreground='white').place(relx=0.4, rely=0.65, anchor=CENTER)
t = IntVar()
t.set(6)
tamanho = Spinbox(master, textvariable=t, from_=6, to_=32, width=3, state='readonly').place(relx=0.62, rely=0.65, anchor=CENTER)

#botoes
gerar = Button(master, text='Gerar Senha', fg='white', background='black', command=lambda: passw.set(gera_senha(t.get())), font='BOLD', activebackground='white', activeforeground='black', highlightthickness=2)
gerar.place(rely=0.8, relx=0.3, anchor=CENTER)
gerar.config(highlightbackground='black', highlightcolor='black')
copiar = Button(master, text='Copiar Senha', fg='white', background='black', command=lambda: [senha_gerada.clipboard_clear(), senha_gerada.clipboard_append(passw.get())], font='BOLD', highlightthickness=2)
copiar.place(rely=0.8, relx=0.7, anchor=CENTER)
copiar.config(highlightbackground='black', highlightcolor='black')

#creditos
creditos = Label(master, text='by: Elisson Douglas', foreground='white', font=('Arial', 12, 'underline'), background='black')
creditos.place(relx=0.5, rely=0.95, anchor=CENTER)
creditos.bind('<Button-1>', lambda x: open_new_tab('https://github.com/ElissonDouglas'))

master.mainloop()
