# Exemplo de uso dos sets

letras = set()

while True:
    letra = input('Digite uma letra: ')
    numero_letras = len(letra)

    if letra.isdigit():
        print('Digite uma letra')
        continue

    elif numero_letras >= 2: 
        print('Digite apenas uma letra')
        continue

    elif letra.isalpha():
        letras.add(letra.lower())

    print(letras)