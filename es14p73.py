class Quad:
    def _init_(self, lato):
        self.lato = lato
       
    def calcoloArea(self):
        return self.lato*self.lato
 
    def calcoloPerimetro(self):
        return self.lato*4

    def descrizione(self):
        return f"Nome: {self.lato}, area: {self.calcoloArea()}, Perimetro: {self.calcoloPerimetro()}"

    def puntoInterno(self, x, y):
        if(x > 0 and x < self.lato and y > 0 and y < self.lato):
            return True
        else:
            return False

def main():
    quadrato1 = Quad(3)
    print(quadrato1.descrizione())
    print(quadrato1.puntoInterno(4,5))

    quadrato2 = Quad(10)
    print(quadrato2.descrizione())
    print(quadrato2.puntoInterno(4,5))

if __name__ == "__main__":
    main()