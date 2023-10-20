def print_list(l):                    #cambia sostanzialmente il tipo di stampa, provare sul terminale
    print("la lista è: ", end=" ")
    for elemento in l:
        print(elemento, end=" ")
    print("\n")

def concatenaLista(l):
    r = [10,20,30]
    print(l+r)       #concatena 2 liste
    print(l * 3)     #stampa 3 volte la lisa l

def main():
    #liste

    l = [1,2,3,4,"c",14.5]
    print(l)
    print_list(l[::-1])
    concatenaLista(l)

    #per chiedere all utente dei valori e metterli in lista:
    lista = []    #cosi di dichiara la lista vuota
    num = 1       #num 1 cosi entra nel while
    while num > 0:
        num = int(input("scrivi un numero: (-1 per interrompere)"))
        if num > 0:     #in modo che cosi quando inserisco -1 per uscire non me lo stampa nella lista
            lista.append(num)     #append aggiunge num alla lista
       
    print(lista)


if __name__=="__main__":
    main()