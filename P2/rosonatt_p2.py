class Objeto:
    def __init__(self, nome, tipo, descricao):
        self._nome, self._tipo, self._descricao = nome, tipo, descricao
    def apresentacao(self): return f"{self._nome} ({self._tipo}): {self._descricao}"

class Personagem:
    def __init__(self, nome, tipo):
        self._nome, self._tipo, self._vida, self._objeto = nome, tipo, 100, None
        self._descricoes = {'mago':" Usa grande magias ancestrais",'elfo':"Possui uma afindade maior com a natureza",'anão':"Baixo orém  Robusto ",'bardo':"GuitarHero",'arqueiro':"Possui uma  otmia visão e prescisão"}
    def apresentacao(self):
        return f"{self._nome} - {self._tipo.upper()}\n{self._descricoes.get(self._tipo,'Aventureiro')}\nArma: {self._objeto._nome if self._objeto else 'Nenhuma'}"
    def pegar(self, obj): 
        armas_permitidas = {
            'mago': ['cajado'],
            'elfo': ['arco', 'espada'],
            'anão': ['machado', 'espada'],
            'bardo': ['alaúde'],
            'arqueiro': ['arco']
        }
        if obj._tipo in armas_permitidas.get(self._tipo, []):
            self._objeto = obj
            return f"{self._nome} equipou {obj._nome}"
        return f"{self._nome} não pode usar {obj._nome}"

class Personagem_NPC(Personagem):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
        self._vida = 50 if tipo != 'bebe_reborn' else 30
        self._dialogos = {
            'furry': {
                'elfo': "'então você gosta de animais??! hihihi'",
                'aleatorio': "'olha só o que temos aqui?'"
                
            },
            'bebe_reborn': {
                'mago': "'SAI DAQUI VELHOOOOO!'",
                'aleatorio': "'Faz o L!!!'"
            }
        }
    
    def conversa(self, personagem):
        dialogo = self._dialogos.get(self._tipo, {}).get(personagem._tipo, self._dialogos.get(self._tipo, {}).get('aleatorio'))
        return f"NPC {self._nome} diz: {dialogo}"

class Personagem_RPG(Personagem):
    _afinidades = {'mago':['elfo','anão'],'arqueiro':['mago','elfo','bardo'],'bardo':['mago','arqueiro','anão','elfo'],'elfo':['mago','arqueiro','bardo'],'anão':['mago','bardo']}
    _interacaos = {
        'amigavel': {'mago':{'elfo':"'Sua sabedoria me impressiona'",'anão':"' você é realmente forte'"},
                    'elfo':{'mago':"'Sua magia é  poderosa'",'arqueiro':"'Sua pontaria é excelente!'"},
                    'anão':{'mago':"'Sua magia é forte!'",'bardo':"'Sua música é animada!'"}},
        'hostil': {'mago':{'arqueiro':"'Seus arcos são insignificantes!'",'bardo':"'Silêncio, irritante!'"},
                  'elfo':{'anão':"'Bêbado barulhento!'",'bardo':"'Música ruim da peste!'"},
                  'anão':{'elfo':"'humm!! baitola!'",'arqueiro':"'seus arcos são muitos  fraquinhos!'"}},
        'neutro': "'O que você quer?'"}
    _armas = {'mago':'cajado','elfo':'arco','anão':'machado','bardo':'alaúde','arqueiro':'arco'}
    _habilidades = {'mago':"Feitiços",'elfo':"Precisão",'anão':"Força bruta",'bardo':"Encantar",'arqueiro':"Disparos"}

    def __init__(self, nome, tipo):
        super().__init__(nome, tipo); self._habilidade = self._habilidades.get(tipo,"Desconhecida")
    def apresentacao(self): return super().apresentacao()+f"\nHabilidade: {self._habilidade}"
    def conversa(self, p):
        if p._tipo in self._afinidades.get(self._tipo,[]):
            dialogo = self._interacaos['amigavel'].get(self._tipo,{}).get(p._tipo)
            if dialogo: return f"{self._nome} diz: {dialogo}"
        if p._tipo in {'elfo':['anão'],'anão':['elfo'],'mago':['bardo']}.get(self._tipo,[]):
            dialogo = self._interacaos['hostil'].get(self._tipo,{}).get(p._tipo)
            if dialogo: return f"{self._nome} rosna: {dialogo}"
        return f"{self._nome} diz: {self._interacaos['neutro']}"
    def defesa(self, a): self._vida -= a//(3 if self._tipo=='anão' else 2); return f"{self._nome} defendeu! Vida: {self._vida}"
    def ataque(self, a):
        d = (25 if self._tipo=='anão' else 20)+(10 if a._tipo in {'elfo':['anão'],'anão':['elfo'],'mago':['bardo']}.get(self._tipo,[]) else 0)
        d += 10 if (self._objeto and self._objeto._tipo==self._armas[self._tipo]) else 0
        a._vida -= d; return f"{self._nome} atacou {a._nome} causando {d} de dano!"
    def trocar_item(self, outro, item):
        if self._objeto != item: return f"{self._nome} não tem {item._nome}"
        if item._tipo not in self._armas.get(outro._tipo, []): return f"{outro._nome} não pode usar {item._nome}"
        self._objeto = None
        outro.pegar(item)
        return f"{self._nome} deu {item._nome} para {outro._nome}"

class Ambiente:
    def __init__(self, nome):
        self._nome = nome
        self._participantes = []
    
    def adicionar(self, p):
        self._participantes.append(p)
        return f"{p._nome} finalmente chegou em {self._nome}"
    
    def interacoes(self):
        resultados = []
       
        npcs = [p for p in self._participantes if isinstance(p, Personagem_NPC)]
        for npc in npcs:
            for p in self._participantes:
                if p != npc: resultados.append(npc.conversa(p))
        
        arqueiro = next((p for p in self._participantes if p._tipo == 'arqueiro'), None)
        elfo = next((p for p in self._participantes if p._tipo == 'elfo'), None)
        if arqueiro and elfo and arqueiro._objeto:
            resultados.append("\nTentando trocar:")
            resultados.append(arqueiro.trocar_item(elfo, arqueiro._objeto))
        
        mago = next((p for p in self._participantes if p._tipo == 'mago'), None)
        anao = next((p for p in self._participantes if p._tipo == 'anão'), None)
        if mago and anao and anao._objeto:
            resultados.append("\nTentativa  não deu certo:")
            resultados.append(mago.pegar(anao._objeto))
        
        return "\n".join(resultados)

cajado = Objeto("Cajado Arcano de Shetterer","cajado"," da um grande aumento no oder magico")
arco = Objeto("Arco Élfico de Delternoir","arco","aumenta a pescisão")
machado = Objeto("Machado de Batalha de Igynoir","machado"," aumenta a perfuração do corte")
alaude = Objeto("Alaúde Dourado de Roberto Carlos","alaúde"," hipnotiza todos que possam ouvir")

mago = Personagem_RPG("Dumbledore","mago"); mago.pegar(cajado)
elfo = Personagem_RPG("Adamastor","elfo"); elfo.pegar(arco)
anao = Personagem_RPG("Ryan Guiwison","anão"); anao.pegar(machado)
bardo = Personagem_RPG("Astolfo","bardo"); bardo.pegar(alaude)
arqueiro = Personagem_RPG("KURT","arqueiro"); arqueiro.pegar(arco)

furry = Personagem_NPC("Menino Guaxinim Matheus Prates", "furry")
bebe_reborn = Personagem_NPC("Jv", "bebe_reborn")

durmistrong = Ambiente("Cidade de Durmistrong")

durmistrong.adicionar(mago)
durmistrong.adicionar(elfo)
durmistrong.adicionar(anao)
durmistrong.adicionar(bardo)
durmistrong.adicionar(arqueiro)
durmistrong.adicionar(furry)
durmistrong.adicionar(bebe_reborn)

print("=== CIDADE DE DURMISTRONG ===")
print("\n=== PERSONAGENS PRESENTES ===")
for i, p in enumerate(durmistrong._participantes, 1):
    print(f"\nPersonagem {i}:")
    print(p.apresentacao())

print("\n=== INTERAÇÕES ENTRE PERSONAGENS ===")

print("\n--- Diálogos NPCs ---")
npcs = [p for p in durmistrong._participantes if isinstance(p, Personagem_NPC)]
for npc in npcs:
    for p in durmistrong._participantes:
        if p != npc:
            print(f"\n{npc._nome} ({npc._tipo}) conversa com {p._nome} ({p._tipo}):")
            print(npc.conversa(p))

print("\n--- Diálogos entre Aventureiros ---")
for p1 in durmistrong._participantes:
    if isinstance(p1, Personagem_RPG):
        for p2 in durmistrong._participantes:
            if p1 != p2 and isinstance(p2, Personagem_RPG):
                print(f"\n{p1._nome} ({p1._tipo}) conversa com {p2._nome} ({p2._tipo}):")
                print(p1.conversa(p2))

print("\n--- Tentativas de Troca de Itens ---")
arqueiro = next((p for p in durmistrong._participantes if p._tipo == 'arqueiro'), None)
elfo = next((p for p in durmistrong._participantes if p._tipo == 'elfo'), None)
if arqueiro and elfo and arqueiro._objeto:
    print(f"\n{arqueiro._nome} tenta trocar {arqueiro._objeto._nome} com {elfo._nome}:")
    print(arqueiro.trocar_item(elfo, arqueiro._objeto))

mago = next((p for p in durmistrong._participantes if p._tipo == 'mago'), None)
anao = next((p for p in durmistrong._participantes if p._tipo == 'anão'), None)
if mago and anao and anao._objeto:
    print(f"\n{mago._nome} tenta pegar {anao._objeto._nome} de {anao._nome}:")
    print(mago.pegar(anao._objeto))

print("\n=== BATALHAS ENTRE PERSONAGENS ===")
print(f"\n{elfo._nome} ataca {anao._nome}:")
print(elfo.ataque(anao))
print(anao.defesa(30))

print(f"\n{anao._nome} contra-ataca {elfo._nome}:")
print(anao.ataque(elfo))
print(elfo.defesa(35))

print("\n=== SITUAÇÃO FINAL DOS PERSONAGENS ===")
for p in durmistrong._participantes:
    if isinstance(p, Personagem_RPG):
        print(f"\n{p._nome}: Vida = {p._vida}")