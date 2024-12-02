class Item:
    def __init__(self,nome:str,valor:int,peso:int):
        self.nome = nome
        self.peso = peso
        self.valor = valor
        
class Mochila:
    
    @staticmethod
    def mochila(capacidade:int,Items:list[Item]):
        n:int = len(Items)
        matriz:int = []
        
        for z in range(n+1):
            linha = [0] * (capacidade + 1)
            matriz.append(linha)
        
        for i in range(1,n+1):
            for j in range(1,capacidade+1):
                if Items[i-1].peso <= j:
                    matriz[i][j] = max(Items[i-1].valor + matriz[i-1][j - Items[i-1].peso], matriz[i-1][j])
                else:
                    matriz[i][j] = matriz[i-1][j]
                print(f"Subproblema: i={i}, j={j}, matriz[{i}][{j}]={matriz[i][j]}")
        
        # print("matriz final")
        # for z in matriz:
        #     print(z)
        
        return matriz[n][capacidade]               

if __name__ == '__main__':
    items:list[Item] = [
        #nome peso preço
        Item("Item1", 10, 10),
        Item("Item2", 5, 20),
        Item("Item3", 5, 30),
    ]
    capacidade:int = 50
    print(f"valor maximo que poder ser inserido em uma mochila de capacidade {capacidade}: {Mochila.mochila(capacidade, items)}")
    # print(Mochila.mochila(capacidade, items))