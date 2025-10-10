# 📊 Extrator de Operações Financeiras (API para Excel)

Este projeto é um script Python com interface gráfica (GUI) desenvolvido para conectar-se a uma API financeira, buscar dados de operações e exportá-los para um arquivo Excel (`.xlsx`) com um **layout de 113 colunas** e formatação específica, conforme o modelo exigido para processamento de base.

## 🌟 Funcionalidades Principais

* **Interface Gráfica Simples:** Utiliza Tkinter para facilitar a seleção de empresa e parâmetros de data.
* **Autenticação Segura:** Faz a autenticação na API usando credenciais armazenadas em um arquivo JSON local (`api_credentials.json`).
* **Filtro Flexível:** Permite definir a faixa de datas de vencimento (com sugestão automática de 120 dias atrás) e o parâmetro **Baixa Pdd (0/1)**.
* **Mapeamento de Colunas Personalizado:** Implementa a lógica exata de mapeamento:
    * `mci` (da API) $\rightarrow$ **NR OPERAÇÃO**
    * `nr_ficha` (da API) $\rightarrow$ **CONTA**
    * Colunas **MCI** e **NR FICHA** são preenchidas com valor vazio (`''`).
* **Formatação Monetária Brasileira:** Formata os campos de valores (`VALOR OPERAÇÃO`, `VALOR VENCIDO`) para o padrão decimal brasileiro (ex: `1.234,56`).
* **Layout de Exportação Limpo:** O arquivo Excel gerado segue o modelo de três linhas de cabeçalho de controle, com remoção total de bordas e negrito das células, garantindo um layout "limpo".

---

## 🛠️ Pré-requisitos

Para rodar este script, você precisa ter o **Python 3** instalado e as seguintes bibliotecas:

* `tkinter` e `tkcalendar` (para a interface gráfica)
* `requests` (para comunicação com a API)
* `pandas` (para manipulação e estruturação de dados)
* `openpyxl` (para formatação avançada do Excel)

### Instalação das Bibliotecas

Abra seu terminal ou prompt de comando e execute:

```bash
pip install requests pandas openpyxl tkcalendar