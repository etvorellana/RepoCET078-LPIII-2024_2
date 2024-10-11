
#import datas
from datas import MinhaData

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


if __name__ == '__main__':
    main()

