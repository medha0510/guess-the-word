import random
def game():
    
    words=['father','mother','sister','cousin','relative','grandmother','grandfather','uncle','aunt','tire',
    'love','get','redo','heady','stomach','declare','crayon','hellish','thumb','dashing','pricey','educate',
    'water','closed','induce','health','restrain','point','frog','polite','tiny','six','periodic','grandmother',
    'vessel','tremendous','record','wry','cause','thick','squalid','delicate','nail','rewind','whip','spooky',
    'owe','converge','lunchroom','rambunctious','shit','manager','canvas','mind','become','slim','implore',
    'camp','growth','sea','tire','undesirable','river','design','eat','lewd','skate','unequaled','ugly','car','fit',
    'abundant','willing','quickest','drain','bright','reigned','practise','adamant','bumpy','cloistered','shock',
    'adhesive','confess','cannon','standing','celebrate','ocean','funny','dip','cultured']

    word=random.choice(words)
    l=len(word)
    guess=[]
    guess_word=[]
    check=[None]*l
    i=0
    while i<l :
        check[i]= " * "
        i=i+1
    print('The word is ',*check)

    count=l
    flag=0
    print('You have ',l,' attempts left')

    for i in range(2*l):
        ch=input('Enter a char : ')
        for k in range(l) :
            if word[k]==ch.lower():
                print('Correct..')
                for j in range(l):
                    check[k]=ch.lower()
                print(*check)
                print('\nYou have ',count,' attempts left')
                break
        else :
            count=count-1
            guess.append(ch.lower())
            print('Previous guess :',ch.lower())
            print('Try again...')
            print(*check)
            print('\nYou have ',count,' attempts left.')
        if count==0 :
            print('Your attempts are over :(')
            print('The correct word was ',word)
            break
        if word==check :
            print('Congratulations!! You got it right ;)\n')
    play_again()
def play_again():
    print("If you want to play again, press Y else press N:\n")
    inp=input()
    if(inp=='Y'):
        main()
    else:
        print("Thanks for playing!!!!\n")
def main():
    game()
main()
