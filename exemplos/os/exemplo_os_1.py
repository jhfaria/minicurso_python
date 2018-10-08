import os

# pula uma linha no terminal #
print()

# executa um comando no terminal #
print('Resposta do comando "pwd" no terminal:')
os.system("pwd")

# caminho do codigo #
caminho = os.getcwd()
print('Esse arquivo se encontra em:\n{:s}'.format(caminho))

# pula uma linha no terminal #
print()