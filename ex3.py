"""
Descrição:
Este arquivo contém o código-fonte de um jogo de termoo em Python.

Estratégia:
O jogo termoo é implementado usando uma lista de palavras lidas do arquivo "lista_palavras.txt". Os jogadores tentam adivinhar a palavra oculta, inserindo letras em cada rodada.

Estruturas Usadas:
- Listas: Para armazenar palavras e letras inseridas pelos jogadores.
- Dicionários: Para contar as ocorrências de letras em palavras.
- Sets: Para rastrear letras corretas, letras incorretas e letras já usadas.
"""

arquivo = "lista_palavras.txt" # altere o caminho se necessário
                               # o ideal é que esteja no mesmo diretório do programa

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha

lista = le_arquivo(arquivo)

from random import randint
import unicodedata

lista_termo = list(filter(lambda x : len(x) == 5, lista))
teclado = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
letras = [set() for _ in range(3)]
tentativas = [ ]
palavra = list(unicodedata.normalize("NFD", lista_termo[randint(0, len(lista_termo))]).encode("ascii", "ignore").decode("utf-8"))
info_palavra = { x : palavra.count(x) for x in palavra }

ACERTO = "\033[42m"
CONTEM = "\033[43m"
NCONTEM = "\033[30m"
RESET = "\033[0;1m"

def print_game():
    """
    Imprime as tentaativas anteriores do jogo, incluindo as letras corretas, incorretas e letras já usadas.
    Imprime as letras em formato de teclado, incluindo letras já acertadas, letras que não estão no lugar certo e letras erradas.
    """
    for tentativa in tentativas:
        info_tentativa = { x : tentativa.count(x) for x in tentativa }

        for j in range(len(palavra)):
            if not letras[2].__contains__(tentativa[j]):
                if check_letter_in_position(tentativa[j], j):
                    print(ACERTO + tentativa[j], end="")
                else:
                    if(info_tentativa.get(tentativa[j]) > info_palavra.get(tentativa[j])):
                        info_tentativa[tentativa[j]] -= 1
                        print(NCONTEM + tentativa[j], end="")
                    else:
                        print(CONTEM + tentativa[j], end="")
            else:
                print(NCONTEM + tentativa[j], end="")
            
            print(RESET, end="")
            
        print()

    for _ in range(6 - len(tentativas)):
        print(RESET + '-' * 5)

    for linha in teclado:
        for tecla in linha:
            if letras[0].__contains__(tecla): print(ACERTO + tecla, end="")
            elif letras[1].__contains__(tecla): print(CONTEM + tecla, end="")
            elif letras[2].__contains__(tecla): print(NCONTEM + tecla, end="")
            else: print(RESET + tecla, end="")
            print(RESET, end=" ")
        print()

def check_letter_in_position(letter, position):
    """
    Retorna se uma letra está na posição correta.
    """
    return palavra[position] == letter
    
def check_letter_in_word(letter):
    """
    Retorna se uma letra existe na palavra.
    """
    return palavra.__contains__(letter)
    
def check_attempt(attempt):
    """
    Verifica se a tentativa do jogador está correta, atualiza as letras corretas e incorretas.
    Retorna True caso o jogador tenha acertado a palavra.
    """
    for i in range(len(attempt)):
        if check_letter_in_word(attempt[i]):
            if check_letter_in_position(attempt[i], i):
                letras[0].add(attempt[i])
            else:
                letras[1].add(attempt[i])
        else:
            letras[2].add(attempt[i])

    return attempt == palavra

print_game()
exit = 'n'
print(palavra)
while(exit != 's'):
    tentativa = list(input("Digite uma palavra: "))
    if len(tentativa) != 5:
        print("Palavra inválida!")
        continue
    else:
        tentativas.append(tentativa)

    if check_attempt(tentativa):
        print(RESET + "Você Venceu")
        exit = 's'
    elif len(tentativas) >= 6:
        print(RESET + f"Você perdeu a palavra era {palavra}")
        exit = 's'

    print_game()