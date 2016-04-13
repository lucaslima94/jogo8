estadoinicial = [1,5,8,0,2,3,4,6,7]
print (estadoinicial[1])
print (estadoinicial[0])
print (estadoinicial[5])
count = 0
for x in range(9):
    print ("Esse: ")       
    print (estadoinicial[x])
    if(estadoinicial[x] != 0):
        for y in range((x+1), 9):
            if(estadoinicial[y] != 0):
                print ("Compara com esse: ")
                print (estadoinicial[y])
                if(estadoinicial[x] > estadoinicial[y]):
                    count = count + 1
print ("Numero total de inversoes: ", count)
if((count % 2) == 0):
    print ("Soluvel")

#Tranformar saporra em funçao
