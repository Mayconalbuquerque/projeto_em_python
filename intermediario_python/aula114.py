# High order Functions

# Funções de primeira classe

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia')

print(v)
# retorna um erro


def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'bom dia', 'Maycon'))



def saudacao(msg, nome, outro_nome):
    return f'{msg}, {nome}, {outro_nome}'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'bom dia', 'Maycon', '...'))

