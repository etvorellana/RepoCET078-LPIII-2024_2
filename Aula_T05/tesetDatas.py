#import datas
from MinhaData import MinhaData, DataSemestre, DataSemestreC, DataSemestreE

def main():
    data1 = MinhaData()
    data2 = MinhaData(11,10,2024)
    data3 = MinhaData(outraData=data1)
    print(data1)
    print(data2)
    print(data3) 
    if(data1 == data2):
        print("Datas iguais")
    else:
        print("Datas diferentes")

    if(data1 < data2): 
        print("Data1 menor que Data2")
    else:
        print("Data1 maior ou igual que Data2")

    dataS1 = DataSemestre(1, 1, 2020)
    print(dataS1)
    if (dataS1 == data1):
        print("Datas iguais")
    else:
        print("Datas diferentes")

    dataS2 = DataSemestreC(1, 1, 2020)
    print(dataS2)
    if (dataS1 == dataS2):
        print("Datas iguais")
    else:
        print("Datas diferentes")

    dataS3 = DataSemestreE(18, 10, 2024, desc = 'aula normal')
    print(dataS3)
    if (dataS3 == data2):
        print("Datas iguais")
    else:
        print("Datas diferentes")


    


if __name__ == '__main__':
    main()