import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', label="dados")  # Adiciona marcadores aos pontos
plt.title("Exemplo Simples de Gráfico com Matplotlib")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
#Ajustando a escala do eixo x e y

#plt.xticks([0,2,4,8,10,12])
#plt.yticks([-1,2,4,6, 8, 10, 12])

#propriedades da linha
x2 = [2, 4, 16, 64]
y2 = [1, 2, 3, 4]

plt.plot(x2, y2, linestyle=":", color="red", label="vermelho", lw=3)


plt.scatter(x2,y2, color="k")

#plt.bar(x2,y2, color="y")

#Alterando limites do gráfico 

#plt.axis(xmin=-1, xmax=12, ymin= -1, ymax= 20)
plt.axis("auto")
plt.legend()
plt.show()
