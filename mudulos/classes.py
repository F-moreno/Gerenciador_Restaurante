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
    def __init__(self, categoria: str, nome: str, telefone: str, email: str) -> None:
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
    """{categoria: str = 'Cliente',
    nome: str,
    telefone: str,
    email: str}"""

    id = 1

    def __init__(self, *args) -> None:
        super().__init__("Cliente", *args)
        self.id, Cliente.id = Cliente.id, Cliente.id + 1


class Funcionario(Pessoa):
    """{categoria: str = 'Funcionario',
    nome: str,
    telefone: str,
    email: str}"""

    id = 1

    def __init__(self, *args) -> None:
        super().__init__("Funcionário", *args)
        self.id, Funcionario.id = Funcionario.id, Funcionario.id + 1

    def definirSalario(self, salario: float) -> None:
        """Redefine salario do funcionário."""
        self.salario = salario

    def definirAdmissao(self, data_admissao: float) -> None:
        """Define data de admissão do funcionário"""
        self.salario = data_admissao


class Dependente(Pessoa):
    """{responsavel: Funcionario,
    parentesco:str,
    categoria: str = 'Dependente',
    nome: str,
    telefone: str,
    email: str}"""

    id = 1

    def __init__(self, responsavel: Funcionario, parentesco: str, *args) -> None:
        super().__init__("Dependente", *args)
        self.id, Dependente.id = Dependente.id, Dependente.id + 1
        self.responsavel = responsavel
        self.parentesco = parentesco

    def __str__(self):
        return f"Meu nome é {self.nome} e sou {self.categoria} do funcionario {getattr(self.responsavel, 'nome')} deste Restaurante."


class Recepcionista(Funcionario):
    """{categoria: str = 'Recepcionista',
    nome: str,
    telefone: str,
    email: str}"""

    id = 1

    def __init__(self, *args) -> None:
        super().__init__("Recepcionista", *args)

    def ocuparMesa(self, cliente: Cliente, mesa: Mesa, data: str):
        pass


class Cozinheiro(Funcionario):
    def __init__(self, *args) -> None:
        super().__init__("Cozinheiro", *args)

    def fecharComanda(self, id_comanda: int):
        pass


class Garcon(Funcionario):
    def __init__(self, *args) -> None:
        super().__init__("Garçon", *args)

    def abrirComanda(self, cliente: Cliente, mesa: Mesa, data: str):
        pass


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
