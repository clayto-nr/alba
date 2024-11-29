from Autor import Autor

class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_anoPublicacao(self):
        return self.__anoPublicacao

    def set_anoPublicacao(self, anoPublicacao):
        self.__anoPublicacao = anoPublicacao

    def to_dict(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor.to_dict(),
            "anoPublicacao": self.__anoPublicacao
        }

    @classmethod
    def from_dict(cls, dados):
        autor = Autor.from_dict(dados['autor'])
        return cls(dados['titulo'], autor, dados['anoPublicacao'])
