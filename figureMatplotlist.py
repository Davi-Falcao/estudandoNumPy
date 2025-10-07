import matplotlib.pyplot as plt

figura = plt.figure(figsize=(20,5))
figura.suptitle("Titulo Geral da figura")

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 8, 1]

figura.add_subplot(131) # 1 - 3 - 1 , 1 - qnt de linhas, 3 - qnt de colunas, 1 - pos do plot
plt.plot(x, y, ls="-", lw=3, color="b", label="dados")
plt.title("Gráfico normal")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()

figura.add_subplot(132)
plt.title("Gráfico pontos")
plt.scatter(x, y, color="r", label="dados em pontos")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()


figura.add_subplot(133)
plt.title("Gráfico barras")
plt.bar(x, y, color="r", label="dados em barra")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()
plt.show()