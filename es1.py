def main():   #definizione della funzione main
    nome = input("come ti chiami? ")
    anni = int(input("quanti anni hai? "))#la funzione input returna sempre e solo stringhe, per scoprirplo print(type(variabile))
    anno_corrente = int(input("in quale anno siamo? "))#int cosi per convertire le stringhe in interi altrimenti non potrei fare l' operazione successiva
    
    print(f"Il tuo nome è {nome} e hai {anni} anni")#si mette la f davanti perche devo concatenare una varianile nella print, in quella successiva ad esempio no
    print(f"Sei nato nel {anno_corrente - anni}") #python con la print va a capo sempre senza \n

if __name__ == "__main__":
    main()