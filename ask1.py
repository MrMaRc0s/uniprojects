f=open('test.txt','r')
endword=[' ','\n']#iparxi atipos kononas pos otan tenioni i le3i vazoume keno opote ta kalipti ola me autin tin lista
maxies=['','','','','']
specialchar=['(',';','.',',','!','-','?',':',')']
word=''
for lines in f:
    for char in lines:
        if char not in endword:
            if char not in specialchar:
                word+=char
        else:
            if len(maxies[0])<len(word):
                maxies[0]=word
            word=''
            for i in range(len(maxies)-1):
                for j in range(len(maxies)-1,i,-1):
                    if len(maxies[j])<len(maxies[j-1]):
                        maxies[j],maxies[j-1]=maxies[j-1],maxies[j]
f.close()
print maxies
