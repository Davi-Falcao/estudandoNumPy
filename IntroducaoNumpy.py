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


#Mudar o tipo do array usando astype
array_inteiros = np.array([1, 2, 3, 4, 5])
print(array_inteiros.dtype)  # imprime o tipo dos elementos do array (int64, int32, etc)
print("----")

array_float = array_inteiros.astype(float)  # muda o tipo do array para float
print(array_float.dtype)  # imprime o novo tipo dos elementos do array
print("----")


#Broadcasting com NumPy
print("Broadcasting com NumPy")
# O broadcasting é uma técnica que permite realizar operações entre arrays de diferentes formas

# Exemplo 1: Somar um escalar a um array
print("Exemplo 1: Somar um escalar a um array")
array = np.array([[1, 2, 3], [4, 5, 6]])
escalar = 10
resultado = array + escalar  
# o escalar é "broadcasted" para cada elemento do array, como se o escalar correspondesse a uma matriz de [[10, 10, 10], [10, 10, 10]]
print(resultado)
print("----")


# Exemplo 2: Somar um vetor e uma matriz (shapes diferentes)
print("Exemplo 2: Somar um vetor e uma matriz (shapes diferentes)")
array1 = np.array([[1, 2, 3], [4, 5, 6]])
#O vetor 1D é "broadcasted" para cada linha da matriz 2D, como se o vetor correspondesse a uma matriz de [[10, 20, 30], [10, 20, 30]]
array2 = np.array([10, 20, 30])
resultado = array1 + array2
print(resultado)
print("----")

# Exemplo 3: Somar duas matrizes com shapes compatíveis
print("Exemplo 3: Somar duas matrizes com shapes compatíveis")
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[10], 
                   [20]])

#A matriz 2D é "broadcasted" para cada coluna da matriz 1D, como se a matriz correspondesse a uma matriz de [[10, 10, 10], 
#                                                                                                            [20, 20, 20]]
resultado = array1 + array2
print(resultado)
print("----")

# Exemplo 4: Somar duas matrizes com shapes incompatíveis (gera erro)
print("Exemplo 4: Somar duas matrizes com shapes incompativeis (gera erro)")
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1)
print("----")
array2 = np.array([[10, 20], 
                   [30, 40]])
print(array2)
#Gera um erro porque as shapes (2, 3) e (2, 2) não são compatíveis para broadcasting
try:
    resultado = array1 + array2
    print(resultado)
except ValueError as e:
    print(f'Erro: {e}')
print("----")

#Exemplo 5: Multiplicação de matrizes com broadcasting
print("Exemplo 5: Multiplicacao de matrizes com broadcasting")
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[10],
                   [20]])
resultado = array1 * array2  # cada elemento da matriz 1 é multiplicado pelo correspondente elemento da matriz 2
print(resultado)
print("----")

#Podemos usar o np.newaxis para ajustar as shapes e permitir o broadcasting
print("Podemos usar o np.newaxis para ajustar as shapes e permitir o broadcasting")
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# ajusta a shape de vetor_convertido para (2, 1)
vetor_convertido = np.array([10, 20])[:, np.newaxis] 

resultado =  matriz + vetor_convertido

print(resultado)
print("----")
