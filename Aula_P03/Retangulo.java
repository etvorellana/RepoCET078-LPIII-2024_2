package Aula_P03;
import Aula_P03.PacotePonto.Ponto2D;
import java.lang.Math;

public class Retangulo {

    private Ponto2D pTL;
    private Ponto2D pBR;

    public Retangulo() {
        this.pTL = new Ponto2D(0,1,false);
        this.pBR = new Ponto2D(1, 0, false);
    }

    public Retangulo(Ponto2D pTL, Ponto2D pBR) {
        this.pTL = new Ponto2D(pTL);
        this.pBR = new Ponto2D(pBR);
    }

    public Retangulo(Ponto2D pTL, float largura, float altura) {
        this.pTL = new Ponto2D(pTL);
        this.pBR = new Ponto2D(pTL.getX() + largura, pTL.getY() - altura, false);
    }

    public Retangulo(Retangulo r) {
        this.pTL = new Ponto2D(r.pTL);
        this.pBR = new Ponto2D(r.pBR);
    }

    public Ponto2D getPTL() {
        return pTL;
    }

    public Ponto2D getPBR() {
        return pBR;
    }

    public double getAltura() {
        return Math.abs(pTL.getY() - pBR.getY());
    }

    public double getLargura() {
        return Math.abs(pTL.getX() - pBR.getX());
    }

    public double area() {
        return this.getAltura() * this.getLargura();
    }

    public double perimetro() {
        return 2 * (this.getAltura() + this.getLargura());
    }

    public double intercepcao(Retangulo r) {
        double x1 = Math.max(this.pTL.getX(), r.pTL.getX());
        double y1 = Math.min(this.pTL.getY(), r.pTL.getY());
        double x2 = Math.min(this.pBR.getX(), r.pBR.getX());
        double y2 = Math.max(this.pBR.getY(), r.pBR.getY());
        return Math.abs((x2 - x1) * (y2 - y1));
    }

    public double diferenca(Retangulo r) {
        
        return this.area() - this.intercepcao(r);
    }

    public boolean estaDentroDe(Retangulo r) {
        return this.pTL.getX() >= r.pTL.getX() && this.pTL.getY() <= r.pTL.getY() && this.pBR.getX() <= r.pBR.getX() && this.pBR.getY() >= r.pBR.getY(); 
    }

    public String toString() {
        return "Ponto 1: " + p1.toString() + "\nPonto 2: " + p2.toString();
    }
    
}
