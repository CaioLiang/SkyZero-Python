#validação de entrada

#sistema

def main():
    print("\nBem vindo à SkyZero!")

    looping = True
    while looping:
        print("\nMENU PRINCIPAL!")
        print("\nDESENVOLVIMENTO!")
        looping = opcaoSaida()

    print("\nFim do programa, volte sempre!\n")

def opcaoSaida():
    while True:
        resposta = input(
            "\n=== OPÇÃO DE SAIR ===\n"
            "Quer sair do programa?\n"
            "1 - Sim\n"
            "2 - Não\n"
            "\nDigite o número da sua escolha: "
        )
        
        try:
            resposta = int(resposta)
            if resposta in [1, 2]:
                break
            else:
                print("Por favor, insira 1 para SIM ou 2 para NÃO.")
        except ValueError:
            print("Por favor, tipo de entrada errada, digite um valor inteiro!.")

    if resposta == 2: 
        return True
    else:
        return False