"""

Estruturas Usadas:
- Dicionário para simular um banco de dados de usuários
"""

def register_user():
    """
    Registra um novo usuário com os campos solicitados na inicialização do programa.
    Pergunta se o usuário gostaria de inserir mais campos, até que ele peça para sair.
    """
    id = len(banco_usuarios) + 1
    banco_usuarios[id] = dict.fromkeys(campos, "")
    for i in campos:
        banco_usuarios[id][i] = input(f"Digite {i} do usuário: ")

    campo_extra = input("Digite o campo extra a ser inserido: ")
    while(campo_extra != "sair"):
        banco_usuarios[id][campo_extra] = input(f"Digite {campo_extra} do usuario: ")
        campo_extra = input("Digite o campo extra a ser inserido: ")
        
def print_users(*args, **kwargs):
    """
    Imprime as informações do usuário de acordo com a opção de filtro selecionada no menu.
    """
    if not args and not kwargs:
        for i in banco_usuarios:
            print(banco_usuarios.values())
    elif args and not kwargs:
        for data in banco_usuarios.items():
            if data["nome"] in args:
                print(data)
    elif not args and kwargs:
        filtered_users = []
        for data in banco_usuarios.values():
            match = True
            for chave, valor in kwargs.items():
                if chave not in data or data[chave] != valor:
                    match = False
                    break
            if match:
                filtered_users.append(data)
        
        if filtered_users:
            for data in filtered_users:
                print(data)
        else:
            print("Nenhum usuário encontrado com os critérios especificados.")
    elif args and kwargs:
        for data in banco_usuarios.values():
            if data["nome"] in args:
                match = True
                for chave, valor in kwargs.items():
                    if chave not in data or data[chave] != valor:
                        match = False
                        break
                if match:
                    print(data)

banco_usuarios = { }

campos = list(input("Digite os campos obrigatórios (separados por ,): ").split(","))
while(True):
    print("1-Cadastrar Usuário")
    print("2-Imprimir Usuários")
    print("0-Encerrar")

    option = int(input("Selecione uma opção: "))
    if option == 0:
        break
    elif option == 1:
        register_user()

    elif option == 2:
        print("1-Imprimir todos")
        print("2-Filtrar por nomes")
        print("3-Filtrar por campos")
        print("4-Filtra por nome e campos")
        option = int(input("Selecione uma opção: "))
        if option == 1:
            print_users()
        elif option == 2:
            names = input("Digite os nomes (separados por ,): ").split(",")
            print_users(*names)
        elif option == 3:
            campos = { }
            
            campo = input("Digite o campo de busca: ")
            while(campo != "sair"):
                valor = input(f"Digite {campo}: ")
                campos[campo] = valor
                campo = input("Digite o campo de busca: ")
            
            print_users(**campos)
        elif option == 4:
            names = input("Digite os nomes (separados por ,): ").split(",")            
            campos = { }
            
            campo = input("Digite o campo de busca: ")
            while(campo != "sair"):
                valor = input(f"Digite {campo}: ")
                campos[campo] = valor
                campo = input("Digite o campo de busca: ")
            
            print_users(*names, **campos)