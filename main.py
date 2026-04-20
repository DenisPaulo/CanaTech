from funcoes import *
from oracle_db import conectar
import os

def menu():
    conn = conectar()
    if not conn:
        return
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*60)
        print("          CANATECH - GESTAO DE PERDAS NA COLHEITA")
        print("="*60)
        print("1. Cadastrar talhao")
        print("2. Listar talhoes")
        print("3. Alterar talhao")
        print("4. Excluir um talhao")
        print("5. Excluir TODOS os talhoes")
        print("6. Gerar relatorio TXT")
        print("7. Salvar em JSON")
        print("8. Sair")
        print("="*60)
        
        op = input("Escolha uma opcao: ")
        
        if op == "1":
            cadastrar_talhao(conn)
        elif op == "2":
            listar_talhoes()
        elif op == "3":
            alterar_talhao(conn)
        elif op == "4":
            excluir_talhao(conn)
        elif op == "5":
            excluir_todos(conn)
        elif op == "6":
            gerar_relatorio_txt()
        elif op == "7":
            salvar_json()
        elif op == "8":
            salvar_json()
            conn.close()
            print("Ate a proxima safra! Projeto entregue com sucesso!")
            break
        else:
            print("Opcao invalida!")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu()