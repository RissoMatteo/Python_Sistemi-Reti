num1 = float(input("Inserisci il primo nuemro: "))
num2 = float(input("Inserisci il secondo numero: "))

num1, num2 = 5, 7 #assegnamento multiplo

if num2 > num1:
    num1,num2 = num2,num1
    
print(f"{num1} , {num2}")

#altro es
a = float(input("Inserisi un numero: "))
print(f"Il tipo di A è {type(a)}")
#
if a > 5: 
    print("A è maggiore di 5")
elif (a<=5) and (a >= 0):
    print("A è maggiore o uguale a zero e minore o uguale a 5")

else:
    print("A è <= a 5")