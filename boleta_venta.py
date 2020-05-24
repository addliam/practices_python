import os
R='\033[31m'
G='\033[32m'
B='\033[34m'
W='\033[0;1m'
os.system('clear')
# gestion boleta de pagos
a = input('Apellido: ')
b = input('Nombre: ')
c = int(input('Horas trabajadas: '))
d = float(input('Valor por hora: '))
sb=c*d
print(R+'[+] Sueldo bruto {0}'.format(sb))
aport=0.13*sb
print(G+'[-] Aporte al SNP {0}'.format(round(aport,4)))
bono=0.7*sb
print(G+'[+] Bonificación familiar {0}'.format(round(bono,4)))
neto=sb-aport+bono
print(B+'[+] Sueldo bruto {0}'.format(neto))