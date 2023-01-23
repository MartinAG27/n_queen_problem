
#Algorithm of the N _ Queens problem

#This function puts a queen in the chesseboard
import time

def Poner_Reina(Reina, solucion):                               

    Q=0
    solucion = False

    while not solucion and Q < Dimension:                         #Recursive loop

        Tablero.append(Q)                                         
        Q += 1

        #Mostrar_Tablero(Reina)                                    #Show current queens on chessboard

        if(Validar(Reina)):                                       #Check if the queen's current move is valid

            if(Reina < Dimension-1 ):
                solucion = Poner_Reina(Reina+1,solucion)          #If is valid and Reina < Dimension-1  , call the Recursive function for puts a next queen 

                if(not solucion):                                 #Exits the current recursive function
                    #print("Por aqui no") 
                    Tablero.pop(Reina)
            else:
                solucion = True
                return solucion
                
        else:                                                     #If is invalid, delete the queen's current move
             Tablero.pop(Reina)
    return solucion


# This function Check a chess Queen rules

def Validar(Reina):         

    Colums         = False                            
    Right_diagonal = False  
    Left_diagonal  = False 

    for i in Tablero:                                           #Check rules for columns
        if i == Tablero[Reina]:
            Colums = not Colums
                                 
    n=0            
    for i in Tablero:                                           #Check rules for right diagonal
    
        if  Tablero[Reina] + Reina == Tablero[n] + n:       
            Right_diagonal = not Right_diagonal
        n+=1

    n=0 
    for i in Tablero:                                          #Check rules for left diagonal
        if  Reina - Tablero[Reina] == n - Tablero[n] :
            Left_diagonal = not Left_diagonal
        n+=1
               
    if Colums and Right_diagonal == 1 and Left_diagonal == 1: #Check if the three rules were valid    
        return True
    else:
        return False

 #This function show a Chessboard

def Mostrar_Tablero(n):                 

    for i in range(0,n+1):
        for j in range(0,Dimension):
            if j == Tablero[i]:    
                print("X" ,end= " ")
            else:
                print( 0,end= " ")    
        print("  ")
    print("  ")


# Main Function

if __name__ == '__main__':          

    Dimension = 8                                                       
    Tablero = []

    start = time.time()

    if Poner_Reina(0,False):
        print(f"Tablero de {Dimension} x {Dimension}. \n \nSolucion: \n")

        Mostrar_Tablero(Dimension-1)
    
    else:
        print(" \n No se encontro solucion al problema \n ")

    end = time.time()

    print("Tiempo de ejecucion", (end-start),"second")  

    #Using show function the program takes 16.75483226776123 second  within show function the program takes 0.03496527671813965 second          
  
