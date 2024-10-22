
public class DataSemestreC
{
    private MinhaData data;
    private String desc;

    /**
     * Construtor para objetos da classe DataSemestreC
     */
    public DataSemestreC()
    {
        data = new MinhaData();
        desc = "A origem de tudo";
    }
    
    public DataSemestreC(byte dia, byte mes, short ano)
    {
        data = new MinhaData(dia, mes, ano);
        desc = "Nada";
    }
    
    public DataSemestreC(byte dia, byte mes, short ano, String desc)
    {
        this(dia, mes, ano);
        this.desc = desc;
    }
    
    public DataSemestreC(MinhaData outraData, String desc)
    {
        data = new MinhaData(outraData);
        this.desc = desc;
    }
    
    public DataSemestreC(MinhaData outraData, int interval, String desc)
    {
        data = new MinhaData(outraData, interval);
        this.desc = desc;
    }

    public boolean inicializaData(MinhaData outraData, int dias){
        return data.inicializaData(outraData, dias);
    }
    
    public void inicializaData(MinhaData outraData)
    {
        data.inicializaData(outraData);
    }
    
    public void inicializaData()
    {
        data.inicializaData();
    }
    
    public String toString(){
        return this.data + ": " + desc;
    }

    public byte qualDia(){
        return this.data.qualDia();
    }

    public byte qualMes(){
        return this.data.qualMes();
    }

    public short qualAno(){
        return this.data.qualAno();
    }
    
    public String qualEvento(){
        return desc;
    }

    public boolean setDia(byte dia){
        return data.setDia(dia);
    }

    public boolean setMes(byte mes){
        return data.setMes(mes);
    }

    public boolean setAno(short ano){
        return data.setAno(ano);
    }
    
    public void setEvento(String desc)
    {
        this.desc = desc;
    }
    
    public boolean igualA(DataSemestreC outraData)
    {
        return this.data.igualA(outraData.data);

    }
    
    public boolean diferenteDe(DataSemestreC outraData)
    {
        return !igualA(outraData);

    }

    public boolean anteriorA(DataSemestreC outraData)
    {
        return data.anteriorA(outraData.data);

    }

    public boolean posteriorA(DataSemestreC outraData)
    {
        return !anteriorA(outraData) && !igualA(outraData);

    }
}
