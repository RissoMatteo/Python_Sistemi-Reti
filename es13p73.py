class Robot:
    def _init_(self, nome, massa, tipologia):
        self.nome = nome
        self.massa = massa
        self.tipologia = tipologia 

    def stampaNome(self):
        print(f"nome robot: {self.nome}")

    def pericoloso(self):
        return (self.tipologia == 'umanoide' and self.massa > 100)

def main():
    r = Robot("Gino", 100, 'noUmanoide')
    rp = Robot("Mario", 101, 'umanoide')
    r.stampaNome()
    print(f"massa: {r.massa} ")
    if r.pericoloso()==True:
        print("è pericoloso")
    rp.stampaNome()
    print(f"massa: {rp.massa} ")
    if rp.pericoloso()==True:
        print("è pericoloso")


if __name__ == "_main_":
    main()