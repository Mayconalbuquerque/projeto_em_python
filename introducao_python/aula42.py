#Operador lógico 'not'
#É usado para inverter expressões 
#Not True = False
#Not False = True   

senha= input('Senha:')

if senha == '123':
    print('Agora você tem permissão para acessar o sistema.')

if not senha:
    print('Você não digitou nada, tente novamente!')

else:
    print('Senha incorreta, tente novamente')