import os

# lista os arquivos na pasta #
arquivos = os.listdir()

# pula uma linha no terminal #
print()

for arquivo in arquivos:
	# abre o arquivo atual # 
	arq = open(arquivo, 'r')

	# le o arquivo inteiro #
	linhas = arq.readlines()

	# separa a 1a linha #
	linha1 = linhas[0]
	linha1 = linha1.split()

	# caso o arquivo aberto seja um dos desejados #
	if(linha1[0] == "lados"):
		triangulo = linha1[1]
		lados = linhas[1:]
		arq.close()
	# caso nao seja #
	else:
		arq.close()
		continue

	# soma dos lados do triangulo #
	soma_lados = 0
	for lado in lados:
		soma_lados += int(lado)

	# confere se eh ou nao um triangulo #
	for lado in lados:
		if((soma_lados - int(lado)) > int(lado)):
			eh_triang = True
		else:
			eh_triang = False
			break

	if(eh_triang):
		print("{:s} eh um triangulo!".format(triangulo))
	else:
		print("{:s} nao eh um triangulo!".format(triangulo))

# pula uma linha no terminal #
print()