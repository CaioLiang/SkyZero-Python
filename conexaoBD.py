import cx_Oracle, json, os

def le_senha():
    caminho = os.path.join(os.path.dirname(__file__), "credenciais.json")
    with open(caminho, 'r') as arquivo:
        info = json.load(arquivo)
        login = info["login"]
        senha = info["senha"]
    return login, senha

def conecta_banco():
    login, senha = le_senha()
    dsn = cx_Oracle.makedsn(
        host='oracle.fiap.com.br',
        port=1521,
        sid='ORCL')
    conn = cx_Oracle.connect(
        user=login,
        password=senha,
        dsn=dsn)
    return conn