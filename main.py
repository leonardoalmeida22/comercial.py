empresa = {
    "nome": "AgroTech Solutions",
    "cnpj": "12.345.678/0001-90",
    "cidade": "São Paulo",
    "segmento": "Tecnologia para agricultura"
}

recursos = [
    "Sensores de umidade",
    "Sensores de temperatura",
    "Sistema de irrigação",
    "Cameras de monitoramento"
]

estoque = [
    ["Arroz", "Feijão", "Macarrão"],
    ["Leite", "Açúcar", "Café"],
    ["Óleo", "Sal", "Farinha"]
]


def mostrar_estoque():
    print("\n--- ESTOQUE ---")
    for i, prateleira in enumerate(estoque):
        print(f"Prateleira {i + 1}: {prateleira}")


def consultar_item():
    try:
        linha = input("Número da prateleira (1 a 3): ").strip()
        coluna = input("Posição do item (1 a 3): ").strip()

        if not linha or not coluna:
            print("Erro: os campos não podem ficar vazios.")
            return

        linha = int(linha) - 1
        coluna = int(coluna) - 1

        if 0 <= linha < 3 and 0 <= coluna < 3:
            print("Item:", estoque[linha][coluna])
        else:
            print("Erro: posição fora do limite.")

    except ValueError:
        print("Erro: digite apenas números inteiros.")


def menu():
    while True:
        print("\n=== MENU DO ESTOQUE ===")
        print("1 - Mostrar estoque")
        print("2 - Consultar item")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if not opcao:
            print("Erro: digite uma opção.")
        elif opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            consultar_item()
        elif opcao == "3":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


menu()
