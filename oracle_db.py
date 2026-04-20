import oracledb

def conectar():
    try:
        # <<< MUDE AQUI seu usuário e senha do Oracle >>>
        conn = oracledb.connect(user='rm573278', password="050589", dsn='oracle.fiap.com.br:1521/ORCL')
        print("Conectado ao Oracle com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao Oracle: {e}")
        return None