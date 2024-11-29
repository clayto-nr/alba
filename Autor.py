class Autor:
    def __init__(self, nome, nacionalidade, dataNascimento):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__dataNascimento = dataNascimento

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def get_dataNascimento(self):
        return self.__dataNascimento

    def set_dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def to_dict(self):
        return {
            "nome": self.__nome,
            "nacionalidade": self.__nacionalidade,
            "dataNascimento": self.__dataNascimento
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados['nome'], dados['nacionalidade'], dados['dataNascimento'])
