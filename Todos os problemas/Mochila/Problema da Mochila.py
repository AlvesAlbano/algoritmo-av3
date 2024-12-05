class Item:
    def __init__(self, nome: str, valor: int, peso: int):
        self.nome = nome
        self.peso = peso
        self.valor = valor

class Mochila:
    @staticmethod
    def mochila(capacidade: int, Items: list[Item]):
        n: int = len(Items)
        matriz: list[list[int]] = []
        
        for z in range(n + 1):
            linha = [0] * (capacidade + 1)
            matriz.append(linha)
        
        for i in range(1, n + 1):
            for j in range(1, capacidade + 1):
                if Items[i - 1].peso <= j:
                    matriz[i][j] = max(
                        Items[i - 1].valor + matriz[i - 1][j - Items[i - 1].peso],
                        matriz[i - 1][j]
                    )
                else:
                    matriz[i][j] = matriz[i - 1][j]
                print(f"Subproblema: i={i}, j={j}, matriz[{i}][{j}]={matriz[i][j]}")

        itens_selecionados = []
        capacidade_restante = capacidade
        for i in range(n, 0, -1):
            if matriz[i][capacidade_restante] != matriz[i - 1][capacidade_restante]:
                itens_selecionados.append(Items[i - 1])
                capacidade_restante -= Items[i - 1].peso

        return matriz[n][capacidade], itens_selecionados

if __name__ == '__main__':
    items: list[Item] = [
        # nome, valor, peso
        Item("Item1", 60, 10),
        Item("Item2", 100, 20),
        Item("Item3", 120, 30),
    ]
    capacidade: int = 50
    valor_maximo, itens_selecionados = Mochila.mochila(capacidade, items)

    print(f"valor máximo que pode ser inserido em uma mochila de capacidade {capacidade}: {valor_maximo}")
    print("Itens selecionados:")
    for item in itens_selecionados:
        print(f"{item.nome} (Valor: {item.valor}, Peso: {item.peso})")
