"""
    Utilizando os recursos da  linguagem de programação Python, apresentados em 
    sala de aula,implemente a classe MinhaData com as seguintes especificações:

    Nome da classe: MinhaData

    Atributos: permitem representar datas válidas, ou seja combinações válidas de 
    dia, mês e ano considerando:
    * A quantidade de dias de cada mês, considerando meses com 30 ou 31 dias e 
    fevereiro com 28 ou 29 dias.
    Meses entre janeiro (mês 1) e dezembro (mês 12)
    Anos desde 1900 até 2050
    Os seguintes construtores da classe (da versão em Java):
    * public MinhaData(): Inicializa a data como 1/1/1970.
    * public MinhaData(byte dia, byte mes, short ano): Se estes parâmetros não 
    caracterizarem uma data válidos atributos da classe são inicializados com 1/1/1970;
    * public MinhaData(MinhaData outraData): Inicializa uma data com os mesmos atributos
    da instância da classe MinhaData.
    * public MinhaData(MinhaData outraData, int interval): Inicializa uma data com a data 
    definida na instância da classe MinhaData incrementada na quantidade de dias definidas 
    pelo parâmetro intervalo. 

    Método de inicialização de uma data nas versões (da versão em Java):
    * public void inicializaData(): Inicializa a data como 1/1/1970;
    * public boolean inicializaData(byte dia, byte mes, short ano): Inicializa uma data com 
    os valores definidos pelos parâmetros de entrada. Se estes parâmetros não caracterizarem 
    uma data válidos, os atributos da classe não são alterados e o método retorna false; 
    * public void inicializaData(MinhaData outraData): Inicializa uma data com os mesmos 
    atributos da instância da classe MinhaData. 
    * public void inicializaData(MinhaData outraData, int interval): Inicializa uma data com 
    a data definida na instância da classe MinhaData incrementada na quantidade de dias 
    definidas pelo parâmetro intervalo. 
    Vamos discutir sobre semelhanças e diferenças entre estes métodos e os construtores 
    definidos anteriormente. Podemos utilizar estes métodos na implementação dos construtores? 
    Qual o sentido de um dos métodos retornar um boolean enquanto que os restantes retornam void? 

    Implemente os seguintes métodos para verificar se uma combinação de valores de dia, mês e ano 
    caracterizam uma data válida:
    * public static boolean dataValida(byte dia, byte mes, short ano) 
    * private boolean dataValida() 
    Qual a diferença entre estas duas implementações do método? Em quais casos pode ser utilizado 
    cada um;  

    Implemente os métodos seters/geters  apropriados para esta classe;

    Implemente o método public String toString() que retorna uma string com a data em formato 
    literal. Exemplo: para 1/1/1970 deve retornar a String “1 de Janeiro de 1970”. 
    * Este método não imprime nada, apenas retorna a String que deve ser construída a partir 
    dos atributos da classe.
    * Pesquise para que serve o método toString() de uma classe e mostre utilizando um exemplo 
    antes e depois de implementar o referido método.

    Implemente os seguintes métodos para realizar operações com instâncias da classe MinhaData:
    * public boolean igualA(MinhaData outraData);  
    * public boolean diferenteDe(MinhaData outraData);
    * public boolean anteriorA(MinhaData outraData);
    * public boolean posteriorA(MinhaData outraData);

"""

class MinhaData:
    
    def __init__(self, dia=1, mes=1, ano=1970, outraData=None, interval=0):
        #if outraData:
        if outraData and isinstance(outraData, MinhaData):
            if interval > 0:
                pass
            else:
                self.__dia = outraData.__dia
                self.__mes = outraData.mes
                self.__ano = outraData.ano
        elif MinhaData.dataValida(dia, mes, ano):
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano

    def inicializaData(self, dia=1, mes=1, ano=1970, outraData=None, interval=0):
        
        if outraData and isinstance(outraData, MinhaData):
            if interval > 0:
                pass  
            else:
                self.__dia = outraData.dia
                self.__mes = outraData.mes
                self.__ano = outraData.ano
                return True
        elif MinhaData.dataValida(dia, mes, ano):
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano
            return True
        return False

    # Implementando set e get dos atributos
    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if MinhaData.dataValida(dia, self.__mes, self.__ano):
            self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if MinhaData.dataValida(self.__dia, mes, self.__ano):
            self.__mes = mes

    @property
    def ano(self):
        return self.__ano        
    
    @ano.setter
    def ano(self, ano):
        if MinhaData.dataValida(self.__dia, self.__mes, ano):
            self.__ano = ano
    
    def dataValida(dia, mes, ano):
        if ano < 1900 or ano > 2050:
            return False
        if dia < 1 or dia > 31:
            return False
        if mes == 2:
            if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
                if dia <= 29:
                    return True
                else:
                    return False
            else:
                if dia <= 28:
                    return True
                else:
                    return False
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia <= 30:
                return True
            else:
                return False
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia <= 31:
                return True
            else:
                return False
        else:
            return False
        
    def __dataValida(self):
        return MinhaData.dataValida(self.__dia, self.__mes, self.__ano)
        
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    












    def __eq__(self, other):
        return self.dia == other.dia and self.mes == other.mes and self.ano == other.ano

    def __ne__(self, other):
        return self.dia != other.dia or self.mes != other.mes or self.ano != other.ano

    def __lt__(self, other):
        if self.ano < other.ano:
            return True
        elif self.ano == other.ano:
            if self.mes < other.mes:
                return True
            elif self.mes == other.mes:
                if self.dia < other.dia:
                    return True
        return False

    def __le__(self, other):
        if self.ano < other.ano:
            return True
        elif self.ano == other.ano:
            if self.mes < other.mes:
                return True
            elif self.mes == other.mes:
                if self.dia < other.dia or self.dia == other.dia:
                    return True
        return False

    def __gt__(self, other):
        if self.ano > other.ano:
            return True
        elif self.ano == other.ano:
            if self.mes > other.mes:
                return True
            elif self.mes == other.mes:
                if self.dia > other.dia:
                    return True
        return False

    def __ge__(self, other):
        if self.ano > other.ano:
            return True
        elif self.ano == other.ano:
            if self.mes > other.mes:
                return True
            elif self.mes == other.mes:
                if self.dia > other.dia or self.dia == other.dia:
                    return True
        return False

    