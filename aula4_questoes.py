1 # Lista com todos os números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]

# Lista com os quadrados de todos os valores da lista [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Lista com todos os números entre 1 e 100 que são divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

# Lista com 'par' ou 'ímpar' para todos os valores em range(0,30,3)
par_ou_impar = ['par' if x % 2 == 0 else 'impar' for x in range(0, 30, 3)]

# Exibindo as listas geradas
print("Números pares entre 20 e 50:", pares)
print("Quadrados da lista [1-9]:", quadrados)
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)
print("'par' ou 'impar' para valores em range(0,30,3):", par_ou_impar)




2 # Solicitar uma frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais ordenadas alfabeticamente
vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])

# Lista de consoantes removendo espaços
consoantes = [letra for letra in frase if letra.lower() not in 'aeiou ']

# Exibindo as listas
print("Vogais:", vogais)
print("Consoantes:", consoantes)




3 horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25

# Usando compreensão de listas para calcular os pagamentos
pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40) for hora in horas_trabalhadas]

print(pagamentos)


4 alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Usando compreensão de listas para filtrar os alunos aprovados
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

print(aprovados)






