import random
def calcolatrice1():

    def somma():
        a = int(input("Inserire il primo numero: "))
        b = int(input("Inserire il secondo numero: "))
        result = a+b
        print(f"Il risultato è: {result}")
        return

    def sottrazione():
        a = int(input("Inserire il primo numero: "))
        b = int(input("Inserire il secondo numero: "))
        result = a-b
        print(f"Il risultato è: {result}")
        return

    def moltiplicazione():
        a = int(input("Inserire il primo numero: "))
        b = int(input("Inserire il secondo numero: "))
        result = a*b 
        print(f"Il risultato è: {result}")
        return

    def divisione():
        a = int(input("Inserire il primo numero: "))
        b = int(input("Inserire il secondo numero: "))
        if b != 0:
            result = a / b
            print(f"Il risultato è: {result}")
        else:
            print(f"Errore! Divisione per zero.") 

    def calcolatrice():
        while True:
            print(f"-------------------------")
            print(f"1: Somma")
            print(f"2: Sottrazione")
            print(f"3: Moltiplicazione")
            print(f"4: Divisione")
            print(f"5: Uscire dalla calcolatrice")
            scelta = int(input("Scegliere un operazione: "))
            print(f"-------------------------")
            
            if scelta == 1:
                somma()
            elif scelta == 2:
                sottrazione()
            elif scelta == 3:
                moltiplicazione()
            elif scelta == 4:
                divisione()
            else:
                print(f"-------------------------")
                print(f"Inserire una scelta adeguata!")
                print(f"-------------------------")

            if scelta == 5:
                break
    calcolatrice()

def fraseinversa2():
    userInput = input("Inserisci una parola: ")

    stringaInversa = userInput[::-1]

    print(f"{stringaInversa}")

def indovinanumero3():
    numero_da_indovinare = random.randint(1, 50)

    print(f"Indovina il numero!")

    tentativi = 0

    while True:
        numero = int(input("Inserimento: "))
        tentativi += 1

        if numero > numero_da_indovinare :
            print(f"Il numero è troppo alto!")
        elif numero < numero_da_indovinare:
            print(f"Il numero è troppo basso")
        else:
            print(f"Il numero è corretto!")
            break

def numeroprimo4():
    def numeroPrimo():
        numeroUno = input("Insersici un numero primo ")
        numeroPrimo = int(numeroUno)

        if numeroPrimo/2 == 1 :
            print(f"è un numero primo")
            return False

        for i in range(2, int(numeroPrimo**0.5) + 1):
            if numeroPrimo % i == 0:  # If divisible, not prime
                print(f"non è un numero primo")
                return False
        print(f"è un numero primo")
        return True 

    numeroPrimo()


def giocoOrientamento():
    while True:
        print("#     #   #####")
        print("#     #   #    #")
        print(" #   #    #     #")
        print("  # #     #    #")
        print("   #      #####")
        print(f"Benvenuti! Ci sono diversi programmi:")
        print(f"------------------------------")
        print(f"1: Calcolatrice")
        print(f"2: Parole Inverse")
        print(f"3: Indovina Il Numero")
        print(f"4: Numero Primo")
        print(f"5: Uscire Dal Programma")
        scelta = int(input("Scegliere un operazione: "))
        print(f"------------------------------")
        
        if scelta == 1:
            calcolatrice1()
        elif scelta == 2:
            fraseinversa2()
        elif scelta == 3:
            indovinanumero3()
        elif scelta == 4:
            numeroprimo4()
        else:
            print(f"------------------------------")
            print(f"Inserire una scelta adeguata!")
            print(f"------------------------------")

        if scelta == 5:
            break
giocoOrientamento()