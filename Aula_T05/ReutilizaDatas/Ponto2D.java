
/**
 * Escreva uma descrição da classe Ponto2D aqui.
 * 
 * @author (seu nome) 
 * @version (um número da versão ou uma data)
 * 
 * 
 */

//import Math.sqrt;

public class Ponto2D
{
    private double x;
    private double y;

    /**
     * Construtor para objetos da classe Ponto2D
     */
    public Ponto2D()
    {
        // inicializa variáveis de instância
        x = 0;
        y = 0;
    }
    
    public Ponto2D(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

    public void setX(double x)
    {
        this.x = x;
    }
    
    public void setY(double y)
    {
        this.y = y;
    }
    
    public double getX()
    {
        return x;
    }
    
    public double getY()
    {
        return y;
    }
    
    public double raio()
    {
        double r;
        r = x*x + y*y;
        //return Math.sqrt(r);
        return r;
    }
    
    public double distanciaAte(Ponto2D outroPonto)
    {
        double d;
        d = (this.x - outroPonto.x)*(this.x - outroPonto.x) + (this.y - outroPonto.y)*(this.y - outroPonto.y);
        //return Math.sqrt(d);
        return d;
    }
    
    public String toString()
    {
        return "( " + x + ", " + y + " )";

    }
    
    
}
