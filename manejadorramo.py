from ramo import Ramo
from manejadorflores import ManejaFlores
class ManejaRamo:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def Venta(self,manejaF):
        band=True
        i=0
        lista=[]
        while(band):
            print("---------------------------------------------------------------------")
            venta=int(input('ingrese codigo de flores a comprar (para terminar ingrese 0):'))
            if(venta==0):
                band=False
            else:
                Flor=manejaF.buscarFlor(venta)
                if(Flor!=None):
                    lista.append(Flor)
                    i+=1 #cantidad de flores vendidas
                    Flor.setVenta()
                    print('Flor agregada al ramo!')
                else:
                    print('Esa flor no la tenemos a la venta!')
        if(i!=0):
            ramo=Ramo(i)
            ramo.setFlores(lista)
            print(ramo)
            self.__lista.append(ramo)
            print("---------------------------------------------------------------------")
            print('Ramo vendido!')
    def RamosVendidos(self):
        ramo=input('ingrese tipo de ramo:')
        for i in self.__lista:
            if(i.getTipo()==ramo):
                print('flores-----\n')
                i.mostrarFlores()
