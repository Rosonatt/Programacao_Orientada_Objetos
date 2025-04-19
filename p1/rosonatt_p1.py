class Cadastrar_Pessoa: #classe  de cadastro de pessoas
    def __init__(self, nome, instituicao, cpf):
        self.nome = nome
        self.instituicao = instituicao
        self.cpf = cpf
        
    @property #encapsulamento em poprety
    def cpf(self):
        return self._cpf

    @cpf.setter # encapsulamento em setter
    def cpf(self, valor):
        if not len(valor) == 11 or not valor.isdigit():
            raise ValueError(" o cpf prescisa ter 11 digitos, caso não tenha sera invalido!!")
        self._cpf = valor

    def resumo(self): # resumo do nome e da instutuição
        return f"{self.nome} ({self.instituicao})"

class cadastrar_sala: #ccadastra sala
    def __init__(self, nome, local, capacidade):
        self.nome = nome
        self.local = local
        self.capacidade = capacidade

    def resumo(self):
        return f"{self.nome} - {self.local}"

class Agendamento: # classe de agendamento
    def __init__(self):
        self.agendamentos = []

    def add(self, pessoa, sala, data):
        self.agendamentos.append({
            'pessoa': pessoa,
            'sala': sala,
            'data': data
        })

    def todos(self): #retorna todos os agendamentos
        return [f"{a['pessoa'].resumo()} -> {a['sala'].resumo()} ({a['data']})" 
                for a in self.agendamentos]

    def cada_sala(self, nome_sala): # retorna por sala
        return [a for a in self.agendamentos if a['sala'].nome == nome_sala]

    def cada_pessoa(self, cpf): #retorna por pessoa
        return [a for a in self.agendamentos if a['pessoa'].cpf == cpf]

# alguns cadastros ja  feitos
p1 = Cadastrar_Pessoa("Rosonatt", "UVA", "16511897737")
p2 = Cadastrar_Pessoa("Diego", "UniVassouras", "16611997838")
l1 = cadastrar_sala("Lab 1", "campus 2", 87)
l2 = cadastrar_sala("Lab 2", "Campus 3", 56)

#exibe  os agendamentos
ag = Agendamento()
ag.add(p1, l1, "08/02/1995 09:30")
ag.add(p2, l2, "27/06/1996 10:00")

print("todos os agendamentos até o momento são:")
for r in ag.todos():
    print(r)

print("\nagendamentos no campus 2:")
for r in ag.cada_sala("campus 2"):
    print(f"{r['pessoa'].nome} - {r['data']}")

print("\nagendamentos de Diego:")
for r in ag.cada_pessoa("16611997838"):
    print(f"{r['sala'].nome} - {r['data']}")



 

