# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se o nome e a idade forem digitados:
#     Exiba:
#     Seu nome é {nome}
#     Seu nome invertido é {nome invertido}
#     Se nome contém (ou não) espaços
#     Seu nome tem {n} letras
#     A primeira letra do seu nome é {letra}
#     A ultima letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#     Exiba 'Desculpe, você deixou campos vazios.'

nome=input('Digite o seu nome: ')
idade=input('Digite a sua idade: ')
qnt_letras=len(nome)

if nome and idade:
    print('Seu nome é %s'% nome)
    print('Seu nome invertido é %s'% nome[::-1])
    
    if ' ' in nome:
        print('Seu nome possui espaços.')
    else:
        print('Seu nome não possui espaços.')
    
    print('A primeira letra do seu nome é: %s'% nome[0])
    print('A ultima letra do seu nome é: %s'% nome[-1])
else:
    print('Desculpe, você deixou campos vazios.')
