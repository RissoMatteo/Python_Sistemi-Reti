import turtle

def esegui_comandi(comandi):
    tartaruga = turtle.Turtle()

    for comando in comandi:
        if comando == 'F':
            tartaruga.forward(100)
        elif comando == 'R':
            tartaruga.right(90)
        elif comando == 'L':
            tartaruga.left(90)

    turtle.done()

def main():
    print("F = forward 100")
    print("R = right 90°")
    print("L = left 90°")
    comandi = input("Scrivi una sequenza di comandi: ")

    lista = list(comandi.upper())  # Converte i comandi in maiuscolo e li inserisce in una lista
    esegui_comandi(lista)

    # Aggiungi questa riga per attendere l'input prima di chiudere la finestra Turtle
    turtle.mainloop()

if __name__ == "__main__":
    main()
