import os
R='\033[31m'
G='\033[32m'
B='\033[34m'
W='\033[0;1m'
main="""
┏━                            ━┓
                                     
          FUENTE DE SODA                    
                                
   ☕                   Soda  ®  
┗━                            ━┛                           
"""
os.system('clear')
#fuente de soda
print(G+main+W)
a=input('Nombre: ')
b=input('Producto a consumir: ')
c=int(input('Cantidad: '))
d=float(input('Precio del producto: '))
p=c*d
igv=0.18*p
os.system('clear')
print(main)
print(G+'[+] Producto {0}'.format(b))
print('[+] Cantidad             {0}'.format(c))
print('[+] Precio unitario      {0}'.format(d))
print('[+] IGV unitario         {0}'.format(round(igv,4)))
print('[+] IGV TOTAL            {0}'.format(round(igv*c,4)))
print(B+'[.] Precio final        {0}'.format(p))
print(W+'Gracias por su compra. Vuelva pronto')