def main():
    
    segno = (input("Inserisci il segno dell operazione da eseguire(+,-,*,/) "))
    num = int(input("Inserisci un nuemro: "))
    num1 = int(input("Inserisci un nuemro: "))

    if segno == '+':
        print(f"La somma è: {num + num1}")
    elif segno == '-':
        print(f"La  sottrazione è: {num - num1}")
    elif segno == '/':
        print(f"La divisione è: {num / num1}")
    elif segno == '*':
        print(f"La moltiplicazione è: {num * num1}")

if __name__ == "__main__":
    main()
