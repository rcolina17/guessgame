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
        