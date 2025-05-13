class Automovel:
    def ligar(self):
        raise NotImplementedError(" o metodo 'ligar' não foi implementado")
    
    def desligar(self):
        raise NotImplementedError(" metodo 'desligar' não foi implementado")
    
    def acelerar(self, velocidade):
        print(f" esta acelerando para {velocidade} km/h")

class Moto(Automovel):
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            print(f"moto {self.modelo} ligada")
            self.ligado = True
        else:
            print(f"moto {self.modelo} já está ligada")
    
    def desligar(self):
        if self.ligado:
            print(f"moto {self.modelo} desligada")
            self.ligado = False
        else:
            print(f"moto {self.modelo} já está desligada")
    
    def acelerar(self, velocidade):
        if self.ligado:
            print(f"moto {self.modelo} acelerando para {velocidade} km/h")
        else:
            print(f"moto {self.modelo} não pode acelerar, está desligada")

class Carro(Automovel):
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            print(f"carro {self.modelo} ligado")
            self.ligado = True
        else:
            print(f"carro {self.modelo} já está ligado")
    
    def desligar(self):
        if self.ligado:
            print(f"carro {self.modelo} desligado")
            self.ligado = False
        else:
            print(f"carro {self.modelo} já está desligado")

class Caminhao(Automovel):
    def __init__(self, modelo, carga_maxima):
        self.modelo = modelo
        self.carga_maxima = carga_maxima
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            print(f"caminhão {self.modelo} ligado")
            self.ligado = True
        else:
            print(f"caminhão {self.modelo} já está ligado")
    
    def desligar(self):
        if self.ligado:
            print(f"caminhão {self.modelo} desligado")
            self.ligado = False
        else:
            print(f"caminhão {self.modelo} já está desligado")

class Onibus(Automovel):
    def __init__(self, modelo, capacidade):
        self.modelo = modelo
        self.capacidade = capacidade
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            print(f"ônibus {self.modelo} ligado")
            self.ligado = True
        else:
            print(f"ônibus {self.modelo} já está ligado")
    
    def desligar(self):
        if self.ligado:
            print(f"ônibus {self.modelo} desligado")
            self.ligado = False
        else:
            print(f"ônibus {self.modelo} já está desligado")
    
    def acelerar(self, velocidade):
        if self.ligado:
            if velocidade > 80:
                print(f"ônibus {self.modelo} limitado a 80 km/h")
            else:
                print(f"ônibus {self.modelo} acelerando para {velocidade} km/h")
        else:
            print(f"ônibus {self.modelo} não pode acelerar, está desligado")

def test_veiculos(veiculo):
    print("\n inFo:", type(veiculo).__name__)
    veiculo.ligar()
    veiculo.acelerar(60)
    veiculo.desligar()
    veiculo.acelerar(30)
    veiculo.desligar()


moto = Moto("honda Cg-125 fan ks")
carro = Carro("chevet")
caminhao = Caminhao("munk", 5000)
onibus = Onibus("apache VIP", 50)

test_veiculos(moto)
test_veiculos(carro)
test_veiculos(caminhao)
test_veiculos(onibus)