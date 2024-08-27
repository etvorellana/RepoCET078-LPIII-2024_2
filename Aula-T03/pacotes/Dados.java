package pacotes;

import java.util.Random;

public class Dados {
    
    int jogo[];
    int min;
    int tam;
    long semente;
    Random rand;

    public void iniDados(int min_, int tam_, int qtVezes, long semente_) {
        jogo = new int[qtVezes];
        min = min_;
        tam = tam_;
        semente = semente_;
        if (semente > 0)
            rand = new Random(semente);
        else if (semente < 0)
            rand = new Random(System.currentTimeMillis());
        else
            rand = new Random(); 
    }

    public  void jogaOsDados()
    {
        int qtVezes = jogo.length;
        
        for (int i = 0; i < qtVezes; i++)
        {
            jogo[i] = min + rand.nextInt(tam);
        }
    }

    public void printJogo()
    {
        int qtVezes = jogo.length;
        System.out.print("( ");
        for (int i = 0; i < qtVezes; i++)
        {
            System.out.print(jogo[i]);
            if (i < qtVezes-1)
                System.out.print(", ");
            else
                System.out.println(")");
        }
    }

    public int getJogo(int i)
    {   
        if (i <= jogo.length && i > 0)
            return jogo[i-1];
        else
            return -1;
    }
}