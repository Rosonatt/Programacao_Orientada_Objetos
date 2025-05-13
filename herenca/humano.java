class Ser_vivo {
    public String genero;
    public float altura;
    
    public Ser_vivo(String genero, float altura) {
        this.genero = genero;
        this.altura = altura;
    }
}

public class humano extends Ser_vivo {
    public String nome;
    public String cpf;
    public int idade;

    public humano(String nome, String cpf, int idade, String genero, float altura) {
        super(genero, altura);
        this.nome = nome;
        this.cpf = cpf;
        this.idade = idade;
    }

    public void apresentar() {
        System.out.println("Nome: " + nome + ", Idade: " + idade + ", Altura: " + altura + 
                           ", Gênero: " + genero + ", CPF: " + cpf);
    }

    public static void main(String[] args) {
        humano ser1 = new humano("Rosonatt", "123456789", 30, "Masculino", 1.78f);
        ser1.apresentar();

        humano ser2 = new humano("Ryan", "987654321", 21, "Boyceta", 1.81f);
        ser2.apresentar();  
    }
}

