# Pokédex

Um programa em Python para gerenciar uma Pokédex, permitindo adicionar, listar, remover, atualizar e registrar capturas de Pokémon, além de exibir um histórico de capturas.

## Funcionalidades

- **Adicionar Pokémon**: Insere um Pokémon com nome, tipo e nível (1-100).
- **Listar Pokémon**: Exibe todos os Pokémon cadastrados em ordem alfabética.
- **Remover Pokémon**: Remove um Pokémon pelo nome.
- **Atualizar nível**: Atualiza o nível de um Pokémon existente.
- **Registrar captura**: Registra a quantidade de capturas de um Pokémon.
- **Exibir histórico**: Mostra o histórico de capturas.
- **Sair**: Encerra o programa.

## Pré-requisitos

- Python 3.9 ou superior
- Poetry (para gerenciamento de dependências)

## Instalação

1. Instale o Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. Clone ou crie o projeto e navegue até o diretório:
   ```bash
   cd pokedex
   ```
3. Instale as dependências:
   ```bash
   poetry install
   ```

## Execução

Execute o programa com:

```bash
poetry run pokedex
```

## Estrutura do Projeto

```
pokedex/
├── src/
│   ├── pokedex/
│   │   ├── __init__.py
│   │   └── pokedex.py
├── tests/
│   ├── __init__.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou adicionar testes no diretório `tests/`.

## Licença

MIT
