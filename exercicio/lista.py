lista1 = []
item_adicionado = lista1.append('')
item_removido = lista1.pop()

while True:
    opcao = input('Selecione uma opção:\n[i]nserir  [a]pagar  [l]istar [s]air: ')
    letra_minuscula = opcao.lower()

    if letra_minuscula == 'i':
        adicionar_lista = input('Qual valor deseja adicionar: ')
        item_adicionado = lista1.append(adicionar_lista)

    elif letra_minuscula == 'l':
        print(lista1)
        for lista_enumerada in enumerate(lista1):
            print(lista_enumerada)

    elif letra_minuscula == 'a':
        remover_lista = input('Informe o índice a ser removido: ')
        
        try: 
            numero_remover = int(remover_lista)

        except:
            print('Digite um número.')
        
        item_removido = lista1.pop(numero_remover)
        print(f'A lista atualizada é: {lista1}')

    elif letra_minuscula == 's':
        print('Obrigado por usar o nosso sistema!')
        break
    