despesas = {
    'lazer': {},
    'contas': {},
    'alimentacao': {},
    'outros': {}
}

def pergunta_usuario():
    tipo_custo = input('Que tipo de despesa você quer add? \n'
    '[l]azer,[c]ontas,[a]limentacao ou [o]utros: ')
    nome_custo = input('Qual nome da despesa? ')
    custo_atividade = input('Qual valor da atividade? ')
    custo_atividade = int(custo_atividade)
    return tipo_custo, nome_custo, custo_atividade

def adicionar_despesa(tipo, nome, valor):
    print(f"Tipo: {tipo}, Nome: {nome}, Valor: {valor}")  # Verificar se estamos recebendo os valores corretos
    if tipo == 'l':
        print("Adicionando ao lazer...")
        despesas['lazer'][nome] = valor
    elif tipo == 'c':
        print("Adicionando às contas...")
        despesas['contas'][nome] = valor
    elif tipo == 'a':
        print("Adicionando à alimentação...")
        despesas['alimentacao'][nome] = valor
    elif tipo == 'o':
        print("Adicionando aos outros...")
        despesas['outros'][nome] = valor
    else:
        print("Tipo de despesa inválido. Tente novamente.")
        return

rodar_programa2 = True
while rodar_programa2:
    tipo_atividade, nome_atividade, custo_atividade = pergunta_usuario()
    adicionar_despesa(tipo_atividade, nome_atividade, custo_atividade)

    rodar_programa2 = input('Deseja continuar? [s] [n] ').lower()
    if rodar_programa2 == 'n':
        rodar_programa2 = False

print(despesas)
