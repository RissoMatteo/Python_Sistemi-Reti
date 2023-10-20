#disegnare i primi 9 poligoni regolari in una finestrs turtle

import turtle

finestra = turtle.Screen()
tartaruga = turtle.Turtle()

def disegnaPoligono(nLati, lunglato):
    angolo = 360 / nLati

    for k in range(nLati):
        tartaruga.forward(lunglato)
        tartaruga.right(angolo)

def disegnoPoligoni():
    lungLato = 30

    for nLati in range(3,12):
        disegnaPoligono(nLati, lungLato)


    finestra.mainloop()

disegnoPoligoni()

