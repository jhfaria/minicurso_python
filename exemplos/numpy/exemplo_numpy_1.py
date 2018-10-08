import numpy as np

# pula uma linha no terminal #
print()

array = np.arange(10)
print("Array com 10 elementos:")
print(array)

array = array.reshape(2,5)
print("Array com 10 elementos, com reshape para 2 linhas e 5 colunas:")
print(array)

array = np.zeros((2,5))
print("Array de zeros com 2 linhas e 5 colunas:")
print(array)

array = np.random.random((2,5))
print("Array com numeros aleatorios com 2 linhas e 5 colunas:")
print(array)

# pula uma linha no terminal #
print()