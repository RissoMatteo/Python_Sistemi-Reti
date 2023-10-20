import turtle
nLati = 3
lato = int(input("Inserisci la lunghezza del lato "))
finestra = turtle.Screen()

for lato in range(3,10):
    angolo = 360 / nLati
    for k in range(nLati):
        turtle.forward(lato)
        turtle.left(angolo)
        nLati = nLati + 1
turtle.penup()
turtle.forward(70)
turtle.pendown()


finestra.mainloop()