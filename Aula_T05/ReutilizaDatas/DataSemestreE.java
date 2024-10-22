
/**
 * Escreva uma descrição da classe DataSemestreE aqui.
 * 
 * @author (seu nome) 
 * @version (um número da versão ou uma data)
 */
public class DataSemestreE extends MinhaData{

    private String desc;

    // Cria uma instância com a data como 1/1/1970.
    public DataSemestreE(){
        super();
        desc = "A origem de tudo";
    }
    /*
     * Se estes parâmetros não caracterizarem uma data válidos 
     * atributos da classe são inicializados com 1/1/1970;
     */
    public DataSemestreE(byte dia, byte mes, short ano)
    {
        super(dia, mes, ano);
        desc = "Nada";
    }
    
    public DataSemestreE(byte dia, byte mes, short ano, String desc)
    {
        this(dia, mes, ano);
        this.desc = desc;
    }

    /*
     * Inicializa uma data com os mesmos atributos da instância da 
     * classe MinhaData. 
     */
    public DataSemestreE(MinhaData outraData, String desc)
    {
        super(outraData);
        this.desc = desc;
    }

    /*
     * Inicializa uma data com a data definida na instância da classe 
     * MinhaData incrementada na quantidade de dias definidas pelo 
     * parâmetro intervalo.
     */
    public DataSemestreE(MinhaData outraData, int interval, String desc)
    {
        super(outraData, interval);
        this.desc = desc;

    }

    public String toString(){
        return super.toString()  + ": " + desc;
    }
    
    public String qualEvento(){
        return desc;
    }

    public void setEvento(String desc)
    {
        this.desc = desc;
    }

}
