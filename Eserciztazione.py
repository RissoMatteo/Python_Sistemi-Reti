def main():
    file = open("covid-19_gen1.txt", "r")
    sequenzaGen = file.read()
    file.close()

    contA = sequenzaGen.count('A')
    contT = sequenzaGen.count('T')
    contG = sequenzaGen.count('G')
    contC = sequenzaGen.count('C')

    print(f'Occorrenze di A: {contA}')
    print(f'Occorrenze di T: {contT}')
    print(f'Occorrenze di G: {contG}')
    print(f'Occorrenze di C: {contC}')

    seqSpike = "ATGTTTGTTTTT"

    posSpike = -1

    for i, c in enumerate(sequenzaGen):
        if sequenzaGen[i:i+len(seqSpike)] == seqSpike:
            posSpike = i
            break

    if posSpike != -1:
        print(f'La sequenza inizia in posizione: {posSpike}')
    else:
        print('La sequenza non è presente')

if __name__ == "__main__":
    main()
