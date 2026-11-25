print(f'{' MÉDIA ALUNO ':=^30}')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
md=(n1+n2)/2
print(f'{'':-^30}')
print(f'{'1ª Nota: ':<20}{n1:>5.2f}')
print(f'{'2ª Nota: ':<20}{n2:>5.2f}')
print(f'{'A média é: ':<20}{md:>5.2f}')