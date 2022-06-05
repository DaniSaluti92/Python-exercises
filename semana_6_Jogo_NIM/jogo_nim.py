def partida():
    n=int(input("Quantas peças?"))
    m=int(input("Limite de peças por jogada?"))
    r=n%(m+1)


    if (r==0):
         print("Você começa!")
         j=(usuario_escolhe_jogada(n,m))
         n=n-j
         if (n==0):
             print("Você ganhou!")
             c=0
         else:
             while (n>0):
                 j=(computador_escolhe_jogada(n,m))
                 n=n-j
                 if (n==0):
                     print("O computador ganhou!")
                     c=1
                     break
                 else:
                     j=(usuario_escolhe_jogada(n,m))
                     n=n-j
                     if (n==0):
                         print ("Você ganhou!")
                         c=0
                         break
                
                    
    else:
        print("Computador começa!")
        j=computador_escolhe_jogada(n,m)
        n=n-j
        if (n==0):
            print("O computador ganhou!")
            c=1
        else:
            while (n>0):
                j=usuario_escolhe_jogada(n,m)
                n=n-j
                if (n==0):
                    print ("Você ganhou!")
                    c=0
                    break
                else:
                    j=computador_escolhe_jogada(n,m)
                    n=n-j
                    if (n==0):
                        print ("O computador ganhou!")
                        c=1
                        break
    return c
   

def computador_escolhe_jogada(n,m):
    n=n
    j=1
    while (j<=m):
        sobra=n-j
        c=sobra%(m+1)
        
        if ((j==m) and (j==1)) or ((c==0) and (j==1)):
            print ("O computador tirou uma peça.")
            break
        if ((j==m) and (j!=1)) or ((c==0) and (j!=1)):
            print ("O computador tirou", j, "peças.")
            break
        else:
            j=j+1

                    
    if (sobra == 1):
        print ("Agora resta apenas uma peça no tabuleiro.")
    else:
        print ("Agora restam", sobra, "peças no tabuleiro.")
    return j
    


def usuario_escolhe_jogada(n,m):
    peças=n
    j=m+1
    while (j>m) or (j>peças) or (j<=0):
        j=int(input("Quantas peças você vai tirar?"))
        if ((j>m) or (j>peças) or (j<=0)):
            print ("Oops! Jogada inválida! Tente de novo")
            
    if (j<=m) and (j<=peças) and (j==1):
              print ("Você tirou uma peça")
    if (j<=m) and (j<=peças) and (j!=1):
              print ("Você tirou", j, "peças.")
    sobra=n-j

    
    if (sobra == 1):
        print ("Agora resta apenas uma peça no tabuleiro.")
    else:
        print ("Agora restam", sobra, "peças no tabuleiro.")

    return j
    

def campeonato():
    print("**** Rodada 1****")
    p1=partida()
    if (p1==1):
        c1=1
        u1=0
    else:
        c1=0
        u1=1
    
    print("****Rodada 2****")
    p2=partida()
    if (p2==1):
        c2=1
        u2=0
    else:
        c2=0
        u2=1

    print("****Rodada 3****")
    p3=partida()
    print(p3)
    if (p3==1):
        c3=1
        u3=0
    else:
        c3=0
        u3=1

    print("****Final do campeonato!****")

    c=(c1+c2+c3)
    u=(u1+u2+u3)

    print("Placar: Você ", u, "X", c, "Computador")

def main():
    print("Bem-vindo ao jogo NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    e=int(input("2 - para jogar um campeonato"))

    if (e==1):
        print("Você escolheu uma partida isolada!")
        partida()
        
    if (e==2):
        print("Você escolheu um campeonato!")
        campeonato()

main()
