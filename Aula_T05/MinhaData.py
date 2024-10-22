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
    

class DataSemestre:
    
    def __init__(self, dia=1, mes=1, ano=1970, outraData=None, interval=0, desc = 'A Origem de Tudo'):
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

        self.__desc = desc

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

    @property
    def desc(self):
        return self.__desc
    
    @desc.setter
    def desc(self, desc):
        self.__desc = desc
    
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
        return f'{self.dia}/{self.mes}/{self.ano}: {self.desc}'

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


class DataSemestreC:

    def __init__(self, dia=1, mes=1, ano=1970, outraData=None, interval=0, desc = 'A Origem de Tudo'):
        self.__data = MinhaData(dia, mes, ano, outraData, interval)
        self.__desc = desc

    def inicializaData(self, dia=1, mes=1, ano=1970, outraData=None, interval=0):
        return self.__data.inicializaData(dia, mes, ano, outraData, interval)

    # Implementando set e get dos atributos
    @property
    def dia(self):
        return self.__data.dia
    
    @dia.setter
    def dia(self, dia):
        self.__data.dia = dia

    @property
    def mes(self):
        return self.__data.mes
    
    @mes.setter
    def mes(self, mes):
        self.__data.mes = mes

    @property
    def ano(self):
        return self.__data.ano        
    
    @ano.setter
    def ano(self, ano):
        self.__data.ano = ano

    @property
    def desc(self):
        return self.__desc
    
    @desc.setter
    def desc(self, desc):
        self.__desc = desc
    
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
        return f'{self.__data}: {self.desc}'

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
    

class DataSemestreE(MinhaData):

    def __init__(self, dia=1, mes=1, ano=1970, outraData=None, interval=0, desc = 'A Origem de Tudo'):
        super().__init__(dia, mes, ano, outraData, interval)
        self.__desc = desc


    @property
    def desc(self):
        return self.__desc
    
    @desc.setter
    def desc(self, desc):
        self.__desc = desc
    
    
    def __str__(self):
        return f'{super().__str__()}: {self.desc}'
    
    