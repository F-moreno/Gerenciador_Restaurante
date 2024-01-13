"""Aqui serão Implementadas todas as classes do sistema"""


# Informações importantes:
#
# todas as classes que possuirem id terão a seguinte extrutura
# para controlar o id durante a criação:
#
# self.id, Classe.id = Classe.id, Classe.id+1
#
# Nomeação Composta
#
# NomeComposto : classe
# nomeComposto : function
# nome_composto : variavel
class Pessoa:
    id = 1

    def __init__(self, categoria: str, nome: str, telefone: str, email: str) -> None:
        self.id, Pessoa.id = Pessoa.id, Pessoa.id + 1
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.categoria = categoria

    def __str__(self):
        return f"Meu nome é {self.nome} e sou {self.categoria} deste Restaurante."

    # def validarNome(nome: str) -> str:
    #     pass

    # def validarTelefone(tel: str) -> str:
    #     pass

    # def validarEmail(email: str) -> str:
    #     pass


class Cliente(Pessoa):
    """Classe Cliente extende a classe Pessoa"""

    def __init__(self, *args) -> None:
        super().__init__("Cliente", *args)


class Funcionario(Pessoa):
    """Classe Funcionario extende a classe Pessoa"""

    def __init__(self, *args) -> None:
        super().__init__("Funcionario", *args)

    def definirSalario(self, salario: float) -> None:
        """Redefine salario do funcionário."""
        self.salario = salario

    def definirAdmissao(self, data_admissao: float) -> None:
        """Define data de admissão do funcionário"""
        self.salario = data_admissao


class Dependente(Pessoa):
    def __init__(self, responsavel: Funcionario, parentesco: str, *args) -> None:
        super().__init__("Dependente", *args)
        self.responsavel = responsavel
        self.parentesco = parentesco

    def __str__(self):
        return f"Meu nome é {self.nome} e sou {self.categoria} do funcionario {getattr(self.responsavel, 'nome')} deste Restaurante."


class Recepcionista(Funcionario):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def fazerReserva(self,cliente:Cliente,mesa: Mesa, data:str):


if __name__ == "__main__":
    """Bloco temporário para testes"""
    cliente1 = Cliente(
        "Marcotti",
        "123456789",
        "joao@email.com",
    )
    funcionario1 = Funcionario(
        "Fernando",
        "987654321",
        "fernando@email.com",
    )
    dependente1 = Dependente(
        funcionario1,
        "Conjuge",
        "Ana",
        "987654321",
        "Ana@email.com",
    )

    print(cliente1)
    print(funcionario1)
    print(dependente1)
