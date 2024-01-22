from __future__ import annotations

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

    def __init__(self,funcao, *args) -> None:
        super().__init__("Funcionário", *args)
        self.id, Funcionario.id = Funcionario.id, Funcionario.id + 1
        self.funcao = funcao

    def definirSalario(self, salario: float) -> None:
        """Redefine salario do funcionário."""
        self.salario = salario

    def definirAdmissao(self, data_admissao: float) -> None:
        """Define data de admissão do funcionário"""
        self.salario = data_admissao

    def __str__(self):
        return super().__str__()+f" Função: {self.funcao}"


class Dependente(Pessoa):
    """{responsavel: Funcionario,
    parentesco:str,
    categoria: str = 'Dependente',
    nome: str,
    telefone: str,
    email: str}"""

    id = 1

    def __init__(self, id_responsavel: int, parentesco: str, *args) -> None:
        super().__init__("Dependente", *args)
        self.id, Dependente.id = Dependente.id, Dependente.id + 1
        self.id_responsavel = id_responsavel
        self.parentesco = parentesco

    def __str__(self):
        return f"Meu nome é {self.nome} e sou {self.categoria} do funcionario id:{self.id_responsavel} deste Restaurante."


class Recepcionista(Funcionario):
    """{categoria: str = 'Recepcionista',
    nome: str,
    telefone: str,
    email: str}"""
    def __init__(self, *args) -> None:
        super().__init__("Recepcionista", *args)


class Cozinheiro(Funcionario):
    """{categoria: str = 'Cozinheiro',
    nome: str,
    telefone: str,
    email: str}"""

    def __init__(self, *args) -> None:
        super().__init__("Cozinheiro", *args)


class Garcon(Funcionario):
    """{categoria: str = 'Garcon',
    nome: str,
    telefone: str,
    email: str}"""


    def __init__(self, *args) -> None:
        super().__init__("Garçon", *args)


class Reserva:
    id = 1

    def __init__(
        self,
        id_recepicionista: int,
        id_mesa: int,
        id_cliente: int,
        data: str,
        hora: str,
    ) -> None:
        self.id, Reserva.id = Reserva.id, Reserva.id + 1
        self.id_recepicionista = id_recepicionista
        self.id_mesa = id_mesa
        self.id_cliente = id_cliente
        self.data = data
        self.hora = hora
        self.status = "Aberto"

    def cancelarReserva(self) -> None:
        self.status = "Cancelado"

    def finalizarReserva(self) -> None:
        self.status = "Finalizado"


class Mesa:
    id = 1

    def __init__(self, capacidade: int) -> None:
        self.id, Mesa.id = Mesa.id, Mesa.id + 1
        self.capacidade = capacidade
        self.status = "Vazia"
        self.comanda = []
        self.id_cliente = None
        self.conta = 0

    def inserirCliente(self, id_cliente: int):
        self.id_cliente = id_cliente
        self.status = "Ocupado"

    def inserirComanda(self, comanda: Comanda):
        self.comanda.append(comanda)
        self.conta += comanda.subtotal

    def inativarMesa(self):
        if self.status == "Ocupado":
            raise ValueError("Não é possivel inativar uma mesa ocupada!")
        self.status = "Inativo"

    def finalizarMesa(self):
        return Conta(self.comanda)


class Comanda:
    id = 1

    def __init__(self, id_garcon: int):
        self.id, Comanda.id = Comanda.id, Comanda.id + 1
        self.id_garcon = id_garcon
        self.id_cozinheiro = None
        self.itemPedido = []
        self.status = "Aberta"
        self.total = 0

    def abrirComanda(self, prato, quantidade):
        self.itemPedido(ItemPedido(prato, quantidade))

    def fecharComanda(self, id_cozinheiro: int):
        self.id_cozinheiro = id_cozinheiro
        self.status = "Finalizada"
        for i in self.itemPedido:
            self.total += i.subtotal


class ItemPedido:
    def __init__(self, prato: Prato, quantidade: int):
        self.prato = prato
        self.quantidade = quantidade
        self.sub_total = quantidade * prato.valor


class Prato:
    id = 1

    def __init__(self, nome: str, valor: float, descricao: str):
        self.id, Prato.id = Prato.id, Prato.id + 1
        self.nome = nome
        self.valor = valor
        self.descricao = descricao


if __name__ == "__main__":
    """Bloco temporário para testes"""
    cliente1 = Cliente(
        "Marcotti",
        "123456789",
        "joao@email.com",
    )
    funcionario1 = Recepcionista(
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
