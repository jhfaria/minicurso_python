import pandas as pd
import matplotlib.pyplot as plt

# le o arquivo inteiro e cria um dataframe #
df = pd.read_csv("lab01.csv")

# informacoes para plotar #
x = df["Tempo"]
y = df["Temperatura"]

# converte a temperatura de oC para K #
df["Temperatura"] = df["Temperatura"] + 273

# salva um csv novo com a temperatura convertida #
df.to_csv("lab01_v2.csv", sep=',', index=False)

# plota o grafico #
plt.plot(x,y)
plt.show()
