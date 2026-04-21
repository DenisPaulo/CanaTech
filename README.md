# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP" border="0" width="40%" height="40%"></a>
</p>

<br>

# 📌 CanaTech - Sistema de Gestão Inteligente de Perdas na Colheita de Cana-de-Açúcar

## 👨‍🎓 Integrantes
- [Jeliel Cardoso](https://www.linkedin.com/in/jelielcardoso/)
- [Denis Paulo Dias da Silva](https://www.linkedin.com/in/denispaulodiassilva/)
- [Deweyne Reuel](https://www.linkedin.com/in/deweyne-reuel-0695522a8/)
- [Matheus Nascimento](https://www.linkedin.com/in/mathnascimento/)

## 👩‍🏫 Professores
### Tutor(a)
- [Sabrina Otoni](https://www.linkedin.com/in/sabrina-otoni-22525519b/)
### Coordenador(a)
- [André Godoi](https://www.linkedin.com/in/andregodoichiovato/)

---

## 📖 Descrição

O **CanaTech** é uma **agrotech** desenvolvida para resolver um dos maiores problemas do agronegócio brasileiro: as altas perdas na colheita mecanizada de cana-de-açúcar, que chegam a **15% da produção** (contra apenas 5% na colheita manual), gerando prejuízos milionários anuais.

O sistema permite o cadastro, monitoramento, alteração e exclusão de talhões, calcula automaticamente o percentual de perda e o prejuízo financeiro em tempo real, gera relatórios claros e persiste todos os dados de forma segura em JSON e no banco Oracle.

**Problema do Agronegócio tratado:**  
Perdas elevadas durante a colheita de cana-de-açúcar (fonte: SOCICANA e textos da atividade).  

**Diferenciais da solução:**
- Cálculo automático de perda percentual e prejuízo financeiro
- CRUD completo integrado com Oracle
- Persistência em arquivos texto e JSON (requisito Cap. 5)
- Tabela em memória + subalgoritmos com passagem de parâmetros
- Validação rigorosa de entradas e usabilidade limpa no terminal
- Totalmente alinhado aos Capítulos 3 ao 6 da disciplina

O resultado é uma ferramenta prática que ajuda o produtor a tomar decisões mais assertivas, reduzir desperdícios e aumentar a eficiência da operação.

---

## 🚀 Funcionalidades

- Cadastro de talhões com cálculo automático de perda e prejuízo
- Listagem completa dos talhões cadastrados
- Alteração de dados de talhões existentes
- Exclusão de um talhão específico
- Exclusão de todos os talhões (com confirmação)
- Geração de relatório legível em arquivo TXT
- Salvamento dos dados em formato JSON
- Conexão segura com banco de dados Oracle
- Validação de entradas para evitar erros

---

## 🧠 Conceitos Utilizados (Capítulos 3 ao 6)

- **Cap 3** → Subalgoritmos (funções e procedimentos com passagem de parâmetros)
- **Cap 4** → Listas, dicionários e tabela em memória (lista de dicionários)
- **Cap 5** → Manipulação de arquivos texto e JSON
- **Cap 6** → Conexão com Oracle + CRUD completo + tratamento de erros

---

## 🧠 Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Banco de Dados**: Oracle (oracledb)
- **Persistência**: Arquivos TXT e JSON
- **Estruturas de Dados**: Lista de dicionários (tabela em memória)
- **Validação**: Funções com try/except e loops de validação
- **Documentação**: Markdown + GitHub

---

## 📁 Estrutura de Pastas

```bash
CanaTech/
├── main.py
├── funcoes.py
├── oracle_db.py
├── dados/
│   ├── talhoes.json
│   └── relatorio_perdas.txt
├── README.md
└── requirements.txt


##⚙️ Como Executar o Projeto

Pré-requisitos

Oracle Database XE instalado e rodando
Oracle SQL Developer
Python 3.8+ instalado
Driver Oracle: pip install oracledb

Execução

Clone o repositório ou entre na pasta do projeto
Configure seu usuário e senha do Oracle no arquivo oracle_db.py
Execute o comando:Bashpython main.py


##🧪 Exemplos de Uso

Cenário 1 (Cadastro normal):
Talhão: Talhao Norte
Área: 45.5 ha
Esperado: 5200 ton
Colhido: 4800 ton
→ Perda: 7.69% | Prejuízo: R$ 60.000,00
Cenário 2 (Perda alta):
Talhão: Talhao Sul
Esperado: 6000 ton
Colhido: 5100 ton
→ Perda: 15% (alerta máximo)

##🗃 Histórico de Versões

1.0.0 – 20/04/2026

Entrega completa da Fase 2
CRUD completo com Oracle
Manipulação de TXT e JSON
Subalgoritmos, tabela em memória e validações
README profissional


## 🎯 Melhorias Futuras

Exportação de relatório para Excel
Interface gráfica com Tkinter ou Streamlit
Gráficos de perdas por talhão (matplotlib)
Relatório comparativo entre talhões
Integração com API de preço da cana em tempo real
Dashboard web para múltiplos usuários


## 📄 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">
MODELO GIT FIAP por Fiap está licenciado sobre Attribution 4.0 International.
CanaTech – Fase 2: Gestão do Agronegócio em Python
Tecnólogo em Inteligência Artificial – FIAP