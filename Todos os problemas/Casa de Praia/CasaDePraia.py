class PDFArquivos:
    def __init__(self, nome, paginas, peso):
        self.nome = nome
        self.paginas = paginas
        self.peso = peso

    # Calcular a razão de páginas por MB
    def razao_paginas_por_mb(self):
        return self.paginas / self.peso


class CasaDePraia:
    @staticmethod
    def escolher_arquivos_pendrive(capacidade, arquivos):
        print("\nPasso 1: Arquivos fornecidos inicialmente:")
        for arquivo in arquivos:
            print(f"Nome: {arquivo.nome}, Páginas: {arquivo.paginas}, Peso: {arquivo.peso} MB, "
                  f"Razão páginas/MB: {arquivo.razao_paginas_por_mb():.2f}")

        # Ordenar arquivos por razão de páginas por MB (decrescente)
        print("\nPasso 2: Ordenando os arquivos pela razão de páginas por MB (maior para menor)...")
        arquivos.sort(key=lambda x: x.razao_paginas_por_mb(), reverse=True)

        print("Arquivos ordenados:")
        for arquivo in arquivos:
            print(f"{arquivo.nome} - Razão páginas/MB: {arquivo.razao_paginas_por_mb():.2f}")

        capacidade_atual = 0
        arquivos_selecionados = []

        print("\nPasso 3: Selecionando os arquivos para o pendrive:")
        # Adicionar arquivos ao pendrive até atingir a capacidade
        for arquivo in arquivos:
            if capacidade_atual + arquivo.peso <= capacidade:
                capacidade_atual += arquivo.peso
                arquivos_selecionados.append(arquivo)
                print(f"Adicionado: {arquivo.nome} (Peso acumulado: {capacidade_atual}/{capacidade} MB)")
            else:
                print(f"Não é possível adicionar: {arquivo.nome} (Capacidade excedida)")
                break

        # Exibir os arquivos escolhidos
        print("\nPasso 4: Resultados finais:")
        print("Arquivos selecionados para o pendrive:")
        for arquivo in arquivos_selecionados:
            print(f"- {arquivo.nome}")

        print(f"\nCapacidade total utilizada: {capacidade_atual}/{capacidade} MB")


if __name__ == "__main__":
    # Exemplo de arquivos PDF
    arquivos = [
        PDFArquivos("Algoritmos 101", 300, 10),
        PDFArquivos("Estruturas de Dados", 500, 20),
        PDFArquivos("Teoria da Computação", 200, 5),
        PDFArquivos("Análise de Algoritmos", 400, 15),
        PDFArquivos("Redes Neurais", 150, 8)
    ]

    capacidade_pendrive = 30  # Capacidade do pendrive em MB

    CasaDePraia.escolher_arquivos_pendrive(capacidade_pendrive, arquivos)
