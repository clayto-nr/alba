import json
from Autor import Autor
from Livro import Livro
import time
import os

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionarLivro(self, livro):
        self.__livros.append(livro)

    def removerLivro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                self.__livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def buscarLivro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                print(f"Livro encontrado: {livro.get_titulo()}, Autor: {livro.get_autor().get_nome()}, Ano: {livro.get_anoPublicacao()}")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def listarLivros(self):
        if not self.__livros:
            print("Nenhum livro disponível na biblioteca.")
        else:
            print("Lista de Livros na Biblioteca:")
            for livro in self.__livros:
                print(f"- {livro.get_titulo()} ({livro.get_anoPublicacao()}), Autor: {livro.get_autor().get_nome()}")

    def salvarEmJson(self, arquivo):
        objetos_dict = [livro.to_dict() for livro in self.__livros]
        dados_em_json = json.dumps(objetos_dict, indent=4)
        try:
            with open(arquivo, 'w') as f:
                f.write(dados_em_json)
            print(f"💾 Dados salvos em {arquivo} com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregarDeJson(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                
                for livro_dict in dados:
                    autor = Autor(**livro_dict['autor'])
                    livro = Livro(livro_dict['titulo'], autor, livro_dict['anoPublicacao'])
                    self.adicionarLivro(livro)

            print("\n📚 LIVROS CARREGADOS COM SUCESSO!")
            for livro in self.__livros:
                print(f" - Título: {livro.get_titulo()}, Autor: {livro.get_autor().get_nome()}, Ano de Publicação: {livro.get_anoPublicacao()}")
                
        except FileNotFoundError:
            print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        except json.JSONDecodeError:
            print(f"Erro: O arquivo '{arquivo}' não contém dados válidos.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

def animar_texto(texto, cor="\033[1;92m"):
    for char in texto:
        print(f"{cor}{char}\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

biblioteca = Biblioteca()
opcao = "0"

while opcao != "7":
    limpar_tela()
    animar_texto("\n📚 BEM-VINDO AO MENU DA BIBLIOTECA 📚\n", cor="\033[1;96m")

    print("\033[1;31m1.\033[1;92m ADICIONAR LIVRO 📖\033[0m")
    print("\033[1;31m2.\033[1;92m REMOVER LIVRO ❌\033[0m")
    print("\033[1;31m3.\033[1;92m BUSCAR LIVRO 🔍\033[0m")
    print("\033[1;31m4.\033[1;92m LISTAR LIVROS 📚\033[0m")
    print("\033[1;31m5.\033[1;92m SALVAR DADOS DOS LIVROS EM ARQUIVO 💾\033[0m")
    print("\033[1;31m6.\033[1;92m CARREGAR DADOS DOS LIVROS DO ARQUIVO 📂\033[0m")
    print("\033[1;31m7.\033[1;92m SAIR 🚪\033[0m")
    
    animar_texto("ESCOLHA UMA OPÇÃO: ", cor="\033[1;92m")
    opcao = input()

    if opcao == "1":
        animar_texto("📖 ADICIONANDO UM NOVO LIVRO...\n", cor="\033[1;93m")
        titulo = input("Digite o título do livro: ")
        nome_autor = input("Digite o nome do autor: ")
        nacionalidade_autor = input("Digite a nacionalidade do autor: ")
        data_nascimento_autor = input("Digite a data de nascimento do autor (formato DD/MM/AAAA): ")
        autor = Autor(nome_autor, nacionalidade_autor, data_nascimento_autor)
        ano_publicacao = input("Digite o ano de publicação: ")
        livro = Livro(titulo, autor, ano_publicacao)
        biblioteca.adicionarLivro(livro)
        animar_texto(f"Livro '{titulo}' adicionado com sucesso!\n", cor="\033[1;92m")

    elif opcao == "2":
        animar_texto("❌ REMOVENDO UM LIVRO...\n", cor="\033[1;93m")
        titulo = input("Digite o título do livro a ser removido: ")
        biblioteca.removerLivro(titulo)

    elif opcao == "3":
        animar_texto("🔍 BUSCANDO UM LIVRO...\n", cor="\033[1;93m")
        titulo = input("Digite o título do livro para buscar: ")
        biblioteca.buscarLivro(titulo)

    elif opcao == "4":
        animar_texto("📚 LISTANDO TODOS OS LIVROS...\n", cor="\033[1;93m")
        biblioteca.listarLivros()

    elif opcao == "5":
        arquivo = input("\033[1;92mDIGITE O NOME DO ARQUIVO PARA SALVAR OS DADOS: \033[0m")
        biblioteca.salvarEmJson(arquivo)

    elif opcao == "6":
        arquivo = input("\033[1;92mDIGITE O NOME DO ARQUIVO PARA CARREGAR OS DADOS: \033[0m")
        biblioteca.carregarDeJson(arquivo)

    elif opcao == "7":
        animar_texto("🚪 SAINDO DO SISTEMA... ATÉ LOGO! 👋\n", cor="\033[1;92m")

    else:
        animar_texto("❌ OPÇÃO INVÁLIDA, TENTE NOVAMENTE.\n", cor="\033[1;91m")
    time.sleep(1.5)
