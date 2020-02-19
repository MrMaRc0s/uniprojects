f=open('test.txt','r')
lista=[]
for lines in f:
    x=[]
    for num in lines:
        if num!=' ':
            if num=='\n':
                lista.append(x)
                x=[]
            else:
                x.append(int(num))
f.close()
orizousa=(lista[0][0]*lista[1][1]*lista[2][2])+(lista[0][1]*lista[1][2]*lista[2][0])+(lista[0][2]*lista[1][0]*lista[2][1])-(lista[0][2]*lista[1][1]*lista[2][0])-(lista[0][1]*lista[1][0]*lista[2][2])-(lista[0][0]*lista[1][2]*lista[2][1])
print lista
print 'orizousa:',orizousa
