# Introdução ao desempacotamento + tuples (tuplas)

# nomes ['Maria', 'João', 'Maycon']

# nome1, nome2, nome3 = nomes

# print(nome2)

# # ou

# nome1, nome2, nome3 = ['Maria', 'João', 'Maycon']

# print(nome2)

nome1, *restante = ['Maria', 'João', 'Maycon']

print(restante) #['João', 'Maycon']