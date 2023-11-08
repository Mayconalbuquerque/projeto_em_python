# Exercício
# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com
# erros de índice inexistentes na lista



# import os

lista = []

while True:
    opcao = input('Selecione uma opção:\n[i]nserir  [a]pagar  [l]istar: ')

    if opcao == 'i':
        # os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
            
    elif opcao == 'a':
        # os.system('cls')
        apagar_str = input('Digite o índice: ')
            
        try:
            apagar = int(apagar_str)
            del lista[apagar]

        except ValueError:
            print('Digite o número do indice para apagar')
            
        except IndexError:
            print('Digite um índice existente')

    elif opcao == 'l':
        # os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar.')
        for indice, valor in enumerate(lista):
            print(indice, valor)
                
    else:
        print('Por favor, escolha entre i, a ou l.')