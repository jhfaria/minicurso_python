import numpy as np
import matplotlib.pyplot as plt

# arrays para serer plotados #
x = np.arange(10000)
y = np.arange(10000)

plt.figure(1)		 # cria a figura
plt.subplot(211)	 # plota o grafico
plt.plot(x, y)		 # plota o grafico
plt.grid()			 # ativa o grid
plt.yscale('linear') # linear
plt.ylabel('linear') # titulo do eixo y

plt.subplot(212)
plt.plot(x, y)
plt.grid()
plt.yscale('log')	 # log
plt.ylabel('log')

# mostra as figuras #
plt.show()