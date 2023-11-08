# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)





opcao = input('Você deseja [E]ntrar ou [S]air?')

senha_digitada = input('Digite a sua senha: ')
senha_correta = '102030'

if opcao == 'E' and senha_digitada == senha_correta:
    print('Você entrou!')
elif opcao == 'S' and senha_digitada == senha_correta:
    print('Você saiu!')
else:
    print('Tente novamente')
