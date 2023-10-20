#disegnare una stella a n punte

nPunte = int(input("Inserisci il numero di punte della stella: "))
LungPunte = int(input("Inserisci la lunghezza delle punte: "))

import turtle
finestra = turtle.Screen() 
tartaruga = turtle.Turtle()

angolo = 360 / nPunte

for k in range(nPunte):
    tartaruga.forward(LungPunte)
    tartaruga.right(angolo)
    tartaruga.forward(LungPunte)
    tartaruga.left(2 * angolo)
    
finestra.mainloop()

