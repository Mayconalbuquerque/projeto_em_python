# While
# Executa uma ação enquanto uma condicao for verdadeira
# loop infinito -> Quando um código não tem fim


contador = 0

while contador <= 1000:
    contador += 1 
    if contador == 6:
        print('Não aparece.')
        continue

    if contador >= 10 and contador <= 27:
        print('não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
    
        break

print('Acabou')
