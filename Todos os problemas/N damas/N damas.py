def resolver_n_damas(n):
    def eh_valido(tabuleiro, linha, coluna):
        # Verifica se há conflitos na coluna ou diagonais
        for i in range(linha):
            if tabuleiro[i] == coluna or abs(tabuleiro[i] - coluna) == abs(i - linha):
                return False
        return True

    def voltar(tabuleiro, linha):
        if linha == n:
            solucoes.append(tabuleiro[:])  # Adiciona uma solução válida
            return
        for coluna in range(n):
            if eh_valido(tabuleiro, linha, coluna):
                tabuleiro[linha] = coluna  # Coloca a dama
                voltar(tabuleiro, linha + 1)  # Próxima linha
                tabuleiro[linha] = -1  # Remove a dama (backtracking)

    solucoes = []
    tabuleiro = [-1] * n  # -1 significa sem dama
    voltar(tabuleiro, 0)
    return solucoes

def imprimir_tabuleiro(tabuleiro):
    n = len(tabuleiro)
    for linha in tabuleiro:
        linha_visual = ["." for _ in range(n)]
        linha_visual[linha] = "Q"  # Coloca a dama
        print(" ".join(linha_visual))
    print("\n")

n = 6
solucoes = resolver_n_damas(n)

print(f"Total de soluções para {n} damas: {len(solucoes)}\n")
for i, solucao in enumerate(solucoes, start=1):
    print(f"Solução {i}:")
    imprimir_tabuleiro(solucao)
