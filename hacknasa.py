import time
import sys
import os
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
os.system('clear')
def runntek(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(10. / 100)
t='    '        
def ma():
    os.system('clear')  
    print(Y+'Hacking Nasa')       
    print(R+' ————————————————————————————————')
    print(R+t+'=   =    =      ==    =  =')   
    print(R+t+'=   =   = =    =   =  = =')
    print(R+t+'=====   ====   =      ==')
    print(R+t+'=   =  =    =   =  =  = =')
    print(R+t+'=   = =      =   ==   =  =') 
    print(R+' ————————————————————————————————')	
    print('\n')	
def load(n):
    for i in range(1,11):
        n()
        print(B+'[+] Hacking... '+'='*i+' '*(15-i)+str(i*10)+' %')         
        time.sleep(1/3)
        
    print('\n'+' Sucesfully hacked') 
    print('Password found: '+G+'trump2020')   
ma()    
k = input(G+' Target: ')
x= input(G+' User verification: ')
load(ma)
	