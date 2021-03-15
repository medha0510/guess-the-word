word=['f','a','t','h','e','r']
l=len(word)
guess=[]
check=[None]*l
i=0
while i<l :
    check[i]='*'
    i=i+1
print 'word is ',
for i in check :
    print i,
print 'of length ',l

count=l
flag=0
print 'You have ',l,' attempts left'

for i in range(2*l):
    ch=raw_input('Enter a char(lowercase) : ')
    for k in range(l) :
        if word[k]==ch :
            print 'correct..'
            for j in range(l):
                check[k]=ch
            for i in check :
                print i,
            print '\nYou have ',count,' attempts left'
            break
    else :
        count=count-1
        guess.append(ch)
        print 'previous guess :',ch
        print 'try again...'
        for i in check :
            print i,
        print '\nYou have ',count,' attempts left'
    if count==0 :
        print 'your attempts are over'
        break
    if word==check :
        print 'congratulations!! you got it right '
        break
