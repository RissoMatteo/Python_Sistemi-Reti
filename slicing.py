#SLICING DI STRINGHE

c = "ciao come stai"
print(c[0])  #stampa il prima carattere
print(c[-1]) #stampa l'ultimo carattere
print(c[-2]) #stampa il penultimo carattere
#se mi interessano i primi carattere uso 0123... se mi interessano gli ultimi uso -1-2-3...

print(c[3:7]) #dal carattere 3 al carattere 7 esculuso (primo indice incluso ultimo escluso)

print(f"stampa tutta la scritta a parte il carattere 0 e l'ultimo carattere: {c[1:-1]}") 
print(f"stampa fino alla fine a parte il carattere 0: {c[1:]}") 
print(f"stampa fino alla fine a parte l'ultimo carattere: {c[:-1]}")
print(c[::-1]) #stampa la stringa al contrario