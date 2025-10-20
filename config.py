# config.py

# =================================================================
# 🔒 DADOS DE CREDENCIAIS DE API (Substitui api_credentials.json)
# =================================================================
# ATENÇÃO: Preencha os valores [SEUS_DADOS] abaixo com suas credenciais reais

API_SECRETS = {
    "unimed": {
        "auth_url": "https://api.unimedteresina.com.br/usuarios/auth/login",
        "data_url": "https://api.unimedteresina.com.br/financeiro/executiva/vencimento",
        "usuario": "01976180000104",
        "senha": "Unimed@99",
        "client_id": "f6acf37c"
    },
    "intermed": {
        "auth_url": "https://api.intermed-pi.com.br/usuarios/auth/login",
        "data_url": "https://api.intermed-pi.com.br/financeiro/executiva/vencimento",
        "usuario": "01976180000104",
        "senha": "Unimed@99",
        "client_id": "f6acf37c"
    }
}


# =================================================================
# 📋 MAPEAMENTO E LAYOUT DE COLUNAS (Substitui db_config/outros arquivos de config)
# =================================================================

MAP_COLUMNS = {
    'tipo': 'TIPO',
    'nome_operacao': 'NOME OPERAÇÃO',
    'dt_atualizacao': 'DT. ATUALIZADO',
    'vencimento': 'DT. VENCIMENTO',
    'vl_venda': 'VALOR OPERAÇÃO',
    'vl_vencido': 'VALOR VENCIDO',
    'cpf_cnpj': 'CPF / CNPJ',
    'nome': 'NOME DO CLIENTE',
    'endereco': 'ENDEREÇO',
    'bairro': 'BAIRRO',
    'cep': 'CEP',
    'cidade': 'CIDADE',
    'uf': 'UF',
    'telefone1': 'TELEFONE 1',
    'telefone2': 'TELEFONE 2',
    'telefone3': 'TELEFONE 3',
    'telefone4': 'TELEFONE 4',
    'telefone5': 'TELEFONE 5',
    'telefone6': 'TELEFONE 6',
    'data_nascimento': 'DATA NASCIMENTO',
    'naturalidade': 'NATURALIDADE',
    'sexo': 'SEXO',
    'estado_civil': 'ESTADO CIVIL',
    'pai': 'NOME DO PAI',
    'mae': 'NOME DA MÃE',
    'email': 'E-MAIL',
    'data_emissao': 'DT. EMISSÃO',
    'benefs_contrato': 'OBS. OPERAÇÃO',
    'mci': 'NR OPERAÇÃO',
    'nr_ficha': 'CONTA'
}

TARGET_COLUMNS = [
    'TIPO', 'NR OPERAÇÃO', 'NOME OPERAÇÃO', 'AGENCIA', 'CONTA', 'PRODUTO', 'DT. ATUALIZADO',
    'DT. VENCIMENTO', 'VALOR OPERAÇÃO', 'VALOR VENCIDO', 'COND. NEGOCIAIS', 'CPF / CNPJ',
    'MCI', 'NR FICHA', 'NOME DO CLIENTE', 'ENDEREÇO', 'BAIRRO', 'CEP', 'CIDADE', 'UF',
    'TELEFONE 1', 'TELEFONE 2', 'TELEFONE 3', 'TELEFONE 4', 'TELEFONE 5', 'TELEFONE 6',
    'DATA NASCIMENTO', 'NATURALIDADE', 'SEXO', 'ESTADO CIVIL', 'NOME DO PAI', 'NOME DA MÃE',
    'NOME AVALISTA 1', 'CPF/CNPJ AVALISTA 1', 'ENDEREÇO AVALISTA 1', 'BAIRRO AVALISTA 1',
    'CEP AVALISTA 1', 'CIDADE AVALISTA 1', 'UF AVALISTA 1', 'TELEFONE 1 AVALISTA 1',
    'TELEFONE 2 AVALISTA 1', 'NOME AVALISTA 2', 'CPF/CNPJ AVALISTA 2', 'ENDEREÇO AVALISTA 2',
    'BAIRRO AVALISTA 2', 'CEP AVALISTA 2', 'CIDADE AVALISTA 2', 'UF AVALISTA 2',
    'TELEFONE 1 AVALISTA 2', 'TELEFONE 2 AVALISTA 2', 'NOME AVALISTA 3', 'CPF/CNPJ AVALISTA 3',
    'ENDEREÇO AVALISTA 3', 'BAIRRO AVALISTA 3', 'CEP AVALISTA 3', 'CIDADE AVALISTA 3',
    'UF AVALISTA 3', 'TELEFONE 1 AVALISTA 3', 'TELEFONE 2 AVALISTA 3', 'NOME AVALISTA 4',
    'CPF/CNPJ AVALISTA 4', 'ENDEREÇO AVALISTA 4', 'BAIRRO AVALISTA 4', 'CEP AVALISTA 4',
    'CIDADE AVALISTA 4', 'UF AVALISTA 4', 'TELEFONE 1 AVALISTA 4', 'TELEFONE 2 AVALISTA 4',
    'NOME AVALISTA 5', 'CPF/CNPJ AVALISTA 5', 'ENDEREÇO AVALISTA 5', 'BAIRRO AVALISTA 5',
    'CEP AVALISTA 5', 'CIDADE AVALISTA 5', 'UF AVALISTA 5', 'TELEFONE 1 AVALISTA 5',
    'TELEFONE 2 AVALISTA 5',
    'NOME AVALISTA 6', 'CPF/CNPJ AVALISTA 6', 'ENDEREÇO AVALISTA 6', 'BAIRRO AVALISTA 6',
    'CEP AVALISTA 6', 'CIDADE AVALISTA 6', 'UF AVALISTA 6', 'TELEFONE 1 AVALISTA 6',
    'TELEFONE 2 AVALISTA 6',
    'PROFISSÃO', 'NOME LOCAL DE TRABALHO', 'ENDEREÇO LOCAL DE TRABALHO', 'BAIRRO LOCAL DE TRABALHO',
    'CEP LOCAL DE TRABALHO', 'CIDADE LOCAL DE TRABALHO', 'UF LOCAL DE TRABALHO',
    'TELEFONE 1 LOCAL DE TRABALHO', 'TELEFONE 2 LOCAL DE TRABALHO',
    'REFERENCIA PESSOAL', 'TELEFONE 1 REFERENCIA', 'TELEFONE 2 REFERENCIA',
    'REFERENCIA PESSOAL 2', 'TELEFONE 1 REFERENCIA 2', 'TELEFONE 2 REFERENCIA 2',
    'REFERENCIA PESSOAL 3', 'TELEFONE 1 REFERENCIA 3', 'TELEFONE 2 REFERENCIA 3',
    'SPC/SERASA', 'E-MAIL', 'DT. EMISSÃO', 'VALOR PROTESTO', 'OBS. OPERAÇÃO',
    'DT. FIMTERCERIZAÇÃO', 'VALOR JUROS', 'COD_CLASSIFICACAO_CLIENTE', 'COD_CLASSIFICACAO_OPERACAO'
]

EMPRESAS = {
    "2003 - Unimed": "unimed",
    "2004 - Intermed": "intermed"
}