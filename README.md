
---

# MySQL Date Range Exporter

![Versão](https://img.shields.io/badge/version-1.0.0-blue)
![Licença](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange?logo=mysql&logoColor=white)

Uma ferramenta de linha de comando (CLI) desenvolvida em Python para extrair dados de um banco MySQL com base em um intervalo de datas e exportá-los para um arquivo CSV. Ideal para gerar relatórios, backups ou análises de dados históricos de forma automatizada.

## ✨ Principais Funcionalidades

- **Exportação por Intervalo de Datas**: Filtre registros de uma tabela específica entre duas datas fornecidas pelo usuário.
- **Geração Automática de CSV**: Cria um arquivo `.csv` nomeado dinamicamente com base no intervalo de datas (ex: `relatorio_de_2023-01-01_ate_2023-12-31.csv`).
- **Interface de Comando Simples**: Interaja com o script de forma intuitiva através do terminal.
- **Cabeçalhos Inclusos**: O arquivo CSV gerado inclui os cabeçalhos das colunas, pronto para ser importado em ferramentas como Excel, Google Sheets ou Power BI.
- **Fácil de Configurar**: Requer apenas a edição das credenciais do banco de dados e da consulta SQL diretamente no script.

## 🚀 Começando

Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes requisitos instalados e configurados:

- **Python 3.x** (recomendado: versão 3.8 ou superior).
- **Biblioteca `mysql-connector-python`**. Instale-a usando o pip:
  ```bash
  pip install mysql-connector-python
  ```
- **Servidor MySQL** em execução (localmente via XAMPP, Docker, MySQL Workbench, ou em um servidor remoto).
- **Credenciais de acesso** ao banco de dados (host, usuário, senha e nome do banco).

### 2. Instalação

Clone este repositório para sua máquina local usando o seguinte comando:

```bash
git clone https://github.com/seu-usuario/MySQL-Date-Range-Exporter.git
cd MySQL-Date-Range-Exporter
```

### 3. Configuração do Script

Antes de executar, você precisa personalizar o script `exporter.py` com suas informações:

1.  **Credenciais do Banco de Dados**: Abra o arquivo e localize o bloco de conexão. Insira suas credenciais:
    ```python
    # Exemplo de configuração no script
    config = {
        'host': 'localhost',    
        'user': 'root',
        'password': 'sua_senha',
        'database': 'seu_banco_de_dados'
    }
    ```

2.  **Consulta SQL**: Ajuste a query para corresponder à sua tabela e às colunas que deseja exportar. **Importante**: Certifique-se de que a coluna de data (`sua_coluna_de_data`) seja do tipo `DATE` ou `DATETIME`.
    ```python
    # Exemplo de consulta no script
    query = """
    SELECT id, nome_produto, valor, data_venda
    FROM sua_tabela
    WHERE sua_coluna_de_data BETWEEN %s AND %s
    ORDER BY sua_coluna_de_data;
    """
    ```

## 💻 Como Usar

Com o ambiente configurado, execute o projeto da seguinte forma:

1.  Abra um terminal na pasta raiz do projeto.
2.  Execute o script com o comando:
    ```bash
    python exporter.py
    ```
    *(Use `python3` se for o padrão em seu sistema)*

3.  O script solicitará a **data de início**. Digite-a no formato `DD-MM-AAAA` (ex: `01-01-2023`).
4.  Em seguida, insira a **data de fim** no mesmo formato.
5.  Aguarde a execução. O script se conectará ao banco, executará a consulta e gerará o arquivo CSV no mesmo diretório.

Ao final, uma mensagem de sucesso será exibida, informando o nome do arquivo e o número de registros exportados.

### 🎬 Demonstração

A imagem abaixo ilustra o fluxo de execução no terminal:


```
$ python exporter.py
Digite a primeira data (DD-MM-YYYY): 16-10-2025
Digite a segunda data (DD-MM-YYYY): 28-10-2025

✓ Arquivo 'relatorio_2025-10-16_ate_2025-10-28.csv' gerado com sucesso!
✓ Total de registros: 25
```

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para:

1.  Abrir uma **Issue** para discutir uma nova funcionalidade ou relatar um bug.
2.  Enviar um **Pull Request** com suas melhorias.

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---
