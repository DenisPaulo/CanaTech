import json
from datetime import datetime

talhoes_memoria = []

def validar_float(msg):
    while True:
        try:
            valor = float(input(msg))
            if valor < 0:
                print("Valor nao pode ser negativo!")
                continue
            return valor
        except ValueError:
            print("Digite apenas numeros!")

def cadastrar_talhao(conn):
    print("\n--- Cadastro de Talhao ---")
    talhao = input("Nome do talhao: ")
    area = validar_float("Area (ha): ")
    esperado = validar_float("Producao esperada (ton): ")
    colhido = validar_float("Producao colhida (ton): ")
    
    perda_pct = round(((esperado - colhido) / esperado * 100) if esperado > 0 else 0, 2)
    prejuizo = round((esperado - colhido) * 150, 2)
    
    registro = {
        "talhao": talhao,
        "area_ha": area,
        "esperado_t": esperado,
        "colhido_t": colhido,
        "perda_pct": perda_pct,
        "prejuizo_rs": prejuizo,
        "data": datetime.now().strftime("%d/%m/%Y")
    }
    
    talhoes_memoria.append(registro)
    
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO TALHOES (talhao, area_ha, esperado_t, colhido_t, perda_pct, prejuizo_rs)
        VALUES (:1, :2, :3, :4, :5, :6)
    """, (talhao, area, esperado, colhido, perda_pct, prejuizo))
    conn.commit()
    print("Talhao cadastrado com sucesso!")

def listar_talhoes():
    print("\n--- Lista de Talhoes ---")
    if not talhoes_memoria:
        print("Nenhum talhao cadastrado ainda.")
        return
    for i, t in enumerate(talhoes_memoria, 1):
        print(f"{i}. {t['talhao']} | Area: {t['area_ha']}ha | Perda: {t['perda_pct']}% | Prejuizo: R$ {t['prejuizo_rs']}")

def alterar_talhao(conn):
    listar_talhoes()
    if not talhoes_memoria:
        return
    try:
        idx = int(input("\nDigite o numero do talhao para alterar: ")) - 1
        if idx < 0 or idx >= len(talhoes_memoria):
            print("Numero invalido!")
            return
        talhao = talhoes_memoria[idx]
        print(f"\nAlterando: {talhao['talhao']}")
        
        novo_nome = input(f"Novo nome ({talhao['talhao']}): ")
        if novo_nome:
            talhao["talhao"] = novo_nome
        talhao["area_ha"] = validar_float(f"Nova area ({talhao['area_ha']}): ") or talhao["area_ha"]
        talhao["esperado_t"] = validar_float(f"Nova esperada ({talhao['esperado_t']}): ") or talhao["esperado_t"]
        talhao["colhido_t"] = validar_float(f"Nova colhida ({talhao['colhido_t']}): ") or talhao["colhido_t"]
        
        talhao["perda_pct"] = round(((talhao["esperado_t"] - talhao["colhido_t"]) / talhao["esperado_t"] * 100) if talhao["esperado_t"] > 0 else 0, 2)
        talhao["prejuizo_rs"] = round((talhao["esperado_t"] - talhao["colhido_t"]) * 150, 2)
        
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE TALHOES 
            SET talhao=:1, area_ha=:2, esperado_t=:3, colhido_t=:4, perda_pct=:5, prejuizo_rs=:6
            WHERE id = (SELECT id FROM TALHOES WHERE ROWNUM = 1 OFFSET :7 ROWS)
        """, (talhao["talhao"], talhao["area_ha"], talhao["esperado_t"], talhao["colhido_t"], talhao["perda_pct"], talhao["prejuizo_rs"], idx))
        conn.commit()
        print("Talhao alterado com sucesso!")
    except Exception as e:
        print(f"Erro ao alterar: {e}")

def excluir_talhao(conn):
    listar_talhoes()
    if not talhoes_memoria:
        return
    try:
        idx = int(input("\nDigite o numero do talhao para excluir: ")) - 1
        if idx < 0 or idx >= len(talhoes_memoria):
            print("Numero invalido!")
            return
        talhao = talhoes_memoria.pop(idx)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TALHOES WHERE ROWNUM = 1 OFFSET :1 ROWS", (idx,))
        conn.commit()
        print("Talhao excluido com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir: {e}")

def excluir_todos(conn):
    if not talhoes_memoria:
        print("Nada para excluir.")
        return
    conf = input("Tem certeza que deseja excluir TODOS os talhoes? (S/N): ").upper()
    if conf != "S":
        return
    talhoes_memoria.clear()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TALHOES")
    conn.commit()
    print("Todos os talhoes foram excluidos!")

def gerar_relatorio_txt():
    with open("dados/relatorio_perdas.txt", "w", encoding="utf-8") as f:
        f.write("=== RELATORIO DE PERDAS - CANATECH ===\n\n")
        f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        for t in talhoes_memoria:
            f.write(f"Talhao: {t['talhao']}\n")
            f.write(f"Area: {t['area_ha']} ha | Esperado: {t['esperado_t']} ton | Colhido: {t['colhido_t']} ton\n")
            f.write(f"Perda: {t['perda_pct']}% | Prejuizo: R$ {t['prejuizo_rs']}\n")
            f.write("-" * 50 + "\n")
    print("Relatorio TXT gerado!")

def salvar_json():
    with open("dados/talhoes.json", "w", encoding="utf-8") as f:
        json.dump(talhoes_memoria, f, ensure_ascii=False, indent=4)
    print("Dados salvos em JSON!")
