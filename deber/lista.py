class Lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longuitud = 0
        self.size = tamanio

    def append(self,dato):
        if self.longuitud < self.size:
            self.lista += [dato]
            self.longuitud += 1
        else:
            print("Lista esta llena")
    
    def obtenerEliminado(self,pos):
        self.mostrar()
        if pos < 0 or pos >= self.longuitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista = self.lista[:pos] + self.lista[pos+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longuitud):
                listaAux += [self.lista[indice]]
            self.longuitud -=1
            self.lista = listaAux

            return eliminado,self.lista

    def mostrar(self):
        print("{:3}{:9} {}".format("","Lista","Posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:10}] {:4}".format(ele,pos))
            
    def buscar(self, valor):
        if valor in self.lista:
            print("Encontrado en la lista el ", valor)
            return True
        else:
            print("No existe en la lista el ", valor)
            return False
    
    # def insertar(self, valor):
    #     print("Lista original :",self.lista)
    #     if (self.buscar(valor)):
    #         print("No se puede insertar, ya se encuentra e la lista")
    #     else:
    #         self.lista.append(valor)
    
    def insertar(self, valor, posicion):
        print("Lista original :",self.lista)
        self.lista.insert(posicion, valor)
        print(self.lista)
            
    def eliminarLista(self, valor):
        print("Lista original :", self.lista)
        for item in self.lista:
            if (item == valor):
                self.lista.remove(valor) 
        print(self.lista)                        
    
    def obtener(self, pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]                       