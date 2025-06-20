"""Módulo simples para controle de despesas por categoria."""

from typing import Dict


CATEGORY_MAP = {
    "l": "lazer",
    "c": "contas",
    "a": "alimentacao",
    "o": "outros",
}

# Estrutura para armazenar as despesas de cada categoria
despesas: Dict[str, Dict[str, float]] = {
    categoria: {} for categoria in CATEGORY_MAP.values()
}

def pergunta_usuario() -> tuple[str, str, float]:
    """Pergunta ao usuário os dados da despesa e retorna-os."""

    while True:
        tipo_custo = input(
            "Que tipo de despesa você quer add?\n[l]azer,[c]ontas,[a]limentacao ou [o]utros: "
        ).lower()
        if tipo_custo in CATEGORY_MAP:
            break
        print("Tipo de despesa inválido. Tente novamente.")

    nome_custo = input("Qual nome da despesa? ")

    while True:
        custo_str = input("Qual valor da atividade? ")
        try:
            custo_valor = float(custo_str)
            break
        except ValueError:
            print("Valor inválido. Digite um número.")

    return tipo_custo, nome_custo, custo_valor

def adicionar_despesa(tipo: str, nome: str, valor: float) -> None:
    """Registra uma nova despesa na categoria informada."""

    categoria = CATEGORY_MAP.get(tipo)
    if categoria is None:
        print("Tipo de despesa inválido. Tente novamente.")
        return

    despesas[categoria][nome] = valor

def exibir_despesas() -> None:
    """Exibe todas as despesas cadastradas."""

    for categoria, itens in despesas.items():
        print(f"\n{categoria.capitalize()}:")
        for nome, valor in itens.items():
            print(f"  {nome}: R$ {valor:.2f}")


def main() -> None:
    """Laço principal do programa."""

    continuar = True
    while continuar:
        tipo, nome, valor = pergunta_usuario()
        adicionar_despesa(tipo, nome, valor)
        continuar = input("Deseja continuar? [s/n] ").lower() == "s"

    print("\nDespesas registradas:")
    exibir_despesas()


if __name__ == "__main__":
    main()
