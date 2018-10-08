import sys

# pula uma linha no terminal #
print()

# sys.argv retorna uma lista, cujo primeiro elemento eh sempre o nome do arquivo #
print("O nome do arquivo eh: {:s}".format(sys.argv[0]))
print("O 1o parametro passado para o programa eh: {:s}".format(sys.argv[1]))

try:
	# abre o arquivo passado como parametro #
	arq = open(sys.argv[1], 'r')

	# le o arquivo inteiro # 
	linhas = arq.readlines()

	# imprime o conteudo do arquivo #
	print("O conteudo do arquivo eh:")
	for linha in linhas:
		print(linha, end='')

	# pula uma linha no terminal #
	print()
	print()

except FileNotFoundError:
	print("Aqruivo inexistente!")
	
	# pula uma linha no terminal #
	print()