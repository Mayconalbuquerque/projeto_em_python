# High order Functions

# Funções de primeira classe

def saudacao(msg):
    return msg

def executa(funcao):
    return funcao()

saudacao_2 = saudacao
v = executa(saudacao_2)
