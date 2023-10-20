def main():
    primo = 5
    secondo = 10

    print(f"Primo valore: {primo}, Secondo valore: {secondo}")

    primo,secondo = secondo,primo

    print(f"Primo valore: {primo}, Secondo valore: {secondo}")

if __name__ == "__main__":
    main()