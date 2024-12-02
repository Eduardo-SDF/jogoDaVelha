jogadorAtual = "X"
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("Jogo da velha:")

def mostrarTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        linha = tabuleiro[i]
        print(f" {linha[0]} | {linha[1]} | {linha[2]}")
        if i < 2:
            print("-" * 11)

def fazerJogada(tabuleiro, jogador):
    while True:
        linha = int(input("Escolha a linha (0 a 2): "))
        coluna = int(input("Escolha a coluna (0 a 2): "))

        if 0 <= linha <= 2 and 0 <= coluna <= 2:
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador
                break
            else:
                print("Posição ocupada!")
        else:
            print("Jogada invalida!")

def verificarVitoria(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] ==  jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def verificarEmpate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

while True:
    mostrarTabuleiro(tabuleiro)
    fazerJogada(tabuleiro, jogadorAtual)

    if verificarVitoria(tabuleiro, jogadorAtual):
        mostrarTabuleiro(tabuleiro)
        print("Venceu!")
        break

    if verificarEmpate(tabuleiro):
        mostrarTabuleiro(tabuleiro)
        print("Deu velha!")
        break

    if jogadorAtual == "X":
        jogadorAtual = "0"
    else:
        jogadorAtual = "X"

