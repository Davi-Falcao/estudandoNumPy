import numpy as np

# Quais os tipos de arrays que o NumPy oferece?
# 1. Arrays unidimensionais (vetores)
# 2. Arrays bidimensionais (matrizes)
# 3. Arrays multidimensionais (tensores) 3 ou mais dimensões


unidimensional = np.array ([1, 2, 3])  # array unidimensional
print(unidimensional)
print(type(unidimensional))
print("----")

np.array ([[1, 2, 3], [4, 5, 6]])  # array bidimensional
np.array ([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  # array tridimensional


# Criando arrays de zeros com NumPy
# cria um array de zeros com 3 linhas, 4 colunas e 2 "profundidade" 
array_zeros = np.zeros(shape = (3, 4, 2))
print(array_zeros)

print(array_zeros.ndim)  # número de dimensões do array
print(array_zeros.shape)  # formato do array (linhas, colunas, profundidade)
print(f'{array_zeros.size}\n')  # número total de elementos no array
print("----")


# Criando arrays de uns com NumPy
# Cria um array de uns com 2 linhas e 3 colunas preenchido com 1s
array_uns = np.ones(shape = (2, 3))
print(array_uns)
print("----")


# Criando arrays vazios com NumPy
vazio = np.empty(3)
print(vazio)
print("----")

# cria um array com valores de 0 a 9
arr = np.arange(10) 
print(arr)
print("----")

# cria um array com 5 valores igualmente espaçados entre 0 e 10
array_linear = np.linspace(0, 10, 5, endpoint=False, retstep=True) 
print(array_linear)
print("----")

#Como transformar um Vetor em Matriz com NumPy
vetor = np.array([1, 2, 3])
print(vetor.ndim)  # número de dimensões do array
print("----")

matriz = vetor[np.newaxis, :]  # transforma o vetor em matriz (1 linha, 3 colunas)
print(matriz)
print(matriz.ndim)  # número de dimensões do array
print(matriz.shape)  # formato do array (linhas, colunas)
print("----")

matriz_2 = vetor[:, np.newaxis]  # transforma o vetor em matriz (3 linhas, 1 coluna)
print(matriz_2)
print(matriz_2.ndim)  # número de dimensões do array
print(matriz_2.shape)  # formato do array (linhas, colunas)
print("----")


#Como pegar um elemento específico de um array NumPy
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
elemento = array[0]  # pega o elemento da 1ª linha (índices começam em 0)
elemento = array[0, 1]  # pega o elemento da 1ª linha, 2ª coluna
print(elemento)
print("----")


#Como concatenar arrays NumPy

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

array_concatenado = np.concatenate((array1, array2))  
print(array_concatenado)
print("----")

#A ordem importa

array_concatenado2 = np.concatenate((array2, array1))
print(array_concatenado2)
print("----")


#Como consultar itens em um array NumPy mas utiizando logica

array = np.array([10, 20, 30, 40, 50])
print(array)
print("-----------------------")
filtro = array[array > 25]  # cria um filtro lógico
print(filtro)  # imprime o filtro lógico
# Saída: [30 40 50]

#Como fazer operações matemáticas com arrays NumPy

a = np.array([1, 2, 3])

print(a.sum())  # soma todos os elementos do array  
print("----")
print(a.mean())  # calcula a média dos elementos do array
print("----")
print(a.std())  # calcula o desvio padrão dos elementos do array
print("----")
print(a.min())  # encontra o valor mínimo no array
print("----")
print(a.max())  # encontra o valor máximo no array
print("----")
print(a.argmin())  # encontra o índice do valor mínimo no array
print("----")
print(a.argmax())  # encontra o índice do valor máximo no array
print("----")
print(a.cumsum())  # calcula a soma cumulativa dos elementos do array
print("----")
print(a.cumprod())  # calcula o produto cumulativo dos elementos do array
print("----")
print(a.prod())  # calcula o produto de todos os elementos do array
print("----")


#Gerar amostras aleatórias com NumPy
rng = np.random.default_rng()  # cria um gerador de números aleatórios
aleatorios = rng.integers(10, size=(3, 4))  # gera um array 3x4 com números aleatórios entre 0 e 5s
print(aleatorios)
print("----")
