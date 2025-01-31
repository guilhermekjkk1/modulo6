1. 
import random

# Gerar a lista com 20 valores inteiros entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Lista ordenada sem modificar a original
valores_ordenados = sorted(valores)

# Índice do maior valor
indice_maior = valores.index(max(valores))

# Índice do menor valor
indice_menor = valores.index(min(valores))

# Imprimir os resultados
print("Lista ordenada (sem modificar a original):", valores_ordenados)
print("Lista original:", valores)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)


2.
import random

# Gerar o valor aleatório para num_elementos entre 5 e 20
num_elementos = random.randint(5, 20)

# Gerar a lista com num_elementos valores entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcular a soma dos valores da lista
soma_valores = sum(elementos)

# Calcular a média dos valores da lista
media_valores = soma_valores / num_elementos

# Imprimir os resultados
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma_valores)
print("Média dos valores:", media_valores)


3.import random
from collections import Counter

# Gerar duas listas com 20 valores inteiros entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrar a interseção (valores que se repetem nas duas listas, sem duplicatas)
interseccao = sorted(list(set(lista1) & set(lista2)))

# Contagem de quantas vezes cada elemento aparece em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Imprimir os resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista interseccao ordenada:", interseccao)
print("Contagem em Lista 1:", contagem_lista1)
print("Contagem em Lista 2:", contagem_lista2)


4.# Função para intercalar duas listas
def intercalar_listas(lista1, lista2):
    # Descobrir o tamanho mínimo entre as duas listas
    tamanho_min = min(len(lista1), len(lista2))

    # Combinar as listas de forma alternada até o tamanho da menor lista
    intercalada = [None] * (len(lista1) + len(lista2))
    intercalada[:2*tamanho_min:2] = lista1[:tamanho_min]
    intercalada[1:2*tamanho_min:2] = lista2[:tamanho_min]

    # Adicionar os elementos restantes da lista maior
    intercalada[2*tamanho_min:] = lista1[tamanho_min:] + lista2[tamanho_min:]

    return intercalada

# Receber as duas listas de números do usuário
lista1 = list(map(int, input("Digite os números da primeira lista separados por espaço: ").split()))
lista2 = list(map(int, input("Digite os números da segunda lista separados por espaço: ").split()))

# Combinar as duas listas de forma alternada
lista_intercalada = intercalar_listas(lista1, lista2)

# Imprimir o resultado
print("Lista intercalada:", lista_intercalada)

