import java.util.ArrayList; // importantei a bivlioteca para fazer listas

public class rosonattp1 { // classe que cadastra pessoa, coloquei meu nome profesor pra poder salvar o nome do arquivo
    public String ident;
    public String doc;
    public String ocup;
    public String local;
    // aqui eu fiz a estrutura das informaçoes
    public rosonattp1(String a, String b, String c, String d) {
        ident = a;
        doc = b;
        ocup = c;
        local = d;
    }
        // ientificando a pessoa
    public void pessoa() {
        String[] dados = {ident, doc, ocup, local};
        for(String info : dados) {
            System.out.println(info);
        }
        System.out.println("-----");
    }

    public static void main(String[] args) { // função principal do cadastro
        ArrayList<rosonattp1> pessoas = new ArrayList<>();
        // pessoas ja adicionadas
        pessoas.add(new rosonattp1(
            "Rosonatt F erreira", 
            "165.118.977-37", 
            "Engenheiro de software", 
            "litoranea, 898"
        ));
        
        pessoas.add(new rosonattp1(
            "Diego Ramos", 
            "166.119.978-38", 
            "Professor", 
            "Gravata, 899"
        ));
        
        pessoas.add(new rosonattp1(
            "Bruno Oliveira ", 
            "199.187.919-45", 
            "Victor papa", 
            " vilatur, 272"
        ));

        for(rosonattp1 individuo : pessoas) {
            individuo.pessoa();
        }
        // saida dos cadastrados
        System.out.println("todos que foram cadastrados: " + pessoas.size());
    }
}