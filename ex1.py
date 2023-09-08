"""
Ex1 - Jogo da Velha 4x4

Descrição:
Este programa implementa o jogo da velha em Python, onde dois jogadores, X e O, alternam fazendo jogadas em um tabuleiro. O objetivo é formar uma linha, coluna ou diagonal completa com suas respectivas marcações (X ou O). O programa verifica continuamente se há um vencedor ou empate e exibe o resultado.

Estratégias:
1. Tabuleiro: O tabuleiro é representado como uma matriz de tamanho 4x4, onde "-" representa uma célula vazia, "X" representa uma jogada do jogador X e "O" representa uma jogada do jogador O.

2. Exibição do Tabuleiro:
   - O tabuleiro é impresso na tela após cada jogada, com as posições numeradas para referência.

3. Fazer uma Jogada:
   - Verifica se a jogada é válida (linha e coluna dentro dos limites do tabuleiro e se a célula está vazia).
   - Atualiza o tabuleiro com a marcação do jogador atual.

4. Verificar Vitória:
   - Verifica se o jogador atual ganhou o jogo após sua jogada, examinando linhas, colunas e diagonais.
   
5. Verificar Empate:
   - Verifica se todas as células do tabuleiro estão preenchidas com "X" ou "O", indicando um empate.

6. Alternância de Jogadores:
   - O programa alterna entre os jogadores X e O após cada jogada.

Estruturas Usadas:
1. Tabuleiro (tab):
   - O tabuleiro é representado como uma matriz (lista de listas) de tamanho personalizável.
   - Cada elemento da matriz representa uma célula do tabuleiro.
   - O valor "-" indica uma célula vazia.
   - O valor "X" indica uma jogada do jogador X.
   - O valor "O" indica uma jogada do jogador O.

2. Elementos (elements):
   - Uma tupla que contém duas strings, "X" e "O", representando as marcações dos jogadores.

3. Tamanho do Tabuleiro (size):
   - O tamanho do tabuleiro é definido pelo usuário ao iniciar o programa.
   - Ele determina o número de linhas e colunas do tabuleiro, criando um tabuleiro quadrado.
"""


def create_board():
    """
    Cria e retorna um tabuleiro "vazio" do jogo da velha com o tamanho especificado.
    """
    return [["-"] * size for _ in range(size)]

def print_board():
    """
    Imprime o tabuleiro atual do jogo da velha.
    """
    print("  ", end="")
    for i in range(0, size):
        print(i + 1, end="   ")
    
    k = 0
    for i in range(0, size):
        k += 1
        print()
        print(k, end=" ")
        for j in range(0, size):
            print(tab[j][i], end=" | ")
    
    print()

def make_play(play):
    """
    Faz uma jogada no tabuleiro do jogo da velha.
    Recebe uma tubla com a coluna e linha da jogada.

    Retorna True caso a jogada seja válida, ou False caso haja algum problema com a jogada (Célula ocupada ou fora dos limites).
    """
    if (len(play) != 2): return False
    if (play[0] > size - 1 or play[0] < 0 or play[1] > size - 1 or play[1] < 0): return False
    if not (tab[play[0]][play[1]] == "-"): return False

    tab[play[0]][play[1]] = elements[player]
    return True

def check_sequence(seq):
    """
    Verifica se uma sequência de células no tabuleiro pertence a um único jogador.
    Retorna True ou False.
    """
    return all(cells == elements[player] for cells in seq)

def check_winner(play):
    """
    Verifica se um jogador venceu.
    Recebe uma tupla com a última jogada.

    Retorna True caso haja alguma coluna linha ou diagonal totalmente preenchida pelo jogador atual.
    """
    if(check_sequence((tab[play[0]][x] for x in range(size)))): return True
    if(check_sequence((tab[x][play[1]] for x in range(size)))): return True
    if(play[0] == play[1]):
        if(check_sequence((tab[x][x] for x in range(0, size)))): return True

    if(play[0] + play[1] == size - 1):
        if(check_sequence((tab[x][size - 1 - x] for x in range(size - 1, -1, -1)))): return True
    
    return False

def check_draw():
    """
    Verifica se todas as células do tabuleiro foram preenchidas.
    Retorna True caso todas as células forem diferentes de '-' (Caractere que representa célula vazia)
    """
    return all(cell != "-" for column in tab for cell in column)


elements = ("X", "O")
size = 4
player = 0

tab = create_board()


print("Para fazer uma jogada digite a célula que você deseja jogar (coluna, linha)")
while(True):
    play = ""
    print_board()

    if(player == 0): play = input("Jogador X: ")
    elif(player == 1): play = input("Jogador O: ")
    
    play = [int(x) - 1 for x in play.split(",")]

    if not (make_play(play)):
        print("Jogada Inválida! Tente Novamente!")
        continue

    if (check_winner(play)):
        print(f"Fim de Jogo! Vencedor: {elements[player]}")
        break

    if (check_draw()):
        print("Fim de Jogo! Não há mais células disponíveis")
        break

    player = (player + 1)%2