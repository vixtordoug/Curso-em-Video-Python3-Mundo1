print(f'{'TABUADA':=^30}')
n=int(input('Digite um número inteiro: '))
cont=int(1)
print('TABUADA DO {}'.format(n))
while(cont<=10):
    print('{} x {} = {}'.format(n, cont, n*cont))
    cont=cont+1
print(f'{'FIM':=^30}')