from menu import Menu
from manejadorflores import ManejaFlores
from manejadorramo import ManejaRamo
if __name__=='__main__':
    menu=Menu()
    manejadorF=ManejaFlores()
    manejadorR=ManejaRamo()
    manejadorF.LeerArchivo()
    salir=False
    while not salir:
        print('------------------------------------------')
        print('1.Registrar ramo vendido')
        print('2.Mostrar el nombre de las 5 flores  más pedidas en un ramo')
        print('3.Mostrar flores segun el ramo')
        print('4.Salir')
        op=input('->')
        print('------------------------------------------')
        if(op=='1' or op=='2' or op=='3'):
            menu.opcion(op,manejadorF,manejadorR)
        salir = op =='4'
