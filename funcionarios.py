class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R${self.salario:.2f}")
        print("-" * 20)

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário '{funcionario.nome}' adicionado à empresa.")

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f"Funcionário '{nome}' removido da empresa.")
                return
        print(f"Funcionário '{nome}' não encontrado na empresa.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("A empresa não tem funcionários.")
        else:
            print("Funcionários na empresa:")
            for funcionario in self.funcionarios:
                funcionario.exibir_informacoes()