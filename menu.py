from manejadorflores import ManejaFlores
from manejadorramo import ManejaRamo
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher= {'1':self.opcion1,
                          '2':self.opcion2,
                          '3':self.opcion3,
                          '4':self.salir}
    def opcion(self,op,manejadorF,manejadorR):
        func=self.__switcher.get(op,lambda: print('Opcion no valida'))
        if(op=='1' or op=='2' or op=='3'):
            func(manejadorF,manejadorR)
        else:
            func()
    def opcion1(self,manejadorF,manejadorR):
        if(type(manejadorR)==ManejaRamo and type(manejadorF)==ManejaFlores):
            manejadorF.Mostrar()
            manejadorR.Venta(manejadorF)
    def opcion2(self,manejadorF,manejadorR):
        if(type(manejadorR)==ManejaRamo and type(manejadorF)==ManejaFlores):
            manejadorF.MostrarFlores()
    def opcion3(self,manejadorF,manejadorR):
        if(type(manejadorR)==ManejaRamo and type(manejadorF)==ManejaFlores):
            manejadorR.RamosVendidos()
    def salir(self):
        print('finalizado...')
