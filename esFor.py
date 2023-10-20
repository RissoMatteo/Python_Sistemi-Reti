lista = [4, 100, 3, 5, "ciao", print] #lista

#ciclo for c-style
for i in range(0, len(lista)):   #len mi dice la dimensione
    print(f"l'elemento {i} -esimo della lista e' {lista[i]}")

#ciclo python style
for elemento in lista:                      #vuol dire per ogni elemento in lista stampa elemento
    print(f"Elemento: {elemento}") 

#esempio
for i in range(0,8): #l'8 è esculuso
    print(f"i vale {i}")
