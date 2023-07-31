def best_fit_allocation(blocos_memoria, tamanho_necessario):
    indice_alocado = -1
    tamanho_menor_adequado = float('inf')

    for i, tamanho_bloco in enumerate(blocos_memoria):
        if tamanho_bloco >= tamanho_necessario and tamanho_bloco < tamanho_menor_adequado:
            indice_alocado = i
            tamanho_menor_adequado = tamanho_bloco

    if indice_alocado != -1:
        blocos_memoria[indice_alocado] -= tamanho_necessario
        return indice_alocado
    else:
        return -1

def agendador_processos(lista_processos, tamanho_memoria, quantum):
    # Ordenar a lista de processos com base no tamanho de memória necessário
    lista_processos.sort(key=lambda x: x[1])  # x[1] representa o tamanho de memória necessário

    # Inicializar a lista de blocos de memória disponíveis
    blocos_memoria = [tamanho_memoria]

    # Lista para armazenar a ordem de execução dos processos
    ordem_execucao = []

    # Variáveis para cálculo do tempo total de execução e tempo médio de espera
    tempo_total_execucao = 0
    tempo_espera_total = 0
    num_processos_executados = 0

    # Executar os processos usando o escalonamento Round Robin
    while lista_processos:
        processo, tamanho_necessario, tempo_execucao = lista_processos.pop(0)  # Remove o primeiro processo da lista
        indice_alocado = best_fit_allocation(blocos_memoria, tamanho_necessario)

        if indice_alocado != -1:
            # Executar o processo
            tempo_executado = min(quantum, tempo_execucao)
            for _ in range(tempo_executado):
                processo()  # Chamada do processo
                ordem_execucao.append(processo.__name__)

            # Atualizar tempos e blocos de memória
            tempo_execucao -= tempo_executado
            tempo_total_execucao += tempo_executado
            blocos_memoria[indice_alocado] -= tamanho_necessario

            if tempo_execucao > 0:
                # Caso o processo ainda possua tempo de execução restante, adicioná-lo de volta à lista
                lista_processos.append((processo, tamanho_necessario, tempo_execucao))
                tempo_espera_total += (tempo_total_execucao - tempo_executado)
            else:
                tempo_espera_total += (tempo_total_execucao - min(quantum, tempo_execucao))

            num_processos_executados += 1

    tempo_medio_espera = tempo_espera_total / num_processos_executados if num_processos_executados > 0 else 0
    return ordem_execucao, tempo_total_execucao, tempo_medio_espera

# Função que representa o processo 1
def processo1():
    print("Executando processo 1")

# Função que representa o processo 2
def processo2():
    print("Executando processo 2")

# Função que representa o processo 3
def processo3():
    print("Executando processo 3")

# Exemplo de uso da função agendador_processos
if __name__ == "__main__":
    # Lista de processos [processo, tamanho_memoria, tempo_execucao]
    lista_processos = [
        (processo1, 30, 10),
        (processo2, 20, 8),
        (processo3, 40, 15)
    ]

    tamanho_memoria_total = 100
    quantum = 5

    # Chamada do agendador de processos
    ordem_execucao, tempo_total_execucao, tempo_medio_espera = agendador_processos(lista_processos, tamanho_memoria_total, quantum)

    # Exibindo a ordem de execução dos processos
    print("Ordem de execução dos processos:")
    for processo in ordem_execucao:
        print(processo)

    # Exibindo o tempo total de execução e o tempo médio de espera
    print("\nTempo total de execução:", tempo_total_execucao)
    print("Tempo médio de espera:", tempo_medio_espera)
