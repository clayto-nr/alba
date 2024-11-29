import json
from Autor import Autor
from Livro import Livro

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
