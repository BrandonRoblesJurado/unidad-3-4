
class Matriz:
    def __init__(self,matriz,fila,columna):
        self.matriz=matriz
        self.fila=fila
        self.col=columna
        
    def ingresar(self,dato):
        pass
    
    
    
    def presentar (self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                # print(columna[col],end=" ")
                print(self.matriz[fila][col],end=" ")
            print()



    def buscar(self,valor):
        enc= False
        for pos1,ele1 in enumerate(self.matriz):
            for pos,ele in enumerate(ele1):
                    if ele==valor:
                        enc=True
                        buscar=(pos1,"columna",pos)
                        break
        if enc==True:
            return buscar
        else:
            return -1
        
        
        
    def buscar2(self,valor):
        enc={}
        band=True
        fila=0
        while fila < len(self.matriz)and band:
            col=0
            while col<len(self.matriz[fila])and band:
                if self.matriz[fila][col]==valor:
                    enc["fila"]=fila
                    enc["col"]=col
                    band=False
                else: col+=1
            fila+=1
        return enc
                       
     
numeros=[[10,20,30],[60,80,90],[25,35,55]]
mat=Matriz(numeros,5,3)
mat.presentar()
# print(numeros[0],numeros[0][1])
res=mat.buscar(80)
if res==-1:print("No existe valor en la matriz")
else:print("su Fila es: {}".format(res))

res=mat.buscar2(80)
if res:print("el valor se encuentra en las siguientes coordenadas: {}".format(res))
else:print("No existe valor en la matriz")