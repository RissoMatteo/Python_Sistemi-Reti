import math

def main():
    #soluzione migliore: 
    lista = [i ** 2 for i in range(0, int(math.sqrt(200)) + 1) if i % 2 != 0]  #bisognerebbe farlo arrivare fino alla radice quadrata di 200 per sofdddisfare l'esercizio
    print(f"Quadrati perfetti dispari: {lista}")

def main1():
    lista = [i ** 2 for i in range(0, 1000) if (i % 2 != 0) and (i ** 2 < 200)]
    print(f"Quadrati perfetti dispari: {lista}")

if __name__ == "__main__":
    main()