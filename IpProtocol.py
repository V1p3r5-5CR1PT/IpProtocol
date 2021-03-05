doloop = True
while doloop:
        print("Inserisci l'ip:")
        print("es: 192.168.1.1/14")
        x = input()
        y = x.split('/')
        z = y[0].split('.')
        s = int(y[1])
        uno = int(z[0])
        due = int(z[1])
        tre = int(z[2])
        qua = int(z[3])
        bit = [1]
        for i in range(1,s,1):
                bit.append(1)
        bitt = ''.join([str(elem) for elem in bit])
        bits = bitt + '0' * (8 - len(bitt) % 8)
        print("Bit Prefisso rete: ", bits)
        if (uno<=127):
                classe = "A"
                print("Classe:",classe)
                print("Indirizzo di Rete: ",uno,".0.0.0")
                print("Indirizzo di BroadCast: ",uno,".255.255.255")
                print("Subnet Mask:")
                print("255.0.0.0 11111111.00000000.00000000.00000000")
        elif (uno<=191):
                classe = "B"
                print("Classe: ",classe)
                print("Indirizzo di Rete: ",uno,".",due,".0.0")
                print("Indirizzo di BroadCast: ",uno,".",due,".255.255")
                print("Subnet Mask:")
                print("255.255.0.0 11111111.11111111.00000000.00000000")
        elif (uno<=223):
                classe = "C"
                print("Classe: ",classe)
                print("Indirizzo di Rete: ",uno,".",due,".",tre,".0")
                print("Indirizzo di BroadCast: ",uno,".",due,".",tre,".255")
                print("Subnet Mask:")
                print("255.255.255.0 11111111.11111111.11111111.00000000")
        elif (uno<=239):
                classe = "D"
                print("Classe: ",classe)
        else:
                classe = "E"
                print("Classe: ",classe)
        print("Per continuare premere s e poi invio")
        print("Se hai finito chiudi l'eseguibile")
        uwu = input()
        if (uwu!='s'):
                break
