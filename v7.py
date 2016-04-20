import sys
from tkinter import*
global a
a=0
def imprimef():
    imprime()
    global a
    a=a+1
def imprimeb():
    imprime()
    global a
    a=a-1
def imprimefinal():
    global a
    a=len(vetor)
    print(a)
    a=a-1
    imprime()
def imprimeinicio():
    global a
    print(a)
    a=0
    imprime()
    
def imprime():
    mlabel=Label(text=vetor[a][0],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel.place(x=205,y=150)
    mlabel2=Label(text=vetor[a][1],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel2.place(x=255,y=150)
    mlabel2=Label(text=vetor[a][2],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel2.place(x=305,y=150)
    mlabel=Label(text=vetor[a][3],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel.place(x=205,y=220)
    mlabel2=Label(text=vetor[a][4],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel2.place(x=255,y=220)
    mlabel2=Label(text=vetor[a][5],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel2.place(x=305,y=220)
    mlabel=Label(text=vetor[a][6],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel.place(x=205,y=290)
    mlabel2=Label(text=vetor[a][7],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel2.place(x=255,y=290)
    mlabel2=Label(text=vetor[a][8],fg='black',bg='white',font="Arial 24 bold",border=5)
    mlabel2.place(x=305,y=290)

def cria(vetor,nodo,caminho):
    mGui = Tk()
    mGui.geometry('520x420')
    mGui.title('jogo do 8')
    
    mlabel2=Label(text="caminho",fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=75,y=350)
    mlabel2=Label(text=caminho,fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=175,y=350)
    mlabel2=Label(text="nodo",fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=255,y=350)
    mlabel2=Label(text=nodo,fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=335,y=350)
    
    b = Button(mGui, text="next", width=18, height=2,command=imprimef)
    b.place(x=350,y=10)
    b2 = Button(mGui, text="back", width=18, height=2,command=imprimeb)
    b2.place(x=200,y=10)
    b3 = Button(mGui, text="final", width=18, height=2,command=imprimefinal)
    b3.place(x=50,y=10)
    b4 = Button(mGui, text="inicio", width=18, height=2,command=imprimeinicio)
    b4.place(x=200,y=60)
vetor= [[1, 4, 2, 3, 7, 5, 0, 6, 8], [1, 4, 2, 3, 7, 5, 6, 0, 8], [1, 4, 2, 3, 0, 5, 6, 7, 8], [1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
nodo=30000
caminho=50000
cria(vetor,nodo,caminho)



