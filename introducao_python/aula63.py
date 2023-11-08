# While dentro de While

qntd_linhas = 5
qntd_colunas = 5
qntd_letras = 5

linha = 1

while linha <= qntd_linhas:
    coluna = 1
    
    while coluna <= qntd_colunas:
        print (f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')