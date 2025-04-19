class Animal {
    String nome;
    String tipo;
    
    public Animal(String nome, String tipo) {
        this.nome = nome;
        this.tipo = tipo;
    }
    
    public void apresentando() {
        System.out.println("aqui temos o " + nome + ", um animal " + tipo + "!");
    }
    
    public void movimentacao() {
        switch(tipo) {
            case "terrestre":
                System.out.println(nome + " consegue andar e também correr ou nadar!");
                break;
            case "marinho":
                System.out.println(nome + " consegue nadar! Alguns podem pular, mas não conseguem andar.");
                break;
            case "voador":
                System.out.println(nome + " conseguem voar! Podem andar, mas não conseguem correr.");
                break;
            default:
                System.out.println("Esse tipo de animal não pode ser identificado!");
        }
    }
}

class AniTerrestre extends Animal {
    boolean consegueCorrer;
    boolean consegueNadar;
    
    public AniTerrestre(String nome, boolean consegueCorrer, boolean consegueNadar) {
        super(nome, "terrestre");
        this.consegueCorrer = consegueCorrer;
        this.consegueNadar = consegueNadar;
    }
    
    @Override
    public void movimentacao() {
        StringBuilder habilidades = new StringBuilder(nome + " anda");
        if (consegueCorrer) {
            habilidades.append(", corre");
        }
        if (consegueNadar) {
            habilidades.append(", nada");
        }
        System.out.println(habilidades.append("!").toString());
    }
}

class AniMarinho extends Animal {
    boolean conseguePular;
    
    public AniMarinho(String nome, boolean conseguePular) {
        super(nome, "marinho");
        this.conseguePular = conseguePular;
    }
    
    @Override
    public void movimentacao() {
        if (conseguePular) {
            System.out.println(nome + " consegue nadar e também consegue pular!");
        } else {
            System.out.println(nome + " consegue nadar mas não consegue pular.");
        }
    }
}

class AniVoador extends Animal {
    boolean consegueAndar;
    
    public AniVoador(String nome, boolean consegueAndar) {
        super(nome, "voador");
        this.consegueAndar = consegueAndar;
    }
    
    @Override
    public void movimentacao() {
        if (consegueAndar) {
            System.out.println(nome + " voa e também anda, mas não corre.");
        } else {
            System.out.println(nome + " só voa, não anda (como alguns insetos).");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        AniTerrestre tigre = new AniTerrestre("Tigre", true, false);
        AniTerrestre sapo = new AniTerrestre("Sapo", false, true);
        AniMarinho baleia = new AniMarinho("Baleia", true);
        AniMarinho peixe = new AniMarinho("Peixe", false);
        AniVoador coruja = new AniVoador("Coruja", true);
        AniVoador borboleta = new AniVoador("Mosquito", false);
        
        tigre.apresentando();
        tigre.movimentacao();
        
        sapo.apresentando();
        sapo.movimentacao();
        
        baleia.apresentando();
        baleia.movimentacao();
        
        peixe.apresentando();
        peixe.movimentacao();
        
        coruja.apresentando();
        coruja.movimentacao();
        
        borboleta.apresentando();
        borboleta.movimentacao();
    }
}