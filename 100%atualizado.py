print("Manual de Uso da Lista de Compras:")
print("Link para o manual completo: https://www.canva.com/design/DAGViELkgWk/LE5A-2ylL45npgNNPsU-5g/edit?utm_content=DAGViELkgWk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
print("-" * 60)
# LISTA DE COMPRAS POR CATEGORIA
lista_compras = {
    'Limpeza': [],
    'Carnes': [],
    'Perecivel': [],
    'Frutas e Legumes': [],
    'Higiene Pessoal': [],
    'Bebidas': [],
}

# FUNÇÃO PARA VERIFICAR SE UM PRODUTO ESTÁ NA LISTA
def verificar_produto(nome):
    for categoria, produtos in lista_compras.items():
        for produto in produtos:
            if produto["produto"] == nome:
                return True
    return False


# FUNÇÃO PARA REMOVER UM PRODUTO DA LISTA
def remover_produto():
    categorias_com_produtos = [categoria for categoria in lista_compras if lista_compras[categoria]]
    if not categorias_com_produtos:
        print("Não há categorias com produtos disponíveis para remover.")
        return

    print('Categorias disponíveis com produtos:')
    for i, categoria in enumerate(categorias_com_produtos, start=1):
        print(f"{i}. {categoria}")
    print("0. Voltar ao menu principal")

    while True:
        try:
            escolha_categoria = int(input('Escolha a categoria do produto a ser removido ou "0" para cancelar: '))
            if escolha_categoria == 0:
                print("Operação cancelada. Retornando ao menu principal.")
                return
            elif 1 <= escolha_categoria <= len(categorias_com_produtos):
                categoria_selecionada = categorias_com_produtos[escolha_categoria - 1]
                break
            else:
                print('Escolha um número válido.')
        except ValueError:
            print('Entrada inválida. Por favor, escolha um número.')

    print('Produtos disponíveis:')
    for i, produto in enumerate(lista_compras[categoria_selecionada], start=1):
        print(f"{i}. {produto['produto']} (Quantidade: {produto['quantidade']})")
    print("0. Voltar ao menu principal")

    while True:
        try:
            escolha_produto = int(input('Escolha o número do produto que deseja remover ou "0" para cancelar: '))
            if escolha_produto == 0:
                print("Operação cancelada. Retornando ao menu principal.")
                return
            elif 1 <= escolha_produto <= len(lista_compras[categoria_selecionada]):
                produto_a_remover = lista_compras[categoria_selecionada][escolha_produto - 1]
                confirmacao = input(
                    f"Tem certeza de que deseja remover '{produto_a_remover['produto']}'? (sim ou não): ").strip().lower()
                if confirmacao == "sim":
                    lista_compras[categoria_selecionada].remove(produto_a_remover)
                    print(f"{produto_a_remover['produto']} foi removido com sucesso.")
                else:
                    print("Operação cancelada.")
                break
            else:
                print('Escolha um número válido.')
        except ValueError:
            print('Entrada inválida. Por favor, escolha um número.')
    # FUNÇÃO PARA EXIBIR LISTA
def exibir_lista():
    # VERIFICA SE HÁ ALGUM PRODUTO NA LISTA DE COMPRAS
    lista_vazia = all(not produtos for produtos in lista_compras.values())

    # SE A LISTA ESTIVER VAZIA EXIBIR MENSAGEM E VOLTA.
    if lista_vazia:
        print('╔════════════════════════════════╗')
        print('║ A lista de compras está vazia. ║')
        print('╚════════════════════════════════╝')
        return

    # EXIBE OS PRODUTOS EM CADA LISTA
    for categoria, produtos in lista_compras.items():
        print(f"Categoria: {categoria}")

        # VERIFICA SE HÁ PRODUTOS EM CADA CATEGORIA.
        if produtos:
            for produto in produtos:
                print(f"{produto['produto']} (Quantidade: {produto['quantidade']})")
        else:
            print("Nenhum produto.")

        print()


# FUNÇÃO PARA RENOMEAR PRODUTO
def renomear_produto():
    categorias_com_produtos = [categoria for categoria in lista_compras if lista_compras[categoria]]

    if not categorias_com_produtos:
        print("Não há categorias com produtos disponíveis para renomear.")
        return

    print('Categorias disponíveis com produtos:')
    for i, categoria in enumerate(categorias_com_produtos, start=1):
        print(f"{i}. {categoria}")

    while True:
        try:
            escolha_categoria = int(input('Escolha a categoria do produto a ser renomeado: '))
            if 1 <= escolha_categoria <= len(categorias_com_produtos):
                categoria_selecionada = categorias_com_produtos[escolha_categoria - 1]
                break
            else:
                print('Escolha um número válido.')
        except ValueError:
            print('Entrada inválida. Por favor, escolha um número.')

    print('Produtos disponíveis:')
    for i, produto in enumerate(lista_compras[categoria_selecionada], start=1):
        print(f"{i}. {produto['produto']} (Quantidade: {produto['quantidade']})")

    while True:
        try:
            escolha_produto = int(input('Escolha o número do produto que deseja renomear: '))
            if 1 <= escolha_produto <= len(lista_compras[categoria_selecionada]):
                produto_selecionado = lista_compras[categoria_selecionada][escolha_produto - 1]
                produto_antigo = produto_selecionado['produto']
                break
            else:
                print('Escolha um número válido.')
        except ValueError:
            print('Entrada inválida. Por favor, escolha um número.')

    while True:
        produto_novo = input('Digite o novo nome do produto: ')
        if produto_novo.strip() and produto_novo.replace(" ", "").isalpha():
            produto_selecionado['produto'] = produto_novo 
            print(f"{produto_antigo} foi renomeado para {produto_novo}.")
            break
        else:
            print("O nome do produto deve conter apenas letras e não pode estar vazio. Tente novamente.")


# FUNÇÃO PARA ADICIONAR UM PRODUTO

def adicionar_produto():
    while True:
        print('╔══════════════════════════════╗')
        print('║         CATEGORIAS           ║')
        print('╠══════════════════════════════╣')
        print('║ 1. Limpeza                   ║')
        print('║ 2. Carnes                    ║')
        print('║ 3. Perecivel                 ║')
        print('║ 4. Frutas e Legumes          ║')
        print('║ 5. Higiene Pessoal           ║')
        print('║ 6. Bebidas                   ║')
        print('║ 7. Voltar                    ║')
        print('╚══════════════════════════════╝')
        # Opções
        escolha_categoria = input('Escolha a categoria do seu produto (1-7): ')

        if escolha_categoria == '7':
            break

        categorias = list(lista_compras.keys())
        if escolha_categoria.isdigit() and 1 <= int(escolha_categoria) <= 6:
            categoria = categorias[int(escolha_categoria) - 1]
        else:
            print("Categoria não encontrada. Tente novamente.")
            continue

        while True:
            produto = input("Informe o nome do produto: ")
            if not produto.strip() or not produto.replace(" ", "").isalpha():
                print("O nome do produto deve conter apenas letras. Tente novamente.")
            elif any(produto.lower() == item["produto"].lower() for item in lista_compras[categoria]):
                print("Este produto já existe na categoria selecionada. Tente um nome diferente.")
            else:
                break

        while True:
            try:
                quantidade = int(input("Informe a quantidade: "))
                if quantidade > 0:
                    break
                else:
                    print("A quantidade deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Quantidade inválida. Por favor, digite um número inteiro positivo.")

        lista_compras[categoria].append({"produto": produto, "quantidade": quantidade})
        print("Produto adicionado com sucesso.")


# FUNÇÃO DO MENU E INTELIGAÇÃO DE CADA FUNÇÃO A OPÇÃO.
def menu():
    while True:
        print('╔══════════════════════════════╗')
        print('║       MENU PRINCIPAL         ║')
        print('╠══════════════════════════════╣')
        print('║ 1. Adicionar Produto         ║')
        print('║ 2. Remover Produto           ║')
        print('║ 3. Exibir Lista              ║')
        print('║ 4. Renomear Produto          ║')
        print('║ 5. Sair                      ║')
        print('╚══════════════════════════════╝')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            exibir_lista()
        elif opcao == '4':
            renomear_produto()
        elif opcao == '5':
            print('Saindo da lista. Até mais!')
            break
        else:
            print('Opção Inválida. Tente novamente.')
menu()


