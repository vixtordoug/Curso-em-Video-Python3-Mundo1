print(f'{'':-^50}')
print(f'{'CONVERSOR DE TEMPERATURA °C':^50}')
print(f'{'':-^50}')
c=float(input('Digite a temperatura em °C: '))

print(f'{'':-^50}')
print('Kelvin: {} K'.format(c+273.15))
print('Fahreheit: {} °F'.format((c*9/5)+32))
print(f'{'':-^50}')