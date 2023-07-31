class Processo:
    def __init__(self, id, tempo_execucao, prioridade):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade

def escalona_prioridade_preemptiva(processos):
    tempo_total_execucao = 0
    tempo_espera_total = 0
    numero_processos = len(processos)
    processos_restantes = processos.copy()

    while processos_restantes:
        proximo_processo = None

        # Encontra o processo de maior prioridade entre os processos restantes
        for processo in processos_restantes:
            if proximo_processo is None or processo.prioridade < proximo_processo.prioridade:
                proximo_processo = processo

        # Remove o processo selecionado da lista de processos restantes
        processos_restantes.remove(proximo_processo)

        # Executa o processo por 1 unidade de tempo
        tempo_total_execucao += 1
        proximo_processo.tempo_execucao -= 1

        # Verifica se o processo ainda possui tempo de execução restante
        if proximo_processo.tempo_execucao > 0:
            # Caso possua, coloca o processo de volta na lista de processos restantes
            processos_restantes.append(proximo_processo)
        else:
            # Caso contrário, o processo já terminou sua execução, então seu tempo de espera é 0
            tempo_espera_processo = tempo_total_execucao - proximo_processo.prioridade
            tempo_espera_total += tempo_espera_processo

    tempo_medio_espera = tempo_espera_total / numero_processos
    return tempo_total_execucao, tempo_medio_espera


# Teste com outros processos
if __name__ == "__main__":
    # Lista de processos no formato (id, tempo_execucao, prioridade)
    processos = [
        Processo(1, 4, 2),
        Processo(2, 7, 1),
        Processo(3, 5, 2),
        Processo(4, 3, 3),
    ]

    # Chamada da função de escalonamento
    tempo_total, tempo_medio_espera = escalona_prioridade_preemptiva(processos)

    print(f"\nTempo total de execução: {tempo_total}")
    print(f"Tempo médio de espera: {tempo_medio_espera:.2f} unidades de tempo")
