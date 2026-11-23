a=input('Digite algo: ')
result=str
if(a.isnumeric()):
    result='Sim'
else:
    result='Não'
print(f"A entrada é numérica: {result}")

if(a.isalpha()):
    result='Sim'
else:
    result='Não'
print(f'A entrada é alfabética: {result}')
