num1 = float(input("Inserisci il primo nuemro: "))
num2 = float(input("Inserisci il secondo numero: "))

if num2 > num1:
    num1,num2 = num2,num1

print(f"{num1} , {num2}")
