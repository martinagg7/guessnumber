import random
def juego(nivel):
    minlim=0
    ganar=False
    if nivel==1:
        numero=random.randint(0,100)
        intentoslim=10
        texto="Escoge un numero entre 0 y 100, introduce -1 para ayuda: "
        maxlim=100
    if nivel==2:
        numero=random.randint(0,1000)
        intentoslim=15
        texto="Escoge un numero entre 0 y 1000 ,introduce -1 para ayuda  : "
        maxlim=1000
    if nivel==3:
        numero=random.randint(0,1000000)
        intentoslim=20
        texto="Escoge un numero entre 0 y 1000000 ,introduce -1 para ayuda : "
        maxlim=10000000
    if nivel==4:
        numero=random.randimt(0,1000000000000)
        intentoslim=25
        texto="Escoge un numero entre el 0 y el 1000000000000 ,introduce -1 para ayuda : "
        maxlim==1000000000000 
    intentos=0
    while intentos<intentoslim :
        
        numeroescogido=int(input(texto))
        if numeroescogido==-1:
            print("el numero esta entre   " + str(minlim) +" y " + str(maxlim))
        else:
            intentos=intentos+1


        
            print(numero)
            if numeroescogido<numero:
                print("demasiado pequeño")
                if numeroescogido>minlim:
                    minlim=numeroescogido
                

            elif numeroescogido>numero:
                print("demasiado grande")
                if numeroescogido<maxlim:
                    maxlim=numeroescogido
            else:
                print("ha acertado")
                ganar=True
                break
    if ganar==False:
        print("Superaste el numero de intentos")
    else:
        print("Se han utilizado"    + str(intentos) +   "intentos")
    return ganar,intentos




nivel=0
puntuacion=""
while True:
    print("Escoge tu nivel o salir del juego")       
    print("1-(0,100)")
    print("2-(0,1000)")
    print("3-(0,1000000)")
    print("4-(0,1000000000)")
    print("5-salir del juego")


    nivel=int(input("Escoge tu opcion: "))
    if nivel==5:
        break

    resultado,numerodeintentos=juego(nivel)
    if resultado==True:
        nombre=input("Nombre jugador: ")
        puntuacion=puntuacion + " "+ nombre + " " +str(numerodeintentos)  +"\n"
print("tabla de puntaciones")
print(puntuacion)




    

       
       

   


   
    




