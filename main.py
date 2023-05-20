#### EM DESENVOLVIMENTO #####

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 


# cores
cor1 = "#3b3b3b" # black / preta
cor2 = '#ffffff' # white
cor3 = '#48b3e0' # blue
cor4 = "#fcc058"  # orange / larange

 
janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Frames 
frame_cima = Frame(janela, width=450, height=50,bg=cor2, pady=0, padx=3, relief="flat",)
frame_cima.place(x=2, y=2)

frame_direita = Frame(janela, width=450, height=220,bg=cor2, pady=0, padx=3, relief="flat",)
frame_direita.place(x=2, y=54)

frame_esquerda = Frame(janela, width=198, height=260,bg=cor2, pady=0, padx=0, relief="flat",)
frame_esquerda.place(x=454, y=2)

# Frame cima
l_app_nome = Label(frame_cima, text="Calculadora de Unidades de Medidas", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 15 bold'), bg=cor2, fg=cor1)
l_app_nome.place(x=50, y=10)

# Configurando a funcionalidade
unidades = {'peso':[{'kg':1000},{'hg':100},{'dag':10},{'g':1},{'dg':0.1},{'cg':0.01},{'mg':0.001}],'comprimento':[{'km':1000},{'hm':100},{'dam':10},{'m':1},{'dm':0.1},{'cm':0.01},{'mm':0.001}]}



# Aplicando estilo
style = ttk.Style(janela)
style.theme_use("clam")


def mostrar_menu(i):

    unidade_de = []
    unidade_para = []
    unidade_valores = []

    
    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    c_de ['values'] = (unidade_de)
    c_para['values'] = (unidade_para)
    
    l_unidade['text'] = i
    

    
    def calcular():
               
        # Obtendo as unidades
        a = c_de.get()
        b = c_para.get()

        # Obtendo o numero
        numero_para_converter = float(e_numero.get())
        
        dist=unidade_para.index(b) - unidade_de.index(a)

        # verificando a posicao das unidades ( Se vem da direita para esquerda para determinar a operacao ( Multiplicacao ))
        if unidade_para.index(a) <= unidade_de.index(b):

            # verificando a posicao das unidades para obter o valor de distancia
            if unidade_para.index(a) <= unidade_de.index(b):

                # Obtendo o valor de distancia entre as unidades para ser utilizade como expoente
                distancia = unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(10**distancia)
                               
                # mostrando resultado
                l_resultado['text'] = str(resultado) + ' ' + str(unidade_para[unidade_para.index(b)])
                e_numero.delete(0, END)
               
            else:

                # Obtendo o valor de distancia entre as unidades para ser utilizade como expoente
                distancia = unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter *(10**distancia)

                # mostrando resultado
                l_resultado['text'] = str(resultado) + ' ' + str(unidade_para[unidade_para.index(b)])
                e_numero.delete(0, END)

        # verificando a posicao das unidades ( Se vem da direita para esquerda para determinar a operacao ( Divisao ))
        if unidade_para.index(a) > unidade_de.index(b):

            # verificando a posicao das unidades para obter o valor de distancia
            if unidade_para.index(a) <= unidade_de.index(b):

                # Obtendo o valor de distancia entre as unidades para ser utilizade como expoente
                distancia = unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter /(10**distancia)

                # mostrando resultado
                l_resultado['text'] = str(resultado) + ' ' + str(unidade_para[unidade_para.index(b)])
                e_numero.delete(0, END)

            else:

                # Obtendo o valor de distancia entre as unidades para ser utilizade como expoente
                distancia = unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(10**distancia)
                
                # mostrando resultado
                l_resultado['text'] = str(resultado) + ' ' + str(unidade_para[unidade_para.index(b)])
                e_numero.delete(0, END)
                
# Label, botao, entries dentro da funcao  
    l_info = Label(frame_esquerda,width=21, text="Digite o número abaixo ", anchor=CENTER,height=1,pady=3, padx=5, relief="flat", font=('Ivy 10 bold'), bg=cor2, fg=cor1)
    l_info.place(x=0, y=110)   

    e_numero = Entry(frame_esquerda, width=9, font=('Ivy 15 bold'),justify='center',relief=SOLID)
    e_numero.place(x=10, y=150)

    b_calcular = Button(frame_esquerda,command=calcular, text="Calcular", width=8, height=1, bg=cor4, fg=cor1,font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
    b_calcular.place(x=115, y=150)

    l_resultado = Label(frame_esquerda,width=11,  anchor=CENTER,height=1,pady=0, padx=4, relief="groove", font=('Ivy 18 bold'), bg=cor2, fg=cor1)
    l_resultado.place(x=10, y=200)

# Botao e imagem para peso
img_0 = Image.open('images/weight.png')
img_0 = img_0.resize((50, 50), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

b_0 = Button(frame_direita, command=lambda: mostrar_menu('peso'), text="Peso",width=130, height=50, image=img_0, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )

b_0.grid(row=0, column=0,  sticky=NSEW, pady=5, padx=5)

# Botao e imagem para Tempo 
img_1 = Image.open('images/time.png')
img_1 = img_1.resize((50, 50), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)

b_1 = Button(frame_direita, command=lambda: mostrar_menu('tempo'), text="Tempo",width=130, height=50, image=img_1, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_1.grid(row=0, column=1,  sticky=NSEW, pady=5, padx=5)


# Botao e imagem para Comprimento 
img_2 = Image.open('images/length.png')
img_2 = img_2.resize((45, 45), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_direita, command=lambda: mostrar_menu('comprimento'), text="Comprimento",width=130, height=50, image=img_2, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_2.grid(row=0, column=2,  sticky=NSEW, pady=5, padx=5)


# Botao e imagem para Área
img_3 = Image.open('images/square.png')
img_3 = img_3.resize((50, 50), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)

b_3 = Button(frame_direita, command=lambda: mostrar_menu('área'), text="Área",width=130, height=50, image=img_3, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_3.grid(row=1, column=0,  sticky=NSEW, pady=5, padx=5)

 
# Botao e imagem para Quantidade 
img_4 = Image.open('images/volume.png')
img_4 = img_4.resize((50, 50), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_direita, command=lambda: mostrar_menu('quantidade'), text="Quantidade",width=130, height=50, image=img_4, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_4.grid(row=1, column=1,  sticky=NSEW, pady=5, padx=5)


# Botao e imagem para Velocidade 
img_5 = Image.open('images/speed.png')
img_5 = img_5.resize((50, 50), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_direita, command=lambda: mostrar_menu('velocidade'), text="Velocidade",width=130, height=50, image=img_5, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_5.grid(row=1, column=2,  sticky=NSEW, pady=5, padx=5)


# Botao e imagem para Temperatura 
img_6 = Image.open('images/temperature.png')
img_6 = img_6.resize((50, 50), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_direita, command=lambda: mostrar_menu('temperatura'), text="Temperatura ",width=130, height=50, image=img_6, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_6.grid(row=2, column=0,  sticky=NSEW, pady=5, padx=5)

# Botao e imagem para Energia
img_7 = Image.open('images/energy.png')
img_7 = img_7.resize((50, 50), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_direita, command=lambda: mostrar_menu('energia'), text="Energia",width=130, height=50, image=img_7, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_7.grid(row=2, column=1,  sticky=NSEW, pady=5, padx=5)


# Botao e imagem para  Pressão
img_8 = Image.open('images/pressure.png')
img_8 = img_8.resize((50, 50), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_direita, command=lambda: mostrar_menu('pressão'), text="Pressão",width=130, height=50, image=img_8, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID,  bg=cor3, fg=cor2, font=('Ivy 10 bold') )
b_8.grid(row=2, column=2,  sticky=NSEW, pady=5, padx=5)


# Frame Esquerda 
l_unidade = Label(frame_esquerda,width=16, text="---",anchor=CENTER,height=2,pady=0, padx=0, relief="groove", font=('Ivy 15 bold'), bg=cor2, fg=cor1)
l_unidade.place(x=0, y=0)

l_de = Label(frame_esquerda,text="De",  anchor=NW,height=1,pady=0, padx=3, relief="groove", font=('Ivy 10 bold'), bg=cor2, fg=cor1)
l_de.place(x=10, y=70)
c_de = ttk.Combobox(frame_esquerda, width=5,justify='center', font=('Ivy 8 bold'))
c_de.place(x=38, y=70)

l_para = Label(frame_esquerda, text="Para",  anchor=NW,height=1,pady=0, padx=3, relief="groove", font=('Ivy 10 bold'), bg=cor2, fg=cor1)
l_para.place(x=100, y=70)
c_para = ttk.Combobox(frame_esquerda, width=5, justify='center',font=('Ivy 8 bold'))
c_para.place(x=140, y=70)



janela.mainloop()