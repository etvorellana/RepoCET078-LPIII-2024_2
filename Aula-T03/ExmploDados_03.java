import pacotes.Dados;

public class  ExmploDados_03 {
    
    public static void main(String[] args) {
        Dados d = new Dados();
        d.iniDados(1, 6, 10, 123456789);
        d.jogaOsDados();
        d.printJogo();
        for(int i = 1; i <= 10; i++)
            System.out.println("Jogo[" + i + "] = " + d.getJogo(i));
    }
}   