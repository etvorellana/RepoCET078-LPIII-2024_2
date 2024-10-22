import DataPack.MinhaData;

public class UsaData {
    public static void main(String[] args) {
        MinhaData data1 = new MinhaData();
        System.out.println("Data 1: " + data1);
        MinhaData data2 = new MinhaData((byte) 31, (byte) 12, (short) 2020);
        System.out.println("Data 2: " + data2);
        data2.inicializaData();
        System.out.println("Data 2: " + data2);
        if (MinhaData.dataValida((byte) 29, (byte) 2, (short) 2020)) {
            System.out.println("2020 foi bissexto!!!");
            data1.inicializaData((byte) 29, (byte) 2, (short) 2020);
        } else {
            System.out.println("2020 não foi bissexto!!!");
            data1.inicializaData((byte) 28, (byte) 2, (short) 2020);
        }
        System.out.println("Data 1: " + data1);
        MinhaData data3 = new MinhaData(data1);
        System.out.println("Data 3: " + data3);
        MinhaData data4 = new MinhaData(data3, 60);
        System.out.println("Data 4: " + data4);

        data1.inicializaData((byte) 1, (byte) 12, (short) 2024);
        data2.inicializaData(data1,31);
        System.out.println("Data 1: " + data1);
        System.out.println("Data 2: " + data2);
        data3.inicializaData((byte) 25, (byte) 12, (short) 2024);
        while(data1.anteriorA(data2)){
            data1.inicializaData(data1,1);
            System.out.println("Data 1: " + data1);
            if (data1.igualA(data3))
                System.out.println("Felix NATAL!!!!");
        }


    }
}