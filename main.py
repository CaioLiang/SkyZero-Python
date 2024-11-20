# GS - SkyZero
# Integrantes:
# Allan Brito Moreira - RM558948
# Caio Liang - RM558868
# Levi Magni - RM98276

from biblioteca import *

def main():
    print("\nBem vindo à SkyZero!")

    looping = True
    usuario = telaLogin()
    
    while looping:    
        
        if usuario != False:
            print("\nMENU PRINCIPAL!")
            print("\nDESENVOLVIMENTO!")

        looping = opcaoSaida()
    
if __name__ == "__main__":
    main()

caminho = 'credenciais.json'   
excluiCredenciais(caminho)

print("\nFim do programa, volte sempre!\n")
#SKYZERO @2024