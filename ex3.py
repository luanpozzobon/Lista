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
teclado = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç'], ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
letras = [set() for _ in range(3)]
tentativas = [ ]
palavra = list(unicodedata.normalize("NFD", lista_termo[randint(0, len(lista_termo))]).encode("ascii", "ignore").decode("utf-8"))
info_palavra = { x : palavra.count(x) for x in palavra }

ACERTO = "\033[42m"
CONTEM = "\033[43m"
NCONTEM = "\033[30m"
RESET = "\033[0;1m"

def print_game():
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
    return palavra[position] == letter
    
def check_letter_in_word(letter):
    return palavra.__contains__(letter)
    
def check_attempt(attempt):
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
while(exit != 's'):
    tentativa = list(input("Digite uma palavra: "))
    tentativas.append(tentativa)

    if check_attempt(tentativa):
        print(RESET + "Você Venceu")
        exit = 's'
    elif len(tentativas) >= 6:
        print(RESET + f"Você perdeu a palavra era {palavra}")
        exit = 's'

    print_game()

# print(lista) # descomente para verificar se a lista está correta