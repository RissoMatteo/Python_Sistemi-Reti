def main():
    parola = "elefante"
    n = len(parola)
    for i in range(n):
        if i % 2 != 0:
            print(parola[i])

if __name__ == "__main__":
    main()