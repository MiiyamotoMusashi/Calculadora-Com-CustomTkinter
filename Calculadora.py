import customtkinter as ct
from PIL import Image, ImageTk

# Função que carrega imagem e altera o tamanho dela
def resize(imagem, tamanho):
    novaImagem = imagem.resize(tamanho)
    return ImageTk.PhotoImage(novaImagem)

# Mudando o tema para 'dark'
ct.set_appearance_mode('dark')

# Algumas funções de botões
class funções:
    def btn0():
        numeros.insert('end', 0)
    def btn1():
        numeros.insert('end', 1)
    def btn2():
        numeros.insert('end', 2)
    def btn3():
        numeros.insert('end', 3)
    def btn4():
        numeros.insert('end', 4)
    def btn5():
        numeros.insert('end', 5)
    def btn6():
        numeros.insert('end', 6)
    def btn7():
        numeros.insert('end', 7)
    def btn8():
        numeros.insert('end', 8)
    def btn9():
        numeros.insert('end', 9)
    def soma():
        numeros.insert('end', '+')
    def menos():
        numeros.insert('end', '-')
    def multipli():
        numeros.insert('end', '*')
    def divisão():
        numeros.insert('end', '/')
    def virgula():
        numeros.insert('end', '.')
    def apaga():
        numeros.delete('end-2c', 'end')
    class parenteses:
        def E():
            numeros.insert('end', '(')
        def D():
            numeros.insert('end', ')')

# Função que apaga os números
def clear_input():
    numeros.delete('0.0', 'end')

# Função de calcular
def calcular():
    try:
        calculo = numeros.get('0.0', 'end')
        resultado = eval(calculo)
        numeros.delete('0.0', 'end')
        numeros.insert('0.0', resultado)
    except:
        print('')

# Configurando a janela
janela = ct.CTk()
janela.title('Calculadora')
janela.geometry('334x515')
janela.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)
janela.rowconfigure((0, 1, 2, 3, 4), weight=0)

# Campo onde o usuário irá digitar os números
numeros = ct.CTkTextbox(janela, width=325, height=124, corner_radius=10, border_width=5, border_color='#042940', font=(('Arial', 50)))
numeros.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# Botôes    
btn0 = ct.CTkButton(janela, text='0', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn0)
btn0.grid(row=1, column=0, padx=5, pady=5)

btn1 = ct.CTkButton(janela,text='1', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn1)
btn1.grid(row=1, column=1, padx=5, pady=5)

btn2 = ct.CTkButton(janela, text='2', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn2)
btn2.grid(row=1, column=2, padx=5, pady=5)

btn3 = ct.CTkButton(janela, text='3', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn3)
btn3.grid(row=2, column=0, padx=5, pady=5)

btn4 = ct.CTkButton(janela, text='4', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn4)
btn4.grid(row=2, column=1, padx=5, pady=5)

btn5 = ct.CTkButton(janela, text='5', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn5)
btn5.grid(row=2, column=2, padx=5, pady=5)

btn6 = ct.CTkButton(janela, text='6', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn6)
btn6.grid(row=3, column=0, padx=5, pady=5)

btn7 = ct.CTkButton(janela, text='7', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn7)
btn7.grid(row=3, column=1, padx=5, pady=5)

btn8 = ct.CTkButton(janela, text='8', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn8)
btn8.grid(row=3, column=2, padx=5, pady=5)

btn9 = ct.CTkButton(janela, text='9', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940', font=(('arial', 30)), command=funções.btn9)
btn9.grid(row=4, column=0, padx=5, pady=5)

iconClear = resize(Image.open('C:\\Users\\Sorte Show\\Desktop\\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconeclear.png'), (45, 45))
clear = ct.CTkButton(janela, text='', corner_radius=5, width=65, height=65, border_width=2, border_color='#042940',fg_color='#012340', image=iconClear, anchor='right', command=clear_input)
clear.grid(row=5, column=0, padx=5, pady=5)

iconSoma = resize(Image.open('C:\\Users\Sorte Show\\Desktop\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconesoma.png'), (35, 35))
btadição = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconSoma, text='', fg_color='#012340', command=funções.soma)
btadição.grid(row=2, column=3, padx=5, pady=5)

iconMenos = resize(Image.open('C:\\Users\Sorte Show\\Desktop\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconemenos (2).png'), (50, 50))
btmenos = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconMenos, text='', fg_color='#012340', command=funções.menos)
btmenos.grid(row=3, column=3, padx=5, pady=5)

iconDelete = resize(Image.open('C:\\Users\Sorte Show\\Desktop\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconedelete.png'), (40, 40))
btdelete = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconDelete, text='', fg_color='#012340', command=funções.apaga)
btdelete.grid(row=1, column=3, padx=5, pady=5)

iconIgual = resize(Image.open('C:\\Users\Sorte Show\\Desktop\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconeigual.png'), (50, 50))
btigual = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconIgual, text='', fg_color='#012340', command=calcular)
btigual.grid(row=5, column=3, padx=5, pady=5)

iconDivisão = resize(Image.open('C:\\Users\\Sorte Show\\Desktop\\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconedivisao (2).png'), (40, 40))
btdivisão = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconDivisão, text='', fg_color='#012340', command=funções.divisão)
btdivisão.grid(row=4, column=3, padx=5, pady=5)

iconMultipli = resize(Image.open('C:\\Users\\Sorte Show\\Desktop\\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconemultiplicaçao.png'), (35, 35))
btmultipli = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconMultipli, text='', fg_color='#012340', command=funções.multipli)
btmultipli.grid(row=4, column=2, padx=5, pady=5)

iconPonto = resize(Image.open('C:\\Users\\Sorte Show\\Desktop\\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconeponto.png'), (35, 35))
btponto = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconPonto, text='', fg_color='#012340', command=funções.virgula)
btponto.grid(row=5, column=2, padx=5, pady=5)

iconParentesesE = resize(Image.open('C:\\Users\\Sorte Show\\Desktop\\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconeparentesesE.png'), (35, 35))
btparentesesE = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconParentesesE, text='', fg_color='#012340', command=funções.parenteses.E)
btparentesesE.grid(row=4, column=1, padx=5, pady=5)

iconParentesesD = resize(Image.open('C:\\Users\\Sorte Show\\Desktop\\Programação\\Projetos\\Finalizados\\Calculadora\\Icones\\iconeparentesesD.png'), (35, 35))
btparentesesD = ct.CTkButton(janela, width=65, height=65, border_width=2, border_color='#042940', image=iconParentesesD, text='', fg_color='#012340', command=funções.parenteses.D)
btparentesesD.grid(row=5, column=1, padx=5, pady=5)

# Loop pra manter janela aberta
janela.mainloop()