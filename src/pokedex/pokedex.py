# Instruções de execução:
# Este programa gerencia uma Pokédex utilizando Python 3.9+.
# Para executar, configure o projeto com Poetry:
#   1. Instale o Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
#   2. No diretório do projeto, execute: `poetry install`
#   3. Execute o programa com: `poetry run pokedex`
# Não são necessárias dependências externas além do Python 3.9+.

# Lista de tipos válidos para Pokémon
TIPOS_VALIDOS = [
    "Normal", "Fogo", "Água", "Elétrico", "Grama", "Gelo", "Lutador", "Veneno",
    "Terra", "Voador", "Psíquico", "Inseto", "Pedra", "Fantasma", "Dragão",
    "Sombrio", "Aço", "Fada"
]

def adicionar_pokemon(pokedex, nome, tipo, nivel):
    """Adiciona um Pokémon ao dicionário da Pokédex."""
    if not (1 <= nivel <= 100):
        print("Erro: O nível deve estar entre 1 e 100.")
        return
    if tipo not in TIPOS_VALIDOS:
        print(f"Erro: Tipo inválido. Tipos aceitáveis: {', '.join(TIPOS_VALIDOS)}")
        return
    pokedex[nome] = {"tipo": tipo, "nivel": nivel}
    print(f"Pokémon {nome} adicionado com sucesso!")

def listar_pokemon(pokedex):
    """Lista todos os Pokémon em ordem alfabética."""
    if not pokedex:
        print("Nenhum Pokémon cadastrado.")
        return
    print("\nLista de Pokémon:")
    for nome in sorted(pokedex.keys()):
        print(f"{nome} - {pokedex[nome]['tipo']} - Nível {pokedex[nome]['nivel']}")

def remover_pokemon(pokedex, nome):
    """Remove um Pokémon da Pokédex."""
    if nome in pokedex:
        del pokedex[nome]
        print(f"Pokémon {nome} removido com sucesso!")
    else:
        print(f"Erro: Pokémon {nome} não encontrado.")

def atualizar_nivel(pokedex, nome, nivel):
    """Atualiza o nível de um Pokémon existente."""
    if nome in pokedex:
        if not (1 <= nivel <= 100):
            print("Erro: O nível deve estar entre 1 e 100.")
            return
        pokedex[nome]["nivel"] = nivel
        print(f"Nível de {nome} atualizado para {nivel}!")
    else:
        print(f"Erro: Pokémon {nome} não encontrado.")

def registrar_captura(historico, pokedex, nome, quantidade):
    """Registra uma captura de Pokémon no histórico."""
    if nome in pokedex:
        historico.append({"nome": nome, "quantidade": quantidade})
        print(f"Captura de {quantidade} {nome}(s) registrada com sucesso!")
    else:
        print(f"Erro: Pokémon {nome} não encontrado na Pokédex.")

def exibir_historico(historico):
    """Exibe o histórico de capturas."""
    if not historico:
        print("Nenhum registro de captura encontrado.")
        return
    print("\nHistórico de Capturas:")
    for entrada in historico:
        print(f"{entrada['nome']} - {entrada['quantidade']} vez(es) capturado(s)")

def main():
    """Função principal que gerencia o menu e a interação com o usuário."""
    pokedex = {}  # Dicionário para armazenar Pokémon
    historico = []  # Lista para armazenar histórico de capturas

    while True:
        print("\n=== Pokédex ===")
        print("1. Adicionar Pokémon")
        print("2. Listar Pokémon")
        print("3. Remover Pokémon")
        print("4. Atualizar nível do Pokémon")
        print("5. Registrar captura")
        print("6. Exibir histórico de capturas")
        print("7. Sair")
        
        opcao = input("Escolha uma opção (1-7): ")
        
        if opcao == "1":
            nome = input("Digite o nome do Pokémon: ").capitalize()
            tipo = input("Digite o tipo do Pokémon: ").capitalize()
            try:
                nivel = int(input("Digite o nível do Pokémon (1-100): "))
                adicionar_pokemon(pokedex, nome, tipo, nivel)
            except ValueError:
                print("Erro: O nível deve ser um número inteiro.")
        
        elif opcao == "2":
            listar_pokemon(pokedex)
        
        elif opcao == "3":
            nome = input("Digite o nome do Pokémon a ser removido: ").capitalize()
            remover_pokemon(pokedex, nome)
        
        elif opcao == "4":
            nome = input("Digite o nome do Pokémon: ").capitalize()
            try:
                nivel = int(input("Digite o novo nível (1-100): "))
                atualizar_nivel(pokedex, nome, nivel)
            except ValueError:
                print("Erro: O nível deve ser um número inteiro.")
        
        elif opcao == "5":
            nome = input("Digite o nome do Pokémon capturado: ").capitalize()
            try:
                quantidade = int(input("Digite a quantidade de capturas: "))
                if quantidade <= 0:
                    print("Erro: A quantidade deve ser maior que zero.")
                else:
                    registrar_captura(historico, pokedex, nome, quantidade)
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro.")
        
        elif opcao == "6":
            exibir_historico(historico)
        
        elif opcao == "7":
            print("Saindo da Pokédex. Até logo!")
            break
        
        else:
            print("Opção inválida. Escolha um número entre 1 e 7.")

if __name__ == "__main__":
    main()