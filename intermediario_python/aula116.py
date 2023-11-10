# Closure e funções que retornam outras funções
"""
def create_greeting(greeting, name):
    return f'{greeting}, {name}'

greeting_1 = create_greeting('Good Morning', 'Luiz')
greeting_2 = create_greeting('Good Night', 'Maycon')

print(greeting_1)
print(greeting_2)
"""


def create_greeting(greeting, name):
    def greet():
        return f'{greeting}, {name}'
    return

greeting_1 = create_greeting('Good Morning', 'Luiz')
greeting_2 = create_greeting('Good Night', 'Maycon')

print(greeting_1)
print(greeting_2)
