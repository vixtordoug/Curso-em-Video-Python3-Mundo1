print(f'{'OPERAÇÃO COM 2 NÚMEROS':=^40}')
n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))
soma=n1+n2
sub=n1-n2
prod=n1*n2
div=n1/n2
exp=n1**n2
restdiv=n1%n2
intdiv=n1//n2

print(f'{'RESULTADOS':=^40}')
print(f'{'A soma é igual à: ':-<30}{soma:>10.3f}')
print(f'{'A subtração é igual à: ':-<30}{sub:>10.3f}')
print(f'{'O produto é igual à: ':-<30}{prod:>10.3f}')
print(f'{'A divisão é igual à: ':-<30}{div:>10.3f}')
print(f'{'A exponenciação é igual à: ':-<30}{exp:>10.3f}')
print(f'{'O resto da divisão é: ':-<30}{restdiv:>10.3f}')
print(f'{'A parte inteira da divisão é: ':-<30}{intdiv:>10.3f}')