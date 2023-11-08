# Iterável -> str, range, etc(__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# Iter -> me entregue seu iterador


# texto = 'Maycon'
# numeros = range(0, 100, 9)

# for numero in numeros:
#     print(numero)



# texto = 'Maycon'.__iter__()
# print(texto)


# texto = iter('Maycon')
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

texto = 'Maycon' #Iterável
# iterador = iter(texto) #iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
        
#     except:
#         break

for letra in texto:
    print(letra)