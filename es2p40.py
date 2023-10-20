def main():
    num = int(input("Inserisci un nuemro: "))

    if num%2 == 0:
        print("E divisibile\n")
    elif num%3 == 0:
        print("E divisibile\n")
    elif num%5 == 0:
        print("E divisibile\n")
    else:
        print("Non è divisibile ne per 2 ne per 3 ne per 5")

if __name__ == "__main__":
    main()