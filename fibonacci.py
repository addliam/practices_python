n=int(input('Enter the length of sequence : '))
def f(a):
    if a<=0:
        return 1
    else:
       return (f(a-1)+f(a-2))
for i in range(n):
    print(f(i),end=' ')      