# NOME: VINICIUS LEANDRO RODRIGUES DE SOUZA | DISCIPLINA: RACIOCÍNIO COMPUTACIONAL
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

estudantes = []  # LISTA PARA ARMAZENAR OS NOMES DOS ESTUDANTES
professores = []
disciplinas = []
turmas = []
matriculas = []

while True:  # LOOP CRIADO PARA O USUÁRIO UTILIZAR O MENU PRINCIPAL QUANTAS VEZES FOR NECESSÁRIO

    import json

    def analisar(x, y):

        if y in x.values():
            print("Código já cadastrado")
            y = y - x.values


    print("----- MENU PRINCIPAL -----")

    print("(1) Gerenciar estudantes."'\n' "(2) Gerenciar professores.",
          '\n' "(3) Gerenciar disciplinas."'\n' "(4) Gerenciar turmas.",
          '\n' "(5) Gerenciar matrículas." '\n' "(9) Sair.")

    opcao_usuario = input("Informe a opção desejada:")  # USUÁRIO SELECIONA A OPÇÃO DESEJADA

    if (opcao_usuario == "1" or opcao_usuario == "2" or opcao_usuario == "3" or opcao_usuario == "4"
            or opcao_usuario == "5" or opcao_usuario == "9"):
        print("Você escolheu a opção:", opcao_usuario)
    else:  # esse bloco é responsável por mostrar qual opção o usuário selecionou
        print("Você escolheu uma opção inválida")

    if opcao_usuario == "9":
        print("Você escolheu sair")  # esse bloco encerra o loop e por consequência o programa.
        break

    while opcao_usuario == "1" or opcao_usuario == "2" or opcao_usuario == "3" or opcao_usuario == "4" \
            or opcao_usuario == "5" or opcao_usuario == "9":  # LOOP CRIADO PARA O USUÁRIO UTILIZAR O MENU SECUNDÁRIO

        if opcao_usuario == "1":
            print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****" '\n' "(1) Incluir."'\n'
                  "(2) Listar." '\n' "(3) Atualizar." '\n' "(4) Excluir" '\n'
                  "(9) Voltar ao menu principal.")

        if opcao_usuario == "2":
            print("***** [PROFESSORES] MENU DE OPERAÇÕES *****" '\n' "(1) Incluir."'\n'
                  "(2) Listar." '\n' "(3) Atualizar." '\n' "(4) Excluir" '\n'
                  "(9) Voltar ao menu principal.")

        if opcao_usuario == "3":
            print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****" '\n' "(1) Incluir."'\n'
                  "(2) Listar." '\n' "(3) Atualizar." '\n' "(4) Excluir" '\n'
                  "(9) Voltar ao menu principal.")

        if opcao_usuario == "4":
            print("***** [TURMAS] MENU DE OPERAÇÕES *****" '\n' "(1) Incluir."'\n'
                  "(2) Listar." '\n' "(3) Atualizar." '\n' "(4) Excluir" '\n'
                  "(9) Voltar ao menu principal.")

        if opcao_usuario == "5":
            print("***** [MATRÍCULAS] MENU DE OPERAÇÕES *****" '\n' "(1) Incluir."'\n'
                  "(2) Listar." '\n' "(3) Atualizar." '\n' "(4) Excluir" '\n'
                  "(9) Voltar ao menu principal.")

        acao_usuario = input("Informe a ação desejada:")  # Usuário seleciona a ação desejada.

        if acao_usuario == "1" or acao_usuario == "2" or acao_usuario == "3" or acao_usuario == "4" \
                or acao_usuario == "9":
            print("Você escolheu a ação:", acao_usuario)
        # Bloco responsável por mostrar qual ação o usuário selecionou
        else:
            print("Você escolheu uma ação inválida")

        # FUNÇÕES: INCLUIR, LISTAR, ATUALIZAR E EXCLUIR
        def incluir(x, y=""):  # FUNÇÃO INCLUSÃO

            print("==== INCLUSÃO ====")  # Incluir elementos na lista
            print("Após digitar o nome, pressione ENTER para continuar")

            try:
                if y == "estudante":
                    cod = int(input("Informe o código do estudante"))  # código do elemento
                    nome = input("Informe o nome do estudante")  # nome do elemento
                    cpf = input("Informe o CPF do estudante")  # cpf do elemento

                    for i in estudantes:
                        analisar(i, cod)
                    x.append({"código do estudante": cod, "nome do estudante:": nome, "cpf do estudante": cpf})
            except:
                print("Valor inválido. Digite um valor válido.")

            try:
                if y == "professor":
                    cod = int(input("Informe o código do professor"))  # código do elemento
                    nome = input("Informe o nome do professor")  # nome do elemento
                    cpf = input("Informe o CPF do professor")  # cpf do elemento

                    for i in professores:
                        analisar(i, cod)
                    x.append({"código do professor": cod, "nome do professor:": nome, "cpf do professor": cpf})
            except:
                print("Valor inválido. Digite um valor válido.")

            try:

                if y == "disciplina":
                    cod = int(input("Informe o código da disciplina "))  # código do elemento
                    nome = input("Informe o nome da disciplina")  # nome do elemento

                    for i in disciplinas:
                        analisar(i, cod)
                    x.append({"código da disciplina": cod, "nome da disciplina:": nome})

            except:
                print("Valor inválido. Digite um valor válido.")

            try:

                if y == "turma":

                    cod = int(input("Informe o código da turma "))  # código do elemento
                    cod_2 = int(input("Informe o código do professor "))  # código do elemento
                    cod_3 = int(input("Informe o código da disciplina "))  # código do elemento

                    for i in turmas:
                        analisar(i, cod)
                    x.append({"código da turma": cod, "código do professor:": cod_2, "código da disciplina": cod_3})

            except:
                print("Valor inválido. Digite um valor válido.")

            try:
                if y == "matricula":
                    cod = int(input("Informe o código da turma "))  # código do elemen
                    cod_2 = int(input("Informe o código do estudante "))  # código do elemento

                    for i in matriculas:
                        analisar(i, cod)
                    x.append({"código da turma": cod, "código do estudante": cod_2})


            except:
                print("Valor inválido. Digite um valor válido.")


        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(str(estudantes + professores + disciplinas + turmas + matriculas), arquivo, ensure_ascii=False)


        def listar(x, y=""):  # FUNÇÃO LISTAR
            print("==== LISTAGEM ====")
            for i in x:  # Loop for utilizado para percorrer cada item da lista.
                print("- ", i)

            if len(x) == 0:
                if y == "estudante":
                    print("Não há estudantes cadastrados")
                    print("Pressione ENTER para continuar")

            if len(x) == 0:
                if y == "professor":
                    print("Não há professores cadastrados")

            if len(x) == 0:
                if y == "disciplina":
                    print("Não há disciplinas cadastradas")

            if len(x) == 0:
                if y == "turma":
                    print("Não há turmas cadastradas")

            if len(x) == 0:
                if y == "matricula":
                    print("Não há matrículas cadastradas")


        def atualizar(x, y=""):

            if estudantes or professores or disciplinas or turmas or matriculas != []:
                try:
                    if y == "estudante":
                        cod = int(input("Digite o código do estudante que deseja atualizar: "))
                        cod_1 = int(input("Informe o código do estudante"))
                        nome_1 = input("Informe o nome do estudante: ")
                        cpf_1 = input("Informe o CPF do estudante: ")

                        for i in x:
                            if i.get("código do estudante") == cod:
                                i.clear()
                                i.update({"código do estudante": cod_1, "nome do estudante": nome_1, "cpf do estudante": cpf_1})
                except:
                    print("Valor inválido. Digite um valor válido.")

                try:
                    if y == "professor":
                        cod = int(input("Digite o código do professor que deseja atualizar: "))
                        cod_1 = int(input("Informe o código do professor"))
                        nome_1 = input("Informe o nome do professor: ")
                        cpf_1 = input("Informe o CPF do professor: ")

                        for i in x:
                            if i.get("código do professor") == cod:
                                i.clear()
                                i.update({"código do professor": cod_1, "nome do professor": nome_1, "cpf do professor": cpf_1})
                except:
                    print("Valor inválido. Digite um valor válido.")

                try:
                    if y == "disciplina":
                        cod = int(input("Digite o código da disciplina que deseja atualizar: "))
                        cod_1 = int(input("Informe o código da disciplina"))
                        nome_1 = input("Informe o nome da disciplina: ")

                        for i in x:
                            if i.get("código da disciplina") == cod:
                                i.clear()
                                i.update({"código da disciplina": cod_1, "nome da disciplina": nome_1})
                except:
                    print("Valor inválido. Digite um valor válido.")

                try:
                    if y == "turma":
                        cod_0 = int(input("Digite o código da turma que deseja atualizar: "))
                        cod = int(input("Informe o código da turma "))  # código do elemento
                        cod_2 = int(input("Informe o código do professor "))  # código do elemento
                        cod_3 = int(input("Informe o código da disciplina "))  # código do elemento

                        for i in x:
                            if i.get("código da turma") == cod_0:
                                i.clear()
                                i.update({"código da turma": cod, "código do professor": cod_2, "código da disciplina": cod_3})
                except:
                    print("Valor inválido. Digite um valor válido.")

                try:
                    if y == "matricula":
                        cod_0 = int(input("Informe o código da matricula que deseja atualizar"))
                        cod = int(input("Informe o código da turma "))  # código do elemento
                        cod_2 = int(input("Informe o código do estudante "))  # código do elemento

                        for i in x:
                            if i.get("código da turma") == cod_0:
                                i.clear()
                                i.clear()
                                i.update({"código da turma": cod, "código do estudante": cod_2})
                except:
                    print("Valor inválido. Digite um valor válido.")

                with open("dados.json", "r", encoding="utf-8") as arquivo:
                            json.load(arquivo)

                with open("dados.json", "w", encoding="utf-8") as arquivo:
                    json.dump(str(estudantes + professores + disciplinas + turmas + matriculas), arquivo, ensure_ascii=False)
            else:
                print("Não há elementos cadastrados")

        def excluir(x, y=""):

            if estudantes or professores or disciplinas or turmas or matriculas != []:
                try:
                    if y == "estudante":
                        for i in estudantes:
                            cod = int(input("Informe o código do estudante que deseja excluir da lista:"))
                            if i.get("código do estudante") == cod:
                                x.remove(i)

                    if y == "professor":
                        for i in x:
                            cod = int(input("Informe o código do professor que deseja excluir da lista:"))
                            if i.get("código do professor") == cod:
                                x.remove(i)

                    if y == "disciplina":
                        for i in x:
                            cod = int(input("Informe o código da disciplina que deseja excluir da lista:"))
                            if i.get("código da disciplina") == cod:
                                x.remove(i)

                    if y == "turma":
                        for i in x:
                            cod = int(input("Informe o código da turma que deseja excluir da lista:"))
                            if i.get("código da turma") == cod:
                                x.remove(i)

                    if y == "matricula":
                        for i in x:
                            cod = int(input("Informe o código do estudante que deseja excluir da lista de matrículas:"))
                            if i.get("código do estudante") == cod:
                                x.remove(i)
                except:
                    print("Valor inválido inserido. Tente novamente")

                with open("dados.json", "r", encoding="utf-8") as arquivo:
                        json.load(arquivo)

                with open("dados.json", "w", encoding="utf-8") as arquivo:
                    json.dump(str(estudantes + professores + disciplinas + turmas + matriculas), arquivo, ensure_ascii=False)
            else:
                print("Não há elementos cadastrados")

        # AÇÕES

        if acao_usuario == "1":  # Chamar a função de inclusão de elementos cadastrados na lista

            if opcao_usuario == "1":
                incluir(estudantes, "estudante")

            if opcao_usuario == "2":
                incluir(professores, "professor")

            if opcao_usuario == "3":
                incluir(disciplinas, "disciplina")

            if opcao_usuario == "4":
                incluir(turmas, "turma")

            if opcao_usuario == "5":
                incluir(matriculas, "matricula")

        if acao_usuario == "2":  # Chamar a função de Listagem de elementos cadastrados na lista

            if opcao_usuario == "1":
                listar(estudantes, "estudante")

            if opcao_usuario == "2":
                listar(professores, "professor")

            if opcao_usuario == "3":
                listar(disciplinas, "disciplina")

            if opcao_usuario == "4":
                listar(turmas, "turma")

            if opcao_usuario == "5":
                listar(matriculas, "matricula")

        if acao_usuario == "3":  # Chamar a função de atualização de elementos cadastrados na lista

            if opcao_usuario == "1":
                atualizar(estudantes, "estudante")

            if opcao_usuario == "2":
                atualizar(professores, "professor")

            if opcao_usuario == "3":
                atualizar(disciplinas, "disciplina")

            if opcao_usuario == "4":
                atualizar(turmas, "turma")

            if opcao_usuario == "5":
                atualizar(matriculas, "matricula")

        if acao_usuario == "4":

            if opcao_usuario == "1":
                excluir(estudantes, "estudante")

            if opcao_usuario == "2":
                excluir(professores, "professor")

            if opcao_usuario == "3":
                excluir(disciplinas, "disciplina")

            if opcao_usuario == "4":
                excluir(turmas, "turma")

            if opcao_usuario == "5":
                excluir(matriculas, "matricula")

        if acao_usuario == "9":  # Encerra o loop e por consequência o menu secundário.
            break
