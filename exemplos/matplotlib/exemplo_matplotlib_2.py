import numpy as np
import matplotlib.pyplot as plt

# arrays para serer plotados #
x  = np.arange(100)
y1 = np.random.random((100)) * 2
t  = np.linspace(0, 3, 100)
y2 = np.cos(2 * np.pi * t)

plt.figure(1)					# cria a 1a figura
plt.plot(x, y1, x, y2)			# plota o grafico
plt.grid()						# ativa o grid 
plt.xlabel("eixo x")			# titulo do eixo x 
plt.ylabel("eixo y")			# titulo do eixo y 
plt.title("Gráfico simples.")	# titulo do grafico 

plt.figure(2)					# cria a 2a figura
plt.subplot(211) 				# num. de linhas, num. de colunas, num. da figura
plt.plot(x, y1, color='red')	
plt.grid()						
plt.xlabel("eixo x")			
plt.ylabel("eixo y")			
plt.title("Gráfico simples.")	

plt.subplot(212)				# num. de linhas, num. de colunas, num. da figura
plt.plot(x, y2, linestyle='--') 

# mostra as figuras #
plt.show()