endword=[' ','\n']#iparxi atipos kononas pos oti tenioni i le3i vazoume keno opote ta kalipti ola me autin tin lista
specialchar=['(',';','.',',','!','-','?',':',')']
f=open('test.txt','r')
word=''
for lines in f:
    for char in lines:
        if char not in endword:
            if char not in specialchar:
                word+=char        
        else:
            if len(word)>3:
                print word[1:]+word[0]+'ay'
            word=''
f.close()
