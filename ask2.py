goodchar=['B','b','D','d','G','g','H','h','J','j','K','k','L','l','M','m','N','n','P','p','Q','q','S','s','T','t','V','v','X','x','Z','z']
endword=[' ','\n']#iparxi atipos kanonas pos otan tenioni i le3i vazoume keno opote ta kalipti ola me autin tin lista
badchar=['F','f','C','c','K','k','R','r']
specialchar=['(',';','.',',','!','-','?',':',')']
f=open('test.txt','r')
word=''
bad=0
good=0
for lines in f:
    for char in lines:
        if char not in endword:
            if char not in specialchar:
                word+=char
            if char in badchar:
                bad+=1
            elif char in goodchar:
                good+=1            
        else:
            if bad>good:
                print '"'+word+'" is bad word'
            else:
                print '"'+word+'" is good word'
            word=''
            bad=0
            good=0
f.close()
