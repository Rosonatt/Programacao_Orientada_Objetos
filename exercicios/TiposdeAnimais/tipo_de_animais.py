class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome  
        self.tipo = tipo  
    
    def apresentando(self):
        print(f"aqui temos  o {self.nome}, um animal {self.tipo}!")
    
    def movimentacao(self):
        if self.tipo == "terrestre":
            print(f"{self.nome} consegue andar e também correr ou nadar!")
        elif self.tipo == "marinho":
            print(f"{self.nome} consegue nadar! Alguns podem pulaar, mas não conseguem andar.")
        elif self.tipo == "voador":
            print(f"{self.nome} conseguem voar! Podem andar , mas não conseguem  correr.")
        else:
            print("Esse tipo de animal não pode ser indetificado!")

class Ani_Terrestre(Animal):
    def __init__(self, nome, consegue_correr, consegue_nadar):
        super().__init__(nome, "terrestre")
        self.consegue_correr = consegue_correr
        self.consegue_nadar = consegue_nadar
    
    def movimentacao(self):
        habilidades = [f"{self.nome} anda"]
        if self.consegue_correr:
            habilidades.append("corre")
        if self.consegue_nadar:
            habilidades.append("nada")
        print(", ".join(habilidades) + "!")

class Ani_Marinho(Animal):
    def __init__(self, nome, consegue_pular):
        super().__init__(nome, "marinho")
        self.consegue_pular = consegue_pular
    
    def movimentacao(self):
        if self.consegue_pular:
            print(f"{self.nome} consegue nadar e as também consegue pular!")
        else:
            print(f"{self.nome} consegue nadar mas não consegue pular.")

class Ani_Voador(Animal):
    def __init__(self, nome, consegue_andar):
        super().__init__(nome, "voador")
        self.consegue_andar = consegue_andar
    
    def movimentacao(self):
        if self.consegue_andar:
            print(f"{self.nome} consegue voar, mas não consegue correr.")
        else:
            print(f"{self.nome} consegue apenas voar, não consegue andar  .")

tigre = Ani_Terrestre("Tigre", True, False)
sapo = Ani_Terrestre("Sapo", False, True)
baleia = Ani_Marinho("Baleia", True)
peixe= Ani_Marinho("Peixe", False)
coruja = Ani_Voador("Coruja", True)
borboleta = Ani_Voador("Mosquito", False)

tigre.apresentando()
tigre.movimentacao()


sapo.apresentando()
sapo.movimentacao()

baleia.apresentando()
baleia.movimentacao()


peixe.apresentando()
peixe.movimentacao()


coruja.apresentando()
coruja.movimentacao()


borboleta.apresentando()
borboleta.movimentacao()