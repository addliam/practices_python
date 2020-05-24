import random
import time 
import os

tab = '\t'*2
R = '\033[31m'
G = '\033[32m'
B = '\033[34m'
W = '\033[0;1m'
def menu():
    os.system('clear')
    print('\n'*3)

menu()
score = 0    
for i in range(1,6):
    print(B+'Presta atencion y memoriza')
    if i == 1:
        print(W+"Primero un número de "+str(i) +" cifra")
    else:
        print(W+"Ahora un número de "+str(i) +" cifras")   
    a = i-1 
    a = 10**a
    #print(a)
    b = 10**i
    #print(b)
    n = random.randint(a,b)
    print('\n'+tab+str(n))
    time.sleep(2)
    menu()
    entr = int(input(G+"Que número viste?: "))
    
    if n == entr:
        print(W+'Good Job')
        print(W+'You got a point')
        time.sleep(2)
        os.system('clear')
        score+=1
    else:
        print(R+'It is wrong')  
        time.sleep(2)
        os.system('clear') 
menu()
print(B+'Thnk for play')
print(G+'Your score is '+str(score)) 