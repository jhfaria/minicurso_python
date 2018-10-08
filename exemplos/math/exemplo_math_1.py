import math

print("Programa para calcular area e volume de uma esfera!")

# controla a execucao do programa #
continua = True

while(continua):
	print("Digite o raio da esfera (em cm):", end=' ')
	# raio da esfera #
	raio = float(input())

	# area da esfera #
	A = 4 * math.pi * pow(raio, 2)
	
	# volume da esfera #
	V = 4 * math.pi * pow(raio, 3) / 3

	print("Area   = {:.2f} cm^2".format(A))
	print("Volume = {:.2f} cm^3".format(V))

	# continua ou para o programa #
	print("\nDeseja continuar? [S/N]", end=' ')
	if(input().upper() == 'N'):
		continua = False
	else:
		# pula uma linha no terminal #
		print() 


