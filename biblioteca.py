from conexaoBD import *  
import os
import re
from datetime import datetime

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

def validaSenha(senha):
    while True:
        if len(senha) >= 8:
            return senha
        print("\nSenha fraca! Mínimo de 8 caracteres\n")
        senha = input("Cadastre a senha do seu Login: ")
    
def tratarDadosBrutos(dados_brutos):
    lista_tratada = []
    for item in dados_brutos:
        lista_tratada.append(item[0]) 
    
    return lista_tratada        
            
def entradaCnpj(cnpj):
    pattern = r'^\d{14}$'
    while True:
        if re.match(pattern, cnpj):         
            return cnpj 

        print("\nCNPJ inválido. Por favor, insira um CNPJ com 14 dígitos.")
        cnpj = input("\nPor favor, insira o CNPJ da empresa: ")
        
def validaDistancia(distancia):
    while True:
        if not distancia.strip():
            print("Erro: A distância não pode estar vazia.")
        
        try:
            distancia_float = float(distancia)
            if distancia_float > 0:
                return distancia_float
            print("Erro: Distância inválida! Digite um valor acima de 0.")
        except ValueError:
            print("Erro: A distância deve ser um número (float).")
        
        distancia = input("Digite a distância em KM: ")

def validaAviao(tipo_aviao):
    """
    Valida se a entrada 'tipo_aviao' é 1 ou 2.
    
    Retorna o valor de 'tipo_aviao' se for válido,
    caso contrário, continua pedindo uma entrada válida.
    """
    while tipo_aviao not in ['1', '2']:
        print("Opção inválida. Por favor, insira 1 para Avião de carga ou 2 para Avião de passageiros.")
        tipo_aviao = input("Digite uma das opções: ")

    if tipo_aviao == '1':
        return "CargoAirplane"
    
    return "PassengerAirplane"

def validaOpcao(opcao):
    """
    Valida se a entrada 'opcao' é 1 ou 2.
    
    Retorna o valor de 'opcao' se for válida,
    caso contrário, continua pedindo uma entrada válida.
    """
    while opcao not in ['1', '2']:
        print("Opção inválida. Por favor, insira 1 para Cálculo de CO₂ ou 2 para Sair.")
        opcao = input("Digite uma das opções: ")

    return opcao

def validaQuantidadePassageiros(quantidade):
    """
    Valida se a entrada 'quantidade' é um número (int),
    maior que zero e não excede 1000 passageiros.
    
    Retorna True se a validação for bem-sucedida, caso contrário, retorna False.
    """
    while True:
        try:
            quantidade = int(quantidade)
            
            if quantidade > 0 and quantidade <= 1000:
                return quantidade
            else:
                print("Erro: A quantidade deve ser maior que zero e menor ou igual a 1000.")
        except ValueError:
            print("Erro: A quantidade deve ser um número.")
        
        quantidade = input("Digite a quantidade de passageiros: ")

def validaPesoAviao(quantidade):
    """
    Valida se a entrada 'quantidade' não é nula, é um número (float),
    diferente de zero e positivo.
    
    Retorna o valor convertido para float se a validação for bem-sucedida,
    caso contrário, continua pedindo uma entrada válida.
    """
    while True:
        try:
            if not quantidade.strip():
                raise ValueError("O peso não pode estar vazio.")
            quantidade_float = float(quantidade)
            if quantidade_float > 0:
                return quantidade_float
            else:
                raise ValueError("O peso deve ser um número positivo e diferente de zero.")
        except ValueError as e:
            print(f"Erro: {e}")
            quantidade = input("Digite o peso do avião em toneladas: ")


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

def telaPrincipal(usuario, contador_registro):
    
    while True:
        print(
                "\n===BEM VINDO AO SISTEMA DE CALCULO DE EMISSAO DE CO₂ POR VIAGEM AÉREA===\n"
                "\n=== MENU PRINCIPAL ===\n"
                "1 - Cálculo de CO₂\n"
                "2 - Sair\n"
            )
        opcao_menu_principal = input("Digite uma das opções : ")
        opcao_menu_principal = validaOpcao(opcao_menu_principal)
        
        if opcao_menu_principal == '1':
            print("\n---TIPO DE AVIÃO---\n"
                "1 - Avião de carga\n"
                "2 - Avião de passageiros\n")
            tipo_aviao = input("Digite uma das opções: ")
            tipo_aviao = validaAviao(tipo_aviao)
            
            if tipo_aviao == "PassengerAirplane":
                quantidade_tipo_aviao = input("\nDigite a quantidade de passageiros: ")
                quantidade_tipo_aviao = validaQuantidadePassageiros(quantidade_tipo_aviao)
            else:
                quantidade_tipo_aviao = input("\nDigite o peso do avião em toneladas: ")
                quantidade_tipo_aviao = validaPesoAviao(quantidade_tipo_aviao)
            
            print("\n---DISTÂNCIA DA VIAGEM---\n")
            distancia = input("Digite a distância em KM: ")
            distancia = validaDistancia(distancia)
            
            dict_calculo_carbono = postAPI(tipo_aviao, distancia)
            emissao_viagem = dict_calculo_carbono['emission']
            
            emissao_total = emissao_viagem * quantidade_tipo_aviao
            
            relatorio_json = {
            'cnpj' : usuario['cnpj'],
            'type' : tipo_aviao,
            'distancia' : distancia, 
            'quantidadeTipoAviao' : quantidade_tipo_aviao,
            'emissaoCalculada' :  emissao_viagem, 
            'emissaoTotal' : emissao_total,
            'dataRegistro' : f'{datetime.today().date()}'   
            }

            query_script = f"SELECT id_usuario FROM tb_usuario WHERE cnpj = {usuario['cnpj']}"
            id_usuario_bruto = comandoConexaoBD(query_script)
            
            for id in id_usuario_bruto: 
                id_usuario_login = id[0]
            
            print("\n-----------------CADASTRANDO REGISTRO NO BANCO DE DADOS-----------------")
            query_script = f"INSERT INTO tb_registro (ID_USUARIO, TIPO_AVIAO, DISTANCIA, EMISSAOCALCULADA, DATA_REGISTRO) VALUES ({id_usuario_login},'{relatorio_json['type']}', {relatorio_json['distancia']}, {relatorio_json['emissaoTotal']}, TO_DATE('{relatorio_json['dataRegistro']}', 'YYYY-MM-DD'))"
            comandoConexaoBD(query_script)

            imprimirRelatorio(relatorio_json)

            contador_registro = exportarJson(relatorio_json, contador_registro)
            
        return contador_registro
    
#<submenus>

def postAPI(tipo_aviao, distancia):
    import requests

    while True:
        url = 'https://api-calculators.carbonext.com.br/v2/calculators/distance'

        headers = {
            'Content-Type' : 'application/json'
        }

        try:
            dados = {
                "type": tipo_aviao,
                "distance": distancia,
                "currency": "BRL"
            }

            response = requests.post(url, headers=headers , json=dados)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro: {response.status_code}")
        except Exception as e:
            print(e)
        
        distancia = input("Digite a distância em KM: ")
        distancia = validaDistancia()
        print("------TIPO DE AVIÃO------\n"
                "1 - Avião de carga\n"
                "2 - Avião de passageiros")
        tipo_aviao = input("Digite uma das opções: ")
        tipo_aviao = validaAviao()
            
def menuCadastro():
    
    print("\n=== MENU CADASTRO ===")
    
    nomeEmpresa = input("\nPor favor, insira o nome da empresa: ")
    nomeEmpresa = validaNomeEmpresa(nomeEmpresa)
    email = input("\nPor favor, insira o email de contato: ")
    email = validaEmail(email)
    cnpj = input("\nPor favor, insira o CNPJ da empresa: ")
    cnpj = validaCnpj(cnpj)
   
    print("\n---INFO---")
    print("\nSeu LOGIN será do seguinte formato: \n"
          "Usuário: CNPJ\n"
          "Senha: SENHA\n")
    senha = input("\nCadastre a SENHA do seu login: ")
    senha = validaSenha(senha)
    usuario = {
        'nomeEmpresa' : nomeEmpresa,
        'email' : email,
        'cnpj' : cnpj,
        'login' : 
            {
            'senha' : senha
            }
    }
    
    print("\n-----------------CADASTRANDO USUÁRIO NO BANCO DE DADOS-----------------")
    query_script = f"INSERT INTO tb_usuario (NOMEEMPRESA, EMAIL, CNPJ) VALUES ('{usuario['nomeEmpresa']}', '{usuario['email']}', '{usuario['cnpj']}')"
    comandoConexaoBD(query_script)
    
    query_script = f"SELECT id_usuario FROM tb_usuario WHERE cnpj = {cnpj}"
    id_usuario_bruto = comandoConexaoBD(query_script)
    
    for id in id_usuario_bruto: 
        id_usuario_login = id[0]
        
    print("\n-----------------CADASTRANDO LOGIN NO BANCO DE DADOS-----------------")
    query_script = f"INSERT INTO tb_login (ID_USUARIO, LOGIN, SENHA) VALUES ({id_usuario_login}, '{usuario['cnpj']}', '{usuario['login']['senha']}')"
    comandoConexaoBD(query_script)
    
    return usuario
    
def realizarLogin():
    
    while True:
        print("\n=== LOGIN ===" )
        
        login_usuario = input("Digite seu CPNJ: ")
        login_usuario = entradaCnpj(login_usuario)
        
        login_senha = input(f"Digite a sua senha do seu usuário: ")
        login_senha = validaSenha(login_senha)
        
        validador_login = False
        
        query_script = 'SELECT login FROM tb_login'
        cnpj_brutos = comandoConexaoBD(query_script)
        cnpj_brutos = tratarDadosBrutos(cnpj_brutos)     
        
        tipo_erro =  "Usuário não registrado!" 
        
        if login_usuario in cnpj_brutos:
            query_script = f"SELECT senha FROM tb_login WHERE login = '{login_usuario}'"
            senha_brutos = comandoConexaoBD(query_script)
            senha_brutos = tratarDadosBrutos(senha_brutos)
            
            tipo_erro =  "Senha inválida!" 
            
            if login_senha in senha_brutos:
                validador_login = True
            
            if validador_login:

                query_script = f"SELECT NOMEEMPRESA FROM tb_usuario WHERE cnpj = '{login_usuario}'"
                nome_empresa_brutos = comandoConexaoBD(query_script)
                
                nome_empresa_brutos = tratarDadosBrutos(nome_empresa_brutos)
                nomeEmpresa = nome_empresa_brutos[0]
                
                query_script = f"SELECT email FROM tb_usuario WHERE cnpj = '{login_usuario}'"
                email_brutos = comandoConexaoBD(query_script)
                
                email_brutos = tratarDadosBrutos(email_brutos)
                email = email_brutos[0]
                
                usuario = {
                    'nomeEmpresa' : nomeEmpresa,
                    'email' : email,
                    'cnpj' : login_usuario,
                    'login' : 
                        {
                        'senha' : login_senha
                        }
                }
                
                return usuario
            
        decisao_cadastro = input(
                f"\n--- {tipo_erro} ---\n"
                "\n--- DESEJA CADASTRAR ---\n" 
                    "1 - Sim\n"
                    "2 - Não\n"
                    "\nDigite uma das opções: ")        
        
        if decisao_cadastro == '1':
            return menuCadastro()

def imprimirRelatorio(relatorio_json):
    
    if relatorio_json['type'] == 'PassengerAirplane':    
        print("\n=== RELATÓRIO DE VIAGEM ===\n")
        print(f"CNPJ do Usuário        : {relatorio_json['cnpj']}")
        print(f"Tipo de Avião          : {relatorio_json['type']}")
        print(f"Distância Percorrida   : {relatorio_json['distancia']} km")
        print(f"Qtde de passageiro     : {relatorio_json['quantidadeTipoAviao']} de pessoa(s)")
        print(f"Emissão Calculada      : {relatorio_json['emissaoCalculada']} t de CO₂")
        print(f"Emissão Total          : {relatorio_json['emissaoTotal']} t de CO₂")
        print(f"Data do Registro       : {relatorio_json['dataRegistro']}")
        print("\n=============================\n")
    elif relatorio_json['type'] == 'CargoAirplane':
        print("\n=== RELATÓRIO DE VIAGEM ===\n")
        print(f"CNPJ do Usuário        : {relatorio_json['cnpj']}")
        print(f"Tipo de Avião          : {relatorio_json['type']}")
        print(f"Distância Percorrida   : {relatorio_json['distancia']} km")
        print(f"Peso do Avião          : {relatorio_json['quantidadeTipoAviao']} t")
        print(f"Emissão Calculada      : {relatorio_json['emissaoCalculada']} t de CO₂")
        print(f"Emissão Total          : {relatorio_json['emissaoTotal']} t de CO₂")
        print(f"Data do Registro       : {relatorio_json['dataRegistro']}")
        print("\n=============================\n")
    
def exportarJson(relatorio_json, contador_registro): 
    
    print("\nDeseja exportar relatório em JSON?\n" 
      "1 = Sim\n"  
      "2 = Não\n")

    exportar = input("Digite uma das opções: ")
    
    while exportar not in ['1', '2']:
        print("Opção inválida. \nPor favor, digite 1 = SIM ou 2 = NÃO")
        exportar = input("Digite uma das opções: ")
    
    if exportar == '1':
        import json
        
        with open (f'relatorio{contador_registro}.json', 'w', encoding='utf-8') as arquivo:
            json.dump(relatorio_json, arquivo, ensure_ascii= False, indent=4)
        
        contador_registro = contador_registro + 1
        print("Relatório exportado em JSON!\n")
    
    return contador_registro
    
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
                
                # if resultados:
                #     print("\nConsulta retornou resultados.")
                # else:
                #     print("\nConsulta não retornou resultados.")
                
                # print("Comando executado com sucesso!\n")
                return resultados
            
            # print("Comando executado com sucesso!\n")
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
