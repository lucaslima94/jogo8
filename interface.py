import sys
from tkinter import*
global a
a=0
def imprimef():
    global a
    
    if((a>=0)and(a<len(vetor)-1)):
        a=a+1
        imprime()
def imprimeb():
    global a
    if((a>0)and(a<len(vetor))):
        a=a-1
        imprime()
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
    if(a<len(vetor)):
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
    
    mlabel2=Label(text="caminhos:",fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=75,y=350)
    mlabel2=Label(text=caminho,fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=180,y=350)
    mlabel2=Label(text="nodos:",fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=255,y=350)
    mlabel2=Label(text=nodo,fg='black',bg='white',font="Arial 15 bold",border=5)
    mlabel2.place(x=340,y=350)
    
    b = Button(mGui, text="next", width=18, height=2,command=imprimef)
    b.place(x=350,y=10)
    b2 = Button(mGui, text="back", width=18, height=2,command=imprimeb)
    b2.place(x=200,y=10)
    b3 = Button(mGui, text="final", width=18, height=2,command=imprimefinal)
    b3.place(x=50,y=10)
    b4 = Button(mGui, text="inicio", width=18, height=2,command=imprimeinicio)
    b4.place(x=200,y=60)






#essa parete deve ficar no final

caminhoarvore.reverse()
vetor=caminhoarvore
tamanho=len(caminhoarvore)-1
cria(vetor,i,tamanho)
