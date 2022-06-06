from flores import Flores
class Ramo:
    __tamano = ''
    __flores = []

    def __init__(self, tamano, flores=None):
        if (tamano > 10):
            self.__tamano = 'Grande'
        elif (tamano <= 10 and tamano > 5):
            self.__tamano = 'Mediano'
        elif (tamano <= 5):
            self.__tamano = 'Chico'
        self.__flores = []

    def setFlores(self, flores):
        for i in flores:
            self.__flores.append(i)

    def getFlores(self):
        return self.__flores

    def mostrarFlores(self):
        for i in self.__flores:
            print(i.getNombre())

    def getTipo(self):
        return self.__tamano

    def __str__(self):
        print("---------------------------------------------------------------------")
        s = '\n Tamaño:{}\n----------------'.format(self.__tamano)
        for i in self.__flores:
            s += '\n{}'.format(i.getNombre())
        return (s)
