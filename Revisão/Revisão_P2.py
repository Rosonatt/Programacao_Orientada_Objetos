class Conta:
    def __init__(self, nome_cliente, numero_conta, agencia):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta 
        self.agencia = agencia
        self.saldo = 0.0
        self.limite_cheque = 1000.0
        self.limite_cartao = 2000.0
        self._pix = None
        self._senha = "1234"

    def cadastrar(self):
        print(f"Conta cadastrada com sucesso!")
        print(f" Cliente: {self.nome_cliente}")
        print(f" Agência: {self.agencia}")
        print(f" Conta: {self.numero_conta}")

    def autenticar(self, senha):
        if senha == self._senha:
            print(" Autenticação realizada com sucesso!")
            return True
        print(" Senha incorreta!")
        return False

    def cadastrar_pix(self, chave_pix):
        self._pix = chave_pix
        print(f" Chave PIX cadastrada: {chave_pix}")
        
    def pix(self, chave_origem, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"💸 PIX de R${valor:.2f} realizado com sucesso!")
            print(f"💰 Saldo atual: R${self.saldo:.2f}")
            return True
        print(" Saldo insuficiente para realizar PIX")
        return False

    def cheque_especial(self, valor):
        if valor <= self.limite_cheque:
            self.saldo -= valor
            print(f" Cheque especial de R${valor:.2f} utilizado")
            print(f" Saldo atual: R${self.saldo:.2f}")
            return True
        print(" Limite de cheque especial insuficiente")
        return False

    def cartao_credito(self, valor):
        if valor <= self.limite_cartao:
            print(f" Compra de R${valor:.2f} aprovada no cartão")
            return True
        print(" Limite do cartão insuficiente")
        return False

    def depositar(self, valor):
        self.saldo += valor
        print(f" Depósito de R${valor:.2f} realizado")
        print(f" Saldo atual: R${self.saldo:.2f}")

    def debito(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"💳 Débito de R${valor:.2f} realizado")
            print(f"💰 Saldo atual: R${self.saldo:.2f}")
            return True
        print(" Saldo insuficiente para débito")
        return False

class Loja:
    def __init__(self):
        self.catalogo = [
            {"nome": "Playstation 5", "preco": 4500},
            {"nome": "Nintendo Switch 2", "preco": 3000}
        ]

    def realizar_venda(self):
        print(" Iniciando venda...")

    def oferecer_promocao(self):
        print(" Oferecendo promoção...")

    def adicionar_produto(self, produto, valor):
        self.catalogo.append({"nome": produto, "preco": valor})
        print(f" Produto adicionado: {produto} - R${valor:.2f}")

    def remover_produto(self, produto):
        self.catalogo = [p for p in self.catalogo if p["nome"] != produto]
        print(f" Produto removido: {produto}")

    def listar_produtos(self):
        print("\n Catálogo de Produtos:")
        for produto in self.catalogo:
            print(f" {produto['nome']} - R${produto['preco']:.2f}")
        return self.catalogo

class LojaFisica(Loja):
    def __init__(self):
        super().__init__()
        self._desconto = None

    def realizar_venda(self, metodo, conta, item_index, produto):
        if item_index >= len(self.catalogo):
            print(" Produto não encontrado!")
            return False
            
        valor = self.catalogo[item_index]["preco"]
        if self._desconto:
            valor = valor * (1 - self._desconto)
            print(f" Desconto aplicado: {self._desconto*100}%")
            print(f" Valor com desconto: R${valor:.2f}")

        print(f"\n Realizando venda:")
        print(f" Produto: {self.catalogo[item_index]['nome']}")
        print(f" Valor: R${valor:.2f}")
        print(f" Método: {metodo}")

        if metodo == "pix":
            return conta.pix(conta._pix, valor, conta)
        elif metodo == "cartao":
            return conta.cartao_credito(valor)
        elif metodo == "cheque":
            return conta.cheque_especial(valor)
        return False

    def oferecer_promocao(self, desconto):
        self._desconto = desconto
        print(f" Nova promoção: {desconto*100}% de desconto!")

print("\n=== Demonstração do Sistema ===")

loja = LojaFisica()
conta_diego = Conta("Diego", "1234", "001")
conta_rosonatt = Conta("Rosonatt", "5678", "001")

print("\n1. Cadastro de Contas:")
conta_diego.cadastrar()
conta_rosonatt.cadastrar()

print("\n2. Listagem de Produtos:")
loja.listar_produtos()

print("\n3. Realizando Depósito:")
conta_diego.depositar(5000)

print("\n4. Aplicando Promoção:")
loja.oferecer_promocao(0.1)

print("\n5. Realizando Venda:")
loja.realizar_venda("pix", conta_diego, 0, "Playstation 5")