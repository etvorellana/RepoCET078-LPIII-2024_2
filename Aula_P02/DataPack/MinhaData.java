package DataPack;

public class MinhaData {
    /*
     * A quantidade de dias de cada mês, considerando meses com 30 ou 31 dias e fevereiro com 29 ou 29 dias.
     * Meses entre janeiro (mês 1) e dezembro (mês 12)
     * Anos desde 1900 até 2050
     */
    private byte dia;
    private byte mes;
    private short ano;

    // Cria uma instância com a data como 1/1/1970.
    public MinhaData(){
        this.inicializaData();
    }
    /*
     * Se estes parâmetros não caracterizarem uma data válidos 
     * atributos da classe são inicializados com 1/1/1970;
     */
    public MinhaData(byte dia, byte mes, short ano)
    {
        this();
        inicializaData(dia, mes, ano);
    }

    /*
     * Inicializa uma data com os mesmos atributos da instância da 
     * classe MinhaData. 
     */
    public MinhaData(MinhaData outraData)
    {
        this.inicializaData(outraData);
    }

    /*
     * Inicializa uma data com a data definida na instância da classe 
     * MinhaData incrementada na quantidade de dias definidas pelo 
     * parâmetro intervalo.
     */
    public MinhaData(MinhaData outraData, int interval)
    {
        this(outraData);
        inicializaData(outraData, interval);

    }

    /*
     * Inicializa uma data com a data definida na instância da 
     * classe MinhaData incrementada na quantidade de dias 
     * definidas pelo parâmetro intervalo.
     */
    public boolean inicializaData(MinhaData outraData, int dias)
    {
        byte dia = outraData.dia;
        byte mes = outraData.mes;
        short ano = outraData.ano;
        for (int i = 0; i < dias; i++) {
            dia++;
            if (!dataValida(dia, mes, ano)) {
                dia = 1;
                mes++;
                if (!dataValida(dia, mes, ano)) {
                    mes = 1;
                    ano++;
                    if(!dataValida(dia, mes, ano)) {
                        return false;
                    }
                }        
            }
        }
        this.inicializaData(dia, mes, ano);
        return true;
    }

    /*
     * Inicializa uma data com os mesmos atributos da instância da 
     * classe MinhaData.
     */
    public void inicializaData(MinhaData outraData)
    { 
        this.dia = outraData.dia;
        this.mes = outraData.mes;
        this.ano = outraData.ano;
    }

    /*
     * Inicializa uma data com os valores definidos pelos parâmetros de 
     * entrada. Se estes parâmetros não caracterizarem uma data válidos, 
     * os atributos da classe não são alterados e o método retorna false; 
     */
    public boolean inicializaData(byte dia, byte mes, short ano)
    {
        if (!dataValida(dia, mes, ano)) {
            return false;
        }
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
        return true;
        
    }
    
    public static boolean dataValida(byte d, byte m, short a) 
    {
        byte diasMes[] = {31,28,31,30,31,30,31,31,30,31,30,31};

        if (a < 1900 || a > 2050) {
            return false;
        }

        if (m < 1 || m > 12) {
            return false;
        }

        if (d < 1 || d > diasMes[m-1]) {
            return false;
        }

        // ano bissexto
        if (m == 2 && d == 29) {
            if (a % 4 == 0 && (a % 100 != 0 || a % 400 == 0)) {
                return true;
            } else {
                return false;
            }
        }
        return true;
    }

    private boolean dataValida()
    {
        return dataValida(this.dia, this.mes, this.ano);
    }

    // Inicializa a data como 1/1/1970;
    public void inicializaData()
    {
        this.dia = 1;
        this.mes = 1;
        this.ano = 1970;
    }

    public String toString(){
        return this.dia + "/" + this.mes + "/" + this.ano;
    }

    public byte qualDia(){
        return this.dia;
    }

    public byte qualMes(){
        return this.mes;
    }

    public short qualAno(){
        return this.ano;
    }

    public boolean setDia(byte dia){
        if (dataValida(dia, this.mes, this.ano)) {
            this.dia = dia;
            return true;
        }
        return false;
    }

    public boolean setMes(byte mes){
        if (dataValida(this.dia, mes, this.ano)) {
            this.mes = mes;
            return true;
        }
        return false;
    }

    public boolean setAno(short ano){
        if (dataValida(this.dia, this.mes, ano)) {
            this.ano = ano;
            return true;
        }
        return false;
    }

    public boolean igualA(MinhaData outraData)
    {
        return this.dia == outraData.dia && this.mes == outraData.mes && this.ano == outraData.ano;

    }
    
    public boolean diferenteDe(MinhaData outraData)
    {
        return !igualA(outraData);

    }

    public boolean anteriorA(MinhaData outraData)
    {
        if (this.ano < outraData.ano) {
            return true;
        } else if (this.ano == outraData.ano) {
            if (this.mes < outraData.mes) {
                return true;
            } else if (this.mes == outraData.mes) {
                if (this.dia < outraData.dia) {
                    return true;
                }
            }
        }
        return false;

    }

    public boolean posteriorA(MinhaData outraData)
    {
        return !anteriorA(outraData) && !igualA(outraData);

    }


}