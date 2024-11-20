from conexaoBD import *  
import os
import re

#VALIDAÇÃO DE ENTRADA

#<login>

def validaNomeEmpresa(nome):
    while True:
        if len(nome.strip()) > 0:
            return nome
        else:
            print("\nNome da empresa inválido. Por favor, insira um nome válido.")
            nome = input("\nPor favor, insira o nome da empresa: ")

def validaEmail(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while True:
        if re.match(pattern, email):
            
            lista_email_cadastrados = [] 
            query_script = 'SELECT email FROM tb_usuario'
            email_brutos = comandoConexaoBD(query_script)
            
            for item_email in email_brutos:
                lista_email_cadastrados.append(item_email[0])        
            
            if email not in lista_email_cadastrados:
                return email 
            
            print(f"\EMAIL '{email}' JÁ CADASTRADO!")
            email = input("\nDigite outro Email: ")

        else:
            print("\nEmail inválido. Por favor, insira um email válido.")
            email = input("\nPor favor, insira o email de contato: ")

def validaCnpj(cnpj):
    pattern = r'^\d{14}$'
    while True:
        if re.match(pattern, cnpj):
            lista_cnpj_cadastrados = [] 
            query_script = 'SELECT cnpj FROM tb_usuario'
            cnpj_brutos = comandoConexaoBD(query_script)
            
            for item_cnpj in cnpj_brutos:
                lista_cnpj_cadastrados.append(item_cnpj[0])        
            
            if cnpj not in lista_cnpj_cadastrados:
                return cnpj 
            
            print(f"\nCNPJ -{cnpj}- JÁ CADASTRADO!")
            cnpj = input("\nDigite outro CNPJ: ")
        else:
            print("\nCNPJ inválido. Por favor, insira um CNPJ com 14 dígitos.")
            cnpj = input("\nPor favor, insira o CNPJ da empresa: ")

#SISTEMA

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
    
def telaLogin():
    while True:
        print(
                "\n=== MENU LOGIN ===\n"
                "1 - Login\n"
                "2 - Cadastrar usuário\n"
                "3 - Sair"
            )
        
        escolha = input("\nDigite o número da sua escolha: ").strip()
            
        try:
            escolha = int(escolha)
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        match escolha:
            case 1:
                return realizarLogin()
            case 2:
                return menuCadastro()
            case 3:
                return False
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

#<submenus>
            
def menuCadastro():
    
    print("\n=== MENU CADASTRO ===\n")
    
    credenciaisJson()
    
    nomeEmpresa = input("\nPor favor, insira o nome da empresa: ")
    nomeEmpresa = validaNomeEmpresa(nomeEmpresa)
    email = input("\nPor favor, insira o email de contato: ")
    email = validaEmail(email)
    cnpj = input("\nPor favor, insira o CNPJ da empresa: ")
    cnpj = validaCnpj(cnpj)
        
    usuario = {
        'nomeEmpresa' : nomeEmpresa,
        'email' : email,
        'cnpj' : cnpj
    }
    
    query_script = f"INSERT INTO tb_usuario (NOMEEMPRESA, EMAIL, CNPJ) VALUES ('{usuario['nomeEmpresa']}', '{usuario['email']}', '{usuario['cnpj']}')"
    comandoConexaoBD(query_script)
    
    return usuario
    
def realizarLogin():
    print("OI")
    usuario = {'caio':'12345'}
    return usuario

#<conexão com banco de dados>
def comandoConexaoBD(query_script):
    while True:
        try:
            conn = conecta_banco()
            cursor = conn.cursor()
            cursor.execute(query_script)  

            if query_script.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                conn.commit()
            
            if query_script.strip().upper().startswith('SELECT'):
                resultados = cursor.fetchall()
                
                if resultados:
                    print("\nConsulta retornou resultados.")
                else:
                    print("\nConsulta não retornou resultados.")
                
                print("Comando executado com sucesso!\n")
                return resultados
            
            print("Comando executado com sucesso!\n")
            break
        except Exception as e: 
            print("\nERRO DE CREDENCIAIS\n")
            print(f"\nErro: {e}\n")
            credenciaisJson()  

    cursor.close()
    conn.close()

def credenciaisJson():
    import json
    
    print("\nCONEXÃO COM BANCO DE DADOS\n" +
          "\nForneça suas credencias para conexão com banco de dados da ORACLE - FIAP: \n")
    
    print("\nNota: digite seu LOGIN no seguinte modelo 'rm ou p' + 'numeros' | ex: rm111111 \n")
    
    user = input("Digite o seu login: ")
    password = input("Digite a sua senha: ")
    
    
    dict_credenciais = {
        'login' : user,
        'senha' : password
    }
        
    with open (f'credenciais.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dict_credenciais, arquivo, ensure_ascii= False, indent=4)  
        
    print("\n-----------------EXPORTADO CREDENCIAIS-----------------\n")
        
def excluiCredenciais(arquivo):
    try: 
        os.path.exists(arquivo)
        os.remove(arquivo)
        print(f'\nO arquivo {arquivo} foi apagado com sucesso.')
    except:
        print(f'\nO arquivo {arquivo} não foi encontrado.')    
