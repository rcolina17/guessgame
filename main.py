import random
def humanguess():
    number=random.randrange(0,10)
    print(number)

    numero=-1

    while numero!=number:
        numero=int(input("Dame un numero del 1 al 10 "))
    
        if number==numero:
            print(f"Felicidades ganaste {number}")

        elif number > numero:
            print(f"El numero {number} es mayor")

        else:
            print(f"El numero {number} es menor")

    humanguess()

def computerGuess():
    #Escogi el 500
    firstNumber=0
    secondNumber=1000
    number=random.randrange(firstNumber,secondNumber)
    bandera=False
    
    
    while(bandera==False):
        print (number)
        print ("Este es tu numero?")
        opc=input("si | no: ").lower()
        if (opc =="no"):
            print("Tu numero es mayor o menor al mio?")
            opc2=input("mayor | menor: ").lower()
            if(opc2=="menor"):
                secondNumber=number
                newNumber=random.randrange(firstNumber,secondNumber)#el de la computadora es mayor
                number = newNumber
            
            else:#en caso de que sea mayor
                firstNumber=number
                newNumber=random.randrange(firstNumber,secondNumber)
                number=newNumber
        else:
            bandera=True
            print('Ganaste')
computerGuess()

