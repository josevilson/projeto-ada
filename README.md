# 💸 Projeto Final | Sistema de Controle Financeiro

## Descrição

Este projeto é um sistema de controle financeiro que recebe movimentações financeiras e as armazena em um arquivo JSON chamado `financas.json`, localizado na pasta raiz. O sistema realiza operações de CRUD (Criar, Ler, Atualizar, Deletar) e possui funcionalidades adicionais para cálculo de rendimento e exportação de relatórios.

## Funcionalidades

- **Criar** novos registros com data, tipo de movimentação e valor.
  - Tipos de movimentação:
    - **Receita**: valor armazenado como número positivo.
    - **Despesa**: valor armazenado como número negativo.
    - **Investimento**: inclui cálculo de rendimento utilizando a fórmula dos juros compostos.
  
- **Ler** registros filtrando por data, tipo ou valor.

- **Atualizar** registros com possibilidade de modificar valor, tipo e atualizar a data.

- **Deletar** registros do sistema.

- Função `atualiza_rendimento` para atualizar os valores dos rendimentos com base em cálculos financeiros.

- Função `exportar_relatorio` para exportar o relatório financeiro em formato CSV ou JSON.

- Função de agrupamento para calcular o total de valores por critérios como mês ou tipo de movimentação.

## Estrutura de Pastas

```
├── src/
│   ├── agruparmes.py
│   ├── atualizar_registro.py
│   ├── atualizar_rendimento.py
│   ├── criar_registro.py
│   ├── deletar_registro.py
│   ├── exportar_relatorio.py
│   ├── ler_registros.py
│   ├── salvar_registros.py
├── utilitarios/
│   ├── calcular_tempo.py
│   ├── entrada_data.py
│   ├── validar_generic.py
│   ├── validar_int.py
├── financas.json
├── README.md
└── main.py
```

- **`agruparmes.py`**: Função para agrupar os registros por mês.
- **`atualizar_registro.py`**: Função para atualizar um registro existente.
- **`atualizar_rendimento.py`**: Função que atualiza os rendimentos dos investimentos.
- **`criar_registro.py`**: Função para criar novos registros no sistema.
- **`deletar_registro.py`**: Função para deletar registros existentes.
- **`exportar_relatorio.py`**: Função para exportar o relatório financeiro em CSV ou JSON.
- **`ler_registros.py`**: Função para ler os registros armazenados.
- **`salvar_registros.py`**: Função para salvar os registros no arquivo `financas.json`.

### Utilitários

Os arquivos dentro da pasta `utilitarios/` contêm funções auxiliares utilizadas pelo sistema:

- **`calcular_tempo.py`**: Funções para cálculo de tempo e datas.
- **`entrada_data.py`**: Funções para entrada e manipulação de datas.
- **`solicitar_input.py`**: Funções para solicitar e validar entradas do usuário.
- **`validar_generic.py`**: Funções genéricas de validação.
- **`validar_int.py`**: Funções para validar números inteiros.

## Requisitos

- **Bibliotecas nativas do Python**: Não foi utilizado o Pandas para este projeto, garantindo a simplicidade e o foco em manipulação de arquivos JSON e CSV usando apenas recursos básicos da linguagem.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git

2. Navegue até a pasta do projeto:

   ```bash
   cd nome_do_projeto

1. Execute o arquivo Python para iniciar o sistema de controle financeiro:
  ```bash
  python main.py
