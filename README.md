Coloca o texto abaixo em um arquivo markdown, README.md

# 📊 Extrator de Operações Financeiras (API para Excel)

Este projeto é um script Python com interface gráfica (GUI) desenvolvido para conectar-se a uma API financeira, buscar dados de operações e exportá-los para um arquivo Excel (.xlsx) com um layout de **113 colunas** e formatação específica, conforme o modelo exigido para processamento de base.

## 🌟 Funcionalidades Principais

* **Interface Gráfica (GUI):** Utiliza Tkinter para facilitar a seleção de empresa e parâmetros de data.
* **Segurança de Credenciais:** As chaves de acesso são lidas de um arquivo local (api_credentials.json), que é **ignorado pelo Git** (.gitignore).
* **Mapeamento e Formatação Exatos:**
    * Mapeamento de campos críticos: mci (da API) $\rightarrow$ **NR OPERAÇÃO** e conta (da API) $\rightarrow$ **CONTA**.
    * Formatação de valores monetários para o **padrão brasileiro** (ex: 1.234,56).
* **Layout Limpo:** A exportação final em Excel não contém bordas ou negrito no cabeçalho ou nas linhas de dados, atendendo aos requisitos de layout.

---

## 🛠️ Pré-requisitos e Instalação

Para rodar este script, você precisa ter o **Python 3** instalado e as seguintes bibliotecas:

* requests (para comunicação com a API)
* pandas (para manipulação de dados)
* openpyxl (para escrita no Excel com formatação)
* tkcalendar (para a interface gráfica de seleção de datas)

### Instalação das Bibliotecas

Abra seu terminal ou prompt de comando e execute:

```bash
pip install requests pandas openpyxl tkcalendar
```

---

## ⚙️ Configuração (Credenciais)

O projeto requer um arquivo de configuração JSON local para armazenar as credenciais de acesso à API.

**Atenção:** Este arquivo DEVE ser chamado `api_credentials.json` e **NÃO** deve ser enviado ao GitHub (ele está listado no `.gitignore`).

### 🧩 Exemplo de Estrutura do Arquivo `api_credentials.json`

```json
{
    "unimed": {
        "auth_url": "[URL_DE_AUTENTICACAO_UNIMED]",
        "data_url": "[URL_DE_DADOS_UNIMED]",
        "usuario": "[SEU_USUARIO]",
        "senha": "[SUA_SENHA]",
        "client_id": "[SEU_CLIENT_ID]"
    },
    "intermed": {
        "auth_url": "[URL_DE_AUTENTICACAO_INTERMED]",
        "data_url": "[URL_DE_DADOS_INTERMED]",
        "usuario": "[SEU_USUARIO]",
        "senha": "[SUA_SENHA]",
        "client_id": "[SEU_CLIENT_ID]"
    }
}
```

---

