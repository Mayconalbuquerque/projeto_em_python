# Closure e funções que retornam outras funções
"""
def create_greeting(greeting, name):
    return f'{greeting}, {name}'

greeting_1 = create_greeting('Good Morning', 'Luiz')
greeting_2 = create_greeting('Good Night', 'Maycon')

print(greeting_1)
print(greeting_2)
"""

lista = ['Maycon', 'Vitória', 'Fátima', 'Rodrigo']

def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}'
    return greet

greeting_1 = create_greeting('Good Morning')
greeting_2 = create_greeting('Good Night')

print(greeting_1('Maycon'))
print(greeting_2('Albuquerque'))

# OR

for names in lista:
    print(greeting_2(names))