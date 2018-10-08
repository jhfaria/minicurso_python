import numpy as np
import matplotlib.pyplot as plt

# arrays para serer plotados #
x = np.arange(10)
y = np.random.random((10)) * 20
c = np.random.random((10))

plt.figure(1)							# cria a figura
plt.scatter(x, y, c='red', marker='x')	# plota o grafico
plt.grid()								# ativa o grid

# substitui a cor por um vetor, e define o colormap #
plt.figure(2)
plt.scatter(x, y, c=c, cmap='spring', marker='x')
plt.grid()

# mostra as figuras #
plt.show()