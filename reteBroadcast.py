def conversioneDecimale(ip_binario):
    gruppiDecimali = []
    for i in range(0,32,8): #da 0 a 32 pero a salti di 8
        ottetto = ip_binario[i:i+8]
        gruppiDecimali.append(str(int(ottetto, 2))) #questo è il gruppo fatto in decimale
    return ".".join(gruppiDecimali)

def main():
    ip_adress = (input("Inserisci un ip: "))
    cidr = int(input("Inserisci la notazione CIDR: "))
    subnet_mask = "1" * cidr + "0" * (32 - cidr)
    wild_card = "0" * cidr + "1" * (32 - cidr)

    subnet_maskDecimale = ".".join(str(int(subnet_mask[i:i+8],2))for i in range(0,32,8))
    wild_cardDecimale = ".".join(str(int(wild_card[i:i+8],2))for i in range(0,32,8))
    print(f"SubnetMask: " + subnet_maskDecimale)
    print(f"WildCard: " + wild_cardDecimale)

    #indirizzo ip binario
    ip_binary_group = [format(int(x), "08b") for x in ip_adress.split('.')]
    print(ip_binary_group)
    ip_binary = ''.join(ip_binary_group)
    print(ip_binary)
    ip_network = ip_binary[0:cidr] + "0" * (32 - cidr)
    ip_broadcast = ip_binary[0:cidr] + "1" * (32 - cidr)
    print(f"ip rete: {conversioneDecimale(ip_network)}")
    print(f"ip broadcast: {conversioneDecimale(ip_broadcast)}")
    

if __name__ == "__main__":
    main()
