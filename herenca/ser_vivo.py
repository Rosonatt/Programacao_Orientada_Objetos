class Ser_vivo:
    def __init__(self, genero, alimentacao, altura):
        self.genero = genero
        self.alimentacao = alimentacao
        self.altura = altura

class Humano(Ser_vivo):
    def __init__(self, nome, idade, altura, alimentacao, cpf, genero):
        super().__init__(genero, alimentacao, altura)
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def apresentar(self):
        return (f"\nNome: {self.nome}, Idade: {self.idade}, Altura: {self.altura},\n"
                f"Gênero: {self.genero}, Alimentação: {self.alimentacao}, CPF: {self.cpf}")

class Estudante(Humano):
    def __init__(self, nome, idade, altura, alimentacao, cpf, genero, curso):
        super().__init__(nome, idade, altura, alimentacao, cpf, genero)
        self.curso = curso

    def apresentar(self):
        base = super().apresentar()
        return f"{base}, Curso: {self.curso}"

ser_1 = Humano('Rosonatt', 30, 1.78, 'Carnivoro', '123456789', 'Masculino')
print(ser_1.apresentar())

student = Estudante('Ryan', 21, 1.81, 'Onívora', '987654321', 'Boyceta', 'Engenharia de Software')
print(student.apresentar())
