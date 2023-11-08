'''
Formatação de Strings
s - string
d - int
f - float
<numero de dígitos>f
x ou X - Hexadecimal 
(Caractere) (><^) (Quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion Flags - !r !s !a - __repr__ __str__  
'''

var = 'abc'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: 0^5}')
print(f'{2010.2010201201021021021:.2f}')
print(f'{2010.2010201201021021021:5=+10.2f}')
