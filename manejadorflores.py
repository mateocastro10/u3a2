import numpy as np
from flores import Flores
import csv
class ManejaFlores:
    __dimension=12
    __cantidad=0
    __incremento=1
    def __init__(self):
        self.__flores=np.empty(self.__dimension,dtype=Flores)
    def agregarFlor(self,flor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
            self.__flores[self.__cantidad]=flor
            self.__cantidad += 1
        else:
            self.__flores[self.__cantidad]=flor
            self.__cantidad += 1
    def LeerArchivo(self):
        archivo=open('flores.csv')
        reader=csv.reader(archivo, delimiter=',')
        for fila in reader:
            flor=Flores(int(fila[0]),fila[1],fila[2],fila[3])
            self.agregarFlor(flor)
        print('archivo leido')
    def Mostrar(self):
        for i in self.__flores:
            print(i)
    def buscarFlor(self,elemento):
        i=0
        resultado=None
        while i<len(self.__flores) and elemento!=self.__flores[i].getCodigo():
            i+=1
        if i<len(self.__flores):
            resultado=self.__flores[i]
        return resultado
    def MostrarFlores(self):
        self.__flores.sort()
        print('----------------flores vendidas-----------------')
        for i in range(0,5):
            if(self.__flores[i].getVendidas()!=0):
                print('Nombre:{}'.format(self.__flores[i].getNombre()))
