class Carro:
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.is_running = False
        self.velocidade = 0
        self.marcha = 0 
    
    def __str__(self):
        return f"""
O carro de Marca {self.marca} e modelo {self.modelo}
do ano {self.ano} e cor {self.cor} saiu da loja e hoje tem a placa
{self.placa}
            """
    
    @classmethod
    def cadastro_venda(cls):
        marca = input("Digite aqui a marca do carro comprado: ")
        modelo = input("Digite aqui o modelo do carro comprado: ")
        ano = int(input("Digite aqui o ano do carro comprado: "))
        cor = input("Digite aqui a cor do carro comprado: ")
        placa = input("Digite aqui a placa do carro comprado: ")
        return cls(marca, modelo, ano, cor, placa)
    
    def ligar_carro(self):
        if not self.is_running:
            self.is_running = True
            print("O carro foi ligado..... RUMRUMRUMRUM")
        else:
            print("O carro já está ligado!!!")
    
    def desligar_carro(self):
        if not self.is_running:
            print("O carro já está desligado!")
            return
        
        if self.velocidade > 0:
            print("Reduzindo a velocidade gradualmente...")
            while self.velocidade > 0:
                self.velocidade -= 10  # Changed from 5 to 10
                print(f"Velocidade atual: {self.velocidade}km/h")
                
        self.is_running = False
        self.marcha = 0
        print("O carro foi desligado.")
    
    def trocar_marcha(self, nova_marcha):
        if not self.is_running:
            print("Ligue o carro primeiro!")
            return
        
        if nova_marcha not in [-1, 0, 1, 2, 3, 4, 5]:
            print("Marcha inválida!")
            return
        
        if nova_marcha == -1 and self.velocidade > 2:  # Changed from 1 to 2
            print("Só é possível engatar a ré com o carro parado ou a 2 km/h!")
            return
        
        velocidades_maximas = {
            1: 25,  # Changed from 20 to 25
            2: 45,  # Changed from 40 to 45
            3: 70,  # Changed from 60 to 70
            4: 90,  # Changed from 80 to 90
            5: 130  # Changed from 120 to 130
        }
        
        if nova_marcha > 0:
            marcha_anterior = self.marcha
            velocidade_minima_proxima_marcha = (nova_marcha - 1) * 20  # Changed from 15 to 20
            
            if self.velocidade < velocidade_minima_proxima_marcha:
                print(f"Velocidade muito baixa para a {nova_marcha}ª marcha!")
                return
            
            if self.velocidade > velocidades_maximas[nova_marcha]:
                print(f"Velocidade muito alta para a {nova_marcha}ª marcha!")
                return
        
        self.marcha = nova_marcha
        print(f"Marcha alterada para: {'Ré' if nova_marcha == -1 else 'Neutro' if nova_marcha == 0 else nova_marcha}ª")
    
    def acelerar(self):
        if not self.is_running:
            print(f"O carro {self.modelo} está desligado. Precisa ligar o carro primeiro!")
            return
        
        if self.marcha == 0:
            print("Carro está em ponto morto! Engate uma marcha.")
            return
        
        incrementos = {
            -1: 3,  # Changed from 2 to 3
            1: 7,   # Changed from 5 to 7
            2: 10,   # Changed from 8 to 10
            4: 18,   # Changed from 15 to 18
            5: 25    # Changed from 20 to 25
        }
        
        limites = {
            -1: 25,  # Changed from 20 to 25
            1: 25,   # Changed from 20 to 25
            2: 45,   # Changed from 40 to 45
            3: 70,   # Changed from 60 to 70
            4: 90,   # Changed from 80 to 90
            5: 130   # Changed from 120 to 130
        }