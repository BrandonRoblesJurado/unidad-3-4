import os
from pila import Pila
from cola import Cola
from lista import Lista

class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "4":
    os.system("cls")
    men = Menu("Menu Principal",["1)Operaciones Pila", "2)Operaciones Cola","3)Operacion Lista", "4)Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 = ""
        os.system("cls")
        num = int(input("Ingrese tamaño de Pila: "))
        pila1 = Pila(num)
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Operaciones Pila",["1)Ejercicios de Push", "2))Ejercicios de Pop", "3))Ejercicios de Show","4))Ejercicios de Longitud", "5))Ejercicios de Empty", "6)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Push")
                valor = int(input("Ingrese el valor:"))
                total = pila1.push(valor)
                if total == True:
                    print("El valor ha sido ingresado a la pila.")
                else:
                    print("La Pila ya esta llena") 
                input("CONTINUAR...")
                
            elif opc1 =="2":
                os.system("cls")
                print("Pop")
                total = pila1.pop()
                if total == None:
                    print("La Pila esta vacia")
                else:
                    print("El valor {} fue eliminado.".format(total))
                input("CONTINUAR")
                    
            elif opc1 =="3":
                os.system("cls")
                print("show")
                pila1.show()
                input("CONTINUAR...")
                
            elif opc1 =="4":
                os.system("cls")
                print("Longitud")
                valor = pila1.longitud()
                print("La pilas tiene una longitud de: {}".format(valor))
                input("CONTINUAR...")
                
            elif opc1 =="5":
                os.system("cls")
                print("Empty")
                valor = pila1.longitud()
                if valor:
                   print("La pila tiene elementos.")
                else:
                    print("La pila no tiene elementos, esta vacia.")
                input("CONTINUAR...")
                
    if opc == "2":
        opc1 = ""
        os.system("cls")
        num = int(input("Ingrese tamaño de cola: "))
        cola1 = Cola(num)
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Operaciones Cola",["1))Ejercicios de Push", "2))Ejercicios de Pop", "3))Ejercicios de Show","4))Ejercicios de Longitud", "5))Ejercicios de Empty", "6)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Push")
                valor = int(input("Ingrese el valor:"))
                total = cola1.push(valor)
                if total == True:
                    print("El valor ha sido ingresado a la cola.")
                else:
                    print("La cola ya esta llena") 
                input("CONTINUAR...")
                
            elif opc1 =="2":
                os.system("cls")
                print("Pop")
                total = cola1.pop()
                if total == None:
                    print("La cola esta vacia")
                else:
                    print("El valor {} fue eliminado.".format(total))
                input("CONTINUAR")
                    
            elif opc1 =="2":
                os.system("cls")
                print("Pop")
                total = cola1.pop()
                if total == None:
                    print("La cola esta vacia")
                else:
                    print("El valor {} fue eliminado.".format(total))
                input("CONTINUAR")
            elif opc1 =="3":
                os.system("cls")
                print("show")
                cola1.show()
                input("CONTINUAR...")
                
            elif opc1 =="4":
                os.system("cls")
                print("Longitud")
                valor = cola1.longitud()
                print("La cola tiene una longitud de: {}".format(valor))
                input("CONTINUAR...")
                
            elif opc1 =="5":
                os.system("cls")
                print("Empty")
                valor = cola1.longitud()
                if valor:
                   print("La cola tiene elementos.")
                else:
                    print("La cola no tiene elementos, esta vacia.")
                input("CONTINUAR...")
                                
    if opc == "3":
        opc1 = ""
        lista1=Lista()
        while opc1 != "8":
            os.system("cls")
            men1 = Menu("Menu Operaciones lista",["1: Agregar dato" , "2: Buscar" , "3: Mostrar lista" ,"4: insertar","5: Eliminar dato de la lista" , "6: Eliminar","7: Obtener posición" , "8: Salir al menu principal"])
            opc1 = men1.menu()
            if opc1 == "1":
                print("Ingresar elementos en una lista")
                dato = int(input("ingrese un dato a la lista: "))
                lista1.append(dato)
                print(lista1.lista)
                input("CONTINUAR....")
                
            elif opc1 =="2":
                os.system("cls")
                print("Buscar un valor en una lista")
                num = int(input("Ingrese numero a buscar: "))
                lista1.buscar(num)
                input("CONTINUAR....") 
                   
            elif opc1 =="3":
                os.system("cls")
                print("Mostrar elementos")
                lista1.mostrar()
                input("CONTINUAR....") 
                
            elif opc1 =="4":
                os.system("cls")
                num = int(input("Ingrese valor a insertar :"))
                pos = int(input("Ingrese posición :"))
                lista1.insertar(num, pos)
                input("CONTINUAR....")      
            
            
            elif opc1 =="5":
                os.system("cls")
                print("Eliminado El Elemento")
                posicion = int(input("Ingrese el valor para obtener el valor del elemento: "))
                resp = lista1.obtenerEliminado(posicion)
                if resp == None:
                    print("Posicion no valida, verifique la lista....!!! ")
                else:
                    print("El elemento de la posicion:{} es:{}".format(posicion,resp ))
                input("CONTINUAR....")   
                
            elif opc1 =="6":
                os.system("cls")
                print("Eliminar Lista")
                num = int(input("Ingrese valor a eliminar :"))
                lista1.eliminarLista(num)
                input("CONTINUAR....")
            
            elif opc1 =="7":
                os.system("cls")
                print("Obtener posición")
                posicion = int(input("Ingrese el valor para obtener la posición del elemento: "))
                print(Lista.obtener(posicion))
                input("CONTINUAR....")
                
            elif opc1 =="8":
                
                input("CONTINUAR....")    
                
    elif opc == "4":
        print("Gracias por usar el sistema")
    else:
        print("Opcion no valida") 

    print("Lo esperamos en una proxima ocasión")

