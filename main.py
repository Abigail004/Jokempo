import random

continuar = "sim"

computador = ["pedra", "papel", "tesoura"]
jogada_computador = random.choice(computador)


while continuar == "sim":
    jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    
    print("\n")

    jogador = jogador.lower()

    if jogador != "papel" and jogador != "tesoura" and jogador != "pedra":
        print("tente outra vez!!\n")
    
    else:
        
        if jogador == jogada_computador:
            print(f"Você jogou {jogador.upper()}")
            print(f"eu joguei {jogada_computador.upper()}")
            print("Nós empatamos!!\n")
        
        elif jogador == "pedra":
            if jogada_computador == "papel":
                print(f"Você jogou {jogador.upper()}")
                print(f"eu joguei {jogada_computador.upper()}")
                print("Você perdeu!!\n")
            else:
                print(f"Você jogou {jogador.upper()}")
                print(f"eu joguei {jogada_computador.upper()}")
                print("Você ganhou!!!\n")
            
        elif jogador == "papel":
            if jogada_computador == "tesoura":
                print(f"Você jogou {jogador.upper()}")
                print(f"eu joguei {jogada_computador.upper()}")
                print("Você perdeu!!\n")
            else:
                print(f"Você jogou {jogador.upper()}")
                print(f"eu joguei {jogada_computador.upper()}")
                print("Você ganhou!!!\n")
        
        elif jogador == "tesoura":
            if jogada_computador == "pedra":
                print(f"Você jogou {jogador.upper()}")
                print(f"eu joguei {jogada_computador.upper()}")
                print("Você perdeu!!\n")
            else:
                print(f"Você jogou {jogador.upper()}")
                print(f"eu joguei {jogada_computador.upper()}")
                print("Você ganhou!!!\n")
     
    continuar = input("você deseja continuar sim ou não".lower())
    
