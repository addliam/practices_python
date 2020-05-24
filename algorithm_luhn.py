n = str(input('Enter credit card number: '))
def un(x):
    n=[]
    for j in x:        
        if j>=10:
            a = str(j) # '12'
            a=int(a[0])+int(a[1])
            n.append(a)
        else:
            n.append(j) 
    return n            
m=[int(n[i]) for i in range(0,len(n),2)]
p=[int(n[i])*2 for i in range(1,len(n),2)]
np=un(p)
f=sum(np)+sum(m)
if f%10==0:
    print('Valido')
else:
    print('Error, invalidated')    