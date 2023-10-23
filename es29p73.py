def main():
    
    max = 10
    power = [[k * i for i in range(1, max + 1)] for k in range(1, max + 1)]  #parentesi quadre nel primo for in modo che quando strampa le tabelline escano definite da [] per ognu tabellina

    for k, tabellina in enumerate(power):     #enumerate ritrona l'indice della lista e il suo elemento, in py possiamo mettere 2 contatori in un for -> k, tabellina
        #tabellina è una lista, power è una lista di liste
        print(f"Tabellina del del {k + 1}: {tabellina}")


    #Stampo le tabelline sul file data.txt
    file = open("Data.txt", "w")
    for k, tabellina in enumerate(power): 
        file.write(f"Tabellina del del {k + 1}: {tabellina}\n")

    file.close

if __name__ == "__main__":
    main()