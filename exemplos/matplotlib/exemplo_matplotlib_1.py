import numpy as np
import matplotlib.pyplot as plt

# arrays para serer plotados #
x = np.arange(10)
y = np.random.random((10)) * 20

plt.figure(1)					# cria uma figura
plt.plot(x, y)					# plota o grafico
plt.grid()						# ativa o grid 
plt.xlabel("eixo x")			# titulo do eixo x 
plt.ylabel("eixo y")			# titulo do eixo y 
plt.title("Gráfico simples.")	# titulo do grafico 

# muda a cor, o estilo e a grossura da linha, e tambem adiciona pontos #
plt.figure(2)
plt.plot(x, y, color='red', marker='o', linestyle='--', linewidth=2)
plt.grid()
plt.axis([0, 3, 0, 10])	# limita os eixos, [xmin, xmax, ymin, ymax]
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.title("Gráfico simples.")

# mostra as figuras #
plt.show()