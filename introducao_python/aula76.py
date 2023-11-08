    # Faça um jogo para o usuário adivinha qual a palavra secreta.
    #  - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
    #  - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palaavra secreta.
    #     - Se a letra digitada estiver na
    #     palavra secreta; exiba a letra;
    #     - Se a letra digitada não estiver 
    #     na palavra secreta; exiba *.
    # Faça a contagem de tentativas do seu usuário.

palavra_secreta = 'PAINEL'

letra_certa= ''

letra_errada = ''

nmr_tentativas = 0

while True:
    letra_digitada = input('Letra: ')
    nmr_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada.isnumeric():
        print('Digite uma letra.')

    if letra_digitada.islower():
        print('Digite uma letra maiúscula.')

    if letra_digitada in palavra_secreta:
        letra_certa += letra_digitada
            
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'
        
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Parabéns, você acertou a palavra secreta.')
        print(f'A palavra correta é: {palavra_secreta}')
        print(f'Número de tentativas foi de {nmr_tentativas} vezes.')
        letra_certa = ''
        nmr_tentativas = 0
        
        break