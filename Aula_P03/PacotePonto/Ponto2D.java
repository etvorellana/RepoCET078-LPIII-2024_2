package Aula_P03.PacotePonto;

public class Ponto2D {
    private double x;
    private double y;
    private double alpha;
    private double r;

    public Ponto2D() {
        this.x = 0;
        this.y = 0;
        this.alpha = 0;
        this.r = 0;
    }

    public Ponto2D(double xAlpha, double yR, boolean polar) {
        if (polar) {
            this.alpha = xAlpha;
            this.r = yR;
            polar2cart();
        } else {
            this.x = xAlpha;
            this.y = yR;
            cart2polar();
        }
    }

    public void cart2polar() {
        this.alpha = Math.atan(y/x);
        this.r = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
    }

    public void polar2cart() {
        this.x = r * Math.cos(alpha);
        this.y = r * Math.sin(alpha);
    }

    public Ponto2D(Ponto2D p) {
        this.x = p.x;
        this.y = p.y;
        this.alpha = p.alpha;
        this.r = p.r;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getAlpha() {
        return alpha;
    }

    public double getR() {
        return r;
    }

    public void setX(double x) {
        this.x = x;
        cart2polar();
    }

    public void setY(double y) {
        this.y = y;
        cart2polar();
    }

    public void setAlpha(double alpha) {
        this.alpha = alpha;
        polar2cart();
    }

    public void setR(double r) {
        this.r = r;
        polar2cart();
    }

    public void move(double dx, double dy) {
        x += dx;
        y += dy;
        cart2polar();
    }

    public void moveTo(double xAlpha, double yR, boolean polar) {
        if (polar) {
            this.alpha = xAlpha;
            this.r = yR;
            polar2cart();
        } else {
            this.x = xAlpha;
            this.y = yR;
            cart2polar();
        }
    }

    public void move(Ponto2D p) {
        x = p.x;
        y = p.y;
        alpha = p.alpha;
        r = p.r;
    }

    public double distancia() {
        return r;
    }

    public double distancia(Ponto2D p) {
        return Math.sqrt(Math.pow(x - p.x, 2) + Math.pow(y - p.y, 2));
    }

    public double distancia(double x, double y, boolean polar) {
        if (polar) {
            Ponto2D p = new Ponto2D(x, y, true);
            return this.distancia(p);
        }
        return Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2));
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    public boolean igualA(Ponto2D p) {
        return x == p.x && y == p.y;
    }

    public boolean diferenteDe(Ponto2D p) {
        return !igualA(p);
    }

    public boolean anteriorA(Ponto2D p) {
        return x < p.x && y < p.y;
    }

    public boolean posteriorA(Ponto2D p) {
        return !anteriorA(p) && !igualA(p);

    public Ponto2D espelhar(int eixo){
        if(eixo == 1){
            return new Ponto2D(-x, y, false);
        } else if(eixo == 2){
            return new Ponto2D(x, -y, false);
        } else {
            return new Ponto2D(-x, -y, false);
        }
    }

}
