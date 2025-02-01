1. def main():
    numeros = []
    # Solicita pelo menos 4 números inteiros do usuário
    while len(numeros) < 4:
        try:
            num = int(input("Digite um número inteiro (mínimo 4 valores): "))
            numeros.append(num)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    # O loop continua solicitando números até o usuário decidir parar
    while True:
        opcao = input("Deseja adicionar mais um número? (s/n): ").lower()
        if opcao == 's':
            try:
                num = int(input("Digite um número inteiro: "))
                numeros.append(num)
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        elif opcao == 'n':
            break
        else:
            print("Opção inválida! Digite 's' para sim ou 'n' para não.")
    
    # Exibindo os resultados conforme solicitado
    print(f"\nLista original: {numeros}")
    print(f"Os 3 primeiros elementos: {numeros[:3]}")
    print(f"Os 2 últimos elementos: {numeros[-2:]}")
    print(f"Lista invertida: {numeros[::-1]}")
    print(f"Elementos de índice par: {numeros[::2]}")
    print(f"Elementos de índice ímpar: {numeros[1::2]}")

if __name__ == "__main__":
    main()



2.def extrair_dominios(urls):
    dominios = [url[4:-4] for url in urls]  # Remove "www." do início e ".com" do final
    return dominios

# Exemplo de uso
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = extrair_dominios(urls)

print(dominios)


3.import random

# Gerar uma lista com 20 elementos entre -10 e 10
numeros = [random.randint(-10, 10) for _ in range(20)]
print(f"Original: {numeros}")

# Encontrar o intervalo com maior quantidade de números negativos
maior_intervalo_negativos = (0, 0)  # Inicialmente, intervalo vazio
maior_contagem_negativos = 0

# Percorre a lista buscando o intervalo de maior quantidade de negativos
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros) + 1):
        sub_lista = numeros[i:j]
        contagem_negativos = sum(1 for num in sub_lista if num < 0)
        if contagem_negativos > maior_contagem_negativos:
            maior_contagem_negativos = contagem_negativos
            maior_intervalo_negativos = (i, j)

# Remover o intervalo com maior quantidade de números negativos
inicio, fim = maior_intervalo_negativos
del numeros[inicio:fim]

# Exibir a lista editada
print(f"Editada: {numeros}")
