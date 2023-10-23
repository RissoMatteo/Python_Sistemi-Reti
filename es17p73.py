import math #libreria matematica di python

def main():

    num = int(input("Inserisci un numero: "))
    esponente = int(math.log2(num))
    lista = [2**i for i in range(0, esponente + 1) if 2**2 <= num]

    print(lista)

if __name__ == "__main__":
    main()