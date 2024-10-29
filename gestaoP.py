import os
import random
import string

def formatar_celular(celular):
    return f"({str(celular)[:2]}) {str(celular)[2:7]}-{str(celular)[7:]}"

usuarios = [
    {
        'Nome': 'adm',
        'Idade': 18,
        'Celular': formatar_celular(11945154246),
        'Email': 'adm',
        'Senha': "adm",
    },
]

produtos = [
    {
        'Nome': "agua",
        'Preço': 3.50,
        'Quantidade': 30,
        "Estoque": 10
    }
]

agenda = []

def Principal():
    while True:
        menu_t = """\033[1;34m+===================================+\033[0m
\033[1;34m| \033[1;32m         Gestão Pessoal           \033[1;34m|
\033[0m\033[1;34m+===================================+\033[0m
\033[1;34m| \033[1;33m1. Login                          \033[1;34m|
\033[0m\033[1;34m| \033[1;33m2. Criar Conta                    \033[1;34m|
\033[0m\033[1;34m| \033[1;33m0. Sair                           \033[1;34m|
\033[0m\033[1;34m+===================================+\033[0m"""
        print(menu_t)
        try:
            menu = int(input("Selecione um Número: "))
        except ValueError:
            os.system('cls')
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue
        if menu == 1:
            os.system('cls')
            login()
        elif menu == 2:
            os.system('cls')
            Cadastro_De_Usuario()
        elif menu == 0:
            print("Você saiu.")
            break

def login():
    while True:
        print("""\033[1;34m+===================================+\033[0m
\033[1;34m| \033[1;32m          Login Usuário           \033[1;34m|
\033[0m\033[1;34m+===================================+\033[0m""")
        login = input("Digite seu login (Email): ")
        senha = input("Digite sua senha: ")
        os.system('cls')

        for usuario in usuarios:
            if login == usuario['Email'] and senha == usuario['Senha']:
                print(f'\033[1;32mSeja bem-vindo, {usuario["Nome"]}!\033[0m')
                return menu_geral()
        else:
            print("\033[1;31mSenha ou Login errado.\033[0m")
            print("\033[1;31mTente novamente.\033[0m")
            return Principal()

def Cadastro_De_Usuario(nome=None, idade=None, celular=None, email=None, senha=None):
    while True:
        if nome is None:
            print("""\033[1;34m+===================================+\033[0m
\033[1;34m| \033[1;32m       Cadastro de Usuário        \033[1;34m|
\033[0m\033[1;34m+===================================+\033[0m""")
            nome = input("Nome: ")
        try:
            if idade is None:
                idade = int(input("Idade: "))
                if idade < 18 or idade >= 150:
                    print("\033[1;31mIdade inválida.\033[0m")
                    idade = None
                    continue
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue
        try:
            if celular is None:
                celular = input("Celular: ")
                if len(celular) < 11 or len(celular) > 11:
                    print("\033[1;31mQuantidade de números inválida.\033[0m")
                    celular = None
                    continue
            celular = int(celular)
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue
        if email is None:
            email = input("Email: ")
        if senha is None:
            try:
                escolha = int(input("[1] Criar sua senha [2] Gerar uma senha aleatória: "))
                if escolha == 1:
                    senha = input("Digite sua Senha: ")
                    if len(senha) < 8 or len(senha) > 20:
                        print("\033[1;31mSenha deve ter pelo menos 8 caracteres e no máximo 20 caracteres.\033[0m")
                        senha = None
                        continue
                elif escolha == 2:
                    senha = gerador_de_senha()
                else:
                    print("\033[1;31mOpção inválida! Por favor, escolha 1 ou 2.\033[0m")
                    continue
            except ValueError:
                print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
                continue
        novo_usuario = {
            'Nome': nome,
            'Idade': idade,
            'Celular': formatar_celular(celular),
            'Email': email,
            'Senha': senha,
        }
        usuarios.append(novo_usuario)

        nome = None
        idade = None
        celular = None
        email = None
        senha = None
        return login()

def gerador_de_senha():
    while True:
        try:
            print('-' * 25)
            quantos_de_numeros = int(input("Quantidade de caracteres da senha: "))
            break
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
    senha = ''
    for num in range(quantos_de_numeros):
        if random.choice([True, False]):
            senha += str(random.randint(0, 9))
        else:
            senha += random.choice(string.ascii_letters)
    print(f"\033[1;36mSenha gerada: {senha}\033[0m")
    return senha

def menu_geral():
    menu_text = """
\033[1;34m+===================================+\033[0m
\033[1;34m| \033[1;32m         Gestão Pessoal           \033[1;34m|\033[0m
\033[1;34m+===================================+\033[0m
\033[1;34m| \033[1;33m1. Cadastro de Produto            \033[1;34m|\033[0m
\033[1;34m| \033[1;33m2. Remover de Produto             \033[1;34m|\033[0m
\033[1;34m| \033[1;33m3. Exibir Produtos                \033[1;34m|\033[0m
\033[1;34m| \033[1;33m4. Calculadora Básica             \033[1;34m|\033[0m
\033[1;34m| \033[1;33m5. Calculadora de Desconto        \033[1;34m|\033[0m
\033[1;34m| \033[1;33m6. Conversor de Moedas            \033[1;34m|\033[0m
\033[1;34m| \033[1;33m7. Agenda de Compromissos         \033[1;34m|\033[0m
\033[1;34m| \033[1;33m0. Sair                           \033[1;34m|\033[0m
\033[1;34m+===================================+\033[0m
"""
    print(menu_text)
    try:
        menu = int(input("Selecione um Número: "))
    except ValueError:
        print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")

    if menu == 1:
        os.system('cls')
        Cadastro_de_Produtos()
    elif menu == 2:
        os.system('cls')
        remover_produto()
    elif menu == 3:
        os.system('cls')
        exibir_produtos()
    elif menu == 4:    
        os.system('cls')
        calculadora()
    elif menu == 5:
        os.system('cls')
        calculadora_de_Desconto()
    elif menu == 6:
        os.system('cls')
        conversor_de_moedas()
    elif menu == 7:
        os.system('cls')
        Agenda_de_Compromisso()
    elif menu == 0:
        os.system('cls')
        Principal()


def Cadastro_de_Produtos(nome=None, preco=None,quantidade=None,estoque=None):
    
    while True:

        if nome is None:
            nome = input("Digite Nome do Produto: ")

        try:
            if preco is None:
                preco = float(input("Digite o preço do Produto: "))
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue

        try:
            if quantidade is None:
                quantidade = int(input("Digite a quantidade do Produto: "))
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue

        try:
            if estoque is None:
                estoque =int(input("Digite quantidade em estoque do Produto: "))
                os.system('cls')
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue
        
        
        novo_produto = {
            'Nome': nome,
            'Preço': preco,
            'Quantidade':quantidade,
            "Estoque":estoque
            }
        
        produtos.append(novo_produto)

        nome = None
        preco = None
        quantidade = None
        estoque = None

        return menu_geral()

def remover_produto():
    print("\n\033[1;35m--- Lista de Produtos ---\033[0m")
    for indice, item in enumerate(produtos, start=1):
        print(f"\n\033[1;36mProduto {indice}:\033[0m")
        print(f"\033[1;37mNome       : {item['Nome']}\033[0m")
        print(f"\033[1;37mPreço      : R${item['Preço']:.2f}\033[0m")
        print(f"\033[1;37mQuantidade : {item['Quantidade']}\033[0m")
        print(f"\033[1;37mEstoque    : {item['Estoque']}\033[0m")
        print("\033[1;34m+-----------------------------------+\033[0m")
    print("\n\033[1;35m-----------------------------\033[0m")

    if not produtos:
        print("\n\033[1;31mNenhum produto.\033[0m")
    else:
        try:
            tirando_produto = int(input("Qual produto quer remover? "))
            if 1 <= tirando_produto <=len(produtos):
                del produtos[tirando_produto -1]
                print("\033[1;32mProduto removido com sucesso!\033[0m")
                os.system('cls')
                return menu_geral()
            else:
                print("\033[1;31mNúmero inválido!\033[0m")
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            qualquer = input("Precione qualquer tecla para voltar ao menu: ")
            os.system('cls')



def exibir_produtos():
    print("\n\033[1;35m--- Lista de Produtos ---\033[0m")
    for indice, item in enumerate(produtos, start=1):
        print(f"\n\033[1;36mProduto {indice}:\033[0m")
        print(f"\033[1;37mNome       : {item['Nome']}\033[0m")
        print(f"\033[1;37mPreço      : R${item['Preço']:.2f}\033[0m")
        print(f"\033[1;37mQuantidade : {item['Quantidade']}\033[0m")
        print(f"\033[1;37mEstoque    : {item['Estoque']}\033[0m")
        print("\033[1;34m+-----------------------------------+\033[0m")
    print("\n\033[1;35m-----------------------------\033[0m")

    qualquer = input("Precione qualquer tecla para voltar ao menu: ")
    os.system('cls')
    return menu_geral()


def calculadora():
    def operacao(num1, num2, escolha):
        if escolha == 1:
            return f"{num1} + {num2} = {num1 + num2}"
        elif escolha == 2:
            return f"{num1} - {num2} = {num1 - num2}"
        elif escolha == 3:
            return f"{num1} * {num2} = {num1 * num2}"
        elif escolha == 4:
            if num2 == 0:
                return "\033[1;31mErro: Divisão por zero não é permitida.\033[0m"      
            return f"{num1} / {num2} = {num1 / num2}"
    
    while True:
        print("\033[1;34m+===================================+\033[0m")
        print("\033[1;34m| \033[1;32m         Calculadora              \033[1;34m|\033[0m")
        print("\033[1;34m+===================================+\033[0m")
        print("\033[1;34m| \033[1;33m1. Soma (+)                       \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m2. Subtração (-)                  \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m3. Multiplicação (*)              \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m4. Divisão (/)                    \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m0. Sair da calculadora            \033[1;34m|\033[0m")
        print("\033[1;34m+===================================+\033[0m")
        try:
            escolha = int(input("Escolha uma Operação: "))
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, Digite somente operadores válidos.\033[0m")
            continue
        
        if escolha not in range(5):
            print("Operador inválido")
            continue

        if escolha == 0:
            os.system('cls')
            menu_geral()
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("\033[1;31mNúmero ou Operador inválido.\033[0m")
            continue
        
        print(f"\033[1;36m{operacao(num1, num2, escolha)}\033[0m")

        qualquer = input("Precione qualquer tecla para voltar ao menu:")
        os.system('cls')
        
def calculadora_de_Desconto():
    while True:
        for indice, item in enumerate(produtos, start=1):
            print("\033[1;34m+==============================+\033[0m")
            print(f"\033[1;36m| Produto {indice:<21}|\033[0m")
            print("\033[1;34m+==============================+\033[0m")
            print(f"\033[1;37m| Nome       : {item['Nome']:<16}|\033[0m")
            print(f"\033[1;37m| Preço      : R${item['Preço']:<14.2f}|\033[0m")
            print(f"\033[1;37m| Quantidade : {item['Quantidade']:<16}|\033[0m")
            print(f"\033[1;37m| Estoque    : {item['Estoque']:<16}|\033[0m")
            print("\033[1;34m+==============================+\033[0m")
        
        tirando_item = int(input("Qual item deseja editar o valor para o desconto? (0 voltar ao menu) ")) - 1
        
        if tirando_item == -1:
            menu_geral()
        
        if 0 <= tirando_item < len(produtos):
            valor = produtos[tirando_item]['Preço']
            v_desconto = float(input("Valor do desconto (%) "))
            desconto_final = valor - (valor * v_desconto / 100)
            produtos[tirando_item]['Preço'] = desconto_final
            
            print(f"O produto que custava R${valor:.2f}\n"
                  f"na promoção com desconto de {v_desconto}% vai custar R${desconto_final:.2f}")
        else:
            print("\033[1;31mItem inválido. Tente novamente.\033[0m")
        
    

def conversor_de_moedas(escolha=None, subescolha=None, valor=None):
    taxas = {
        'USD': 5.53,
        'EUR': 6.20,
        'ARS': 0.027,
        'JPY': 0.038
    }

    while True:
        print("\033[1;34m+===================================+\033[0m")
        print("\033[1;34m| \033[1;32m       Conversor de Moedas        \033[1;34m|\033[0m")
        print("\033[1;34m+===================================+\033[0m")
        print("\033[1;34m| \033[1;33m1. Dólar ($)                      \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m2. Euro (€)                       \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m3. Peso Argentino (ARS$)          \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m4. Iene Japonês (¥)               \033[1;34m|\033[0m")
        print("\033[1;34m| \033[1;33m0. Voltar ao Menu                 \033[1;34m|\033[0m")
        print("\033[1;34m+===================================+\033[0m")
        
        try:
            escolha = int(input("Qual moeda deseja converter: "))
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue

        if escolha not in range(5):
            print("\033[1;31mOpção inválida! Por favor, Digite somente de 0 a 4.\033[0m")
            continue

        if escolha == 0:
            os.system('cls')
            menu_geral()


        moedas = ['USD', 'EUR', 'ARS', 'JPY']
        moeda_escolhida = moedas[escolha - 1]

        print(f".1 Real para {moeda_escolhida}\n2. {moeda_escolhida} para Real")
        
        try:
            subescolha = int(input("Escolha 1 ou 2: "))
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue

        if subescolha not in range(1, 3):
            print("Inválido. Digite somente 1 ou 2.")
            continue

        try:
            valor = float(input(f"Digite o valor em {'Reais (R$)' if subescolha == 1 else moeda_escolhida}: "))
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue

        if subescolha == 1:
            convertido = valor / taxas[moeda_escolhida]
            print(f"\033[1;36mReal R${valor} convertido fica {moeda_escolhida} {convertido:.2f}\033[0m")
        elif subescolha == 2:
            convertido = valor * taxas[moeda_escolhida]
            print(f"\033[1;36m{moeda_escolhida} {valor} convertido fica R${convertido:.2f}\033[0m")

        return menu_geral()

def Agenda_de_Compromisso(data=None, hora=None, compromisso=None):
    while True:
        print("\n\033[1;34m==============================\033[0m")
        print("\033[1;32m    AGENDA DE COMPROMISSOS\033[0m")
        print("\033[1;34m==============================\033[0m")
        print("\033[1;33m1. Adicionar Compromisso\033[0m")
        print("\033[1;33m2. Remover Compromisso\033[0m")
        print("\033[1;33m3. Ver Compromissos\033[0m")
        print("\033[1;33m4. Marcar Compromisso como Feito\033[0m")
        print("\033[1;33m0. Voltar ao menu Principal\033[0m")
        print("\033[1;34m==============================\033[0m")
        
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
            continue

        if escolha == 1:
            os.system('cls')
            if data is None:
                data = input("Digite a data (dd/mm/aaaa): ")

            if hora is None:
                hora = input("Digite a hora (hh:mm): ")
                
            if compromisso is None:
                compromisso = input("Digite o compromisso: ")

            novo_compromisso = {
                'Data': data,
                'Hora': hora,
                'Compromisso': compromisso,
                'Status': 'Pendente'
            }

            agenda.append(novo_compromisso)

            data = None
            hora = None 
            compromisso = None
            os.system('cls')

        elif escolha == 2:
            if not agenda:
                print("\n\033[1;31mNenhum compromisso agendado.\033[0m")
            else:
                os.system('cls')
                print("\n\033[1;35m--- Lista de Compromissos ---\033[0m")
                for indice, infos in enumerate(agenda, start=1):
                    print(f"\n\033[1;36mCompromisso {indice}:\033[0m")
                    print(f"\033[1;37mData       : {infos['Data']}\033[0m")
                    print(f"\033[1;37mHora       : {infos['Hora']}\033[0m")
                    print(f"\033[1;37mCompromisso: {infos['Compromisso']}\033[0m")
                    print(f"\033[1;37mStatus     : {infos['Status']}\033[0m")
                print("\n\033[1;35m-----------------------------\033[0m")

                try:
                    tirando_compromisso = int(input("Qual compromisso quer remover? "))
                    if 1 <= tirando_compromisso <= len(agenda):
                        del agenda[tirando_compromisso - 1]
                        print("\033[1;32mCompromisso removido com sucesso!\033[0m")
                    else:
                        print("\033[1;31mNúmero inválido!\033[0m")
                except ValueError:
                    print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
                qualquer = input("Precione qualquer tecla para voltar ao menu: ")
                os.system('cls')


        elif escolha == 3:
            if not agenda:
                print("\n\033[1;31mNenhum compromisso agendado.\033[0m")
            else:
                os.system('cls')
                print("\n\033[1;35m--- Lista de Compromissos ---\033[0m")
                for indice, infos in enumerate(agenda, start=1):
                    print(f"\n\033[1;36mCompromisso {indice}:\033[0m")
                    print(f"\033[1;37mData       : {infos['Data']}\033[0m")
                    print(f"\033[1;37mHora       : {infos['Hora']}\033[0m")
                    print(f"\033[1;37mCompromisso: {infos['Compromisso']}\033[0m")
                    print(f"\033[1;37mStatus     : {infos['Status']}\033[0m")
                print("\n\033[1;35m-----------------------------\033[0m")

                qualquer = input("Precione qualquer tecla para voltar ao menu: ")
                os.system('cls')




        elif escolha == 4:
            if not agenda:
                os.system('cls')
                print("\n\033[1;31mNenhum compromisso agendado.\033[0m")
            else:
                
                for indice, infos in enumerate(agenda, start=1):
                    print(f"\n\033[1;36mCompromisso {indice}:\033[0m")
                    print(f"\033[1;37mData       : {infos['Data']}\033[0m")
                    print(f"\033[1;37mHora       : {infos['Hora']}\033[0m")
                    print(f"\033[1;37mCompromisso: {infos['Compromisso']}\033[0m")
                    print(f"\033[1;37mStatus     : {infos['Status']}\033[0m")
                
                try:
                    indice = int(input("Digite o número do compromisso que deseja marcar como feito: "))
                    if 1 <= indice <= len(agenda):
                        agenda[indice - 1]['Status'] = 'Feito'
                        print("\033[1;32mCompromisso marcado como feito!\033[0m")
                    else:
                        print("\033[1;31mNúmero inválido!\033[0m")
                except ValueError:
                    print("\033[1;31mOpção inválida! Por favor, digite um número.\033[0m")
                
                qualquer = input("Precione qualquer tecla para voltar ao menu: ")
                os.system('cls')    

        elif escolha == 0:
            os.system('cls')
            menu_geral()

        else:
            print("\033[1;31mOpção inválida! Por favor, escolha uma opção válida.\033[0m")

Principal()