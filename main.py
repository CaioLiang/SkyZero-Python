# GS - SkyZero
# Integrantes:
# Allan Brito Moreira - RM558948
# Caio Liang - RM558868
# Levi Magni - RM98276

from biblioteca import *

def main():
    print("\nBem vindo à SkyZero!")

    contador_registro = 1
    looping = True
    usuario = telaLogin()
    
    while looping:    
        
        if usuario != False:
            contador_registro = telaPrincipal(usuario, contador_registro)

        looping = opcaoSaida()
    
if __name__ == "__main__":
    main()

caminho = 'credenciais.json'   
excluiCredenciais(caminho)

print("\nFim do programa, volte sempre!\n")
#SKYZERO @2024