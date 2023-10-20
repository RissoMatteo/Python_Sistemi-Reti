import turtle

n = int(input("Inserisci il numero dei lati del poligono ")) 
lato = int(input("Inserisci la lunghezza del lato "))
finestra = turtle.Screen()
angolo = 360 / n              # Calcola l'angolo per girare in base al numero di lati

turtle.color("red")  #do il colore alla linea
turtle.begin_fill()  #riempo il contorno di colore
turtle.speed(30)     #aumento la velocita di disegno

for k in range(0,n):
        
        turtle.forward(lato)  # Lunghezza del lato 
        turtle.left(angolo)

turtle.color("black")  #riempo il contorno di un colore diverso da quello della linea
turtle.end_fill()   #riempo il contorno di colore

finestra.mainloop()