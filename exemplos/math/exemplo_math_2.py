import math

print("Programa para calcular a diagonal de um quadrado!")

# controla a execucao do programa #
continua = True

while(continua):
	print("Digite o lado do quadrado (em cm):", end=' ')
	# lado do quadrado #
	lado = float(input())

	# diagonal do quadrado #
	diag = lado * math.sqrt(2)	

	print("Diagonal = {:.2f} cm".format(diag))
	
	# continua ou para o programa #
	print("\nDeseja continuar? [S/N]", end=' ')
	if(input().upper() == 'N'):
		continua = False
	else:
		# pula uma linha no terminal #
		print() 


