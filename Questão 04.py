def best_fit_allocation(blocos_memoria, tamanho_necessario):
    indice_alocado = -1
    
    for i, tamanho_bloco in enumerate(blocos_memoria):
        if tamanho_bloco >= tamanho_necessario:
            if indice_alocado == -1 or tamanho_bloco < blocos_memoria[indice_alocado]:
                indice_alocado = i
    
    if indice_alocado != -1:
        blocos_memoria[indice_alocado] -= tamanho_necessario
        return indice_alocado
    else:
        return -1

# Exemplo de uso da função
if __name__ == "__main__":
    # Lista de blocos de memória disponíveis (tamanhos em bytes)
    blocos_memoria = [100, 50, 200, 80, 150]
    
    # Tamanho do bloco necessário (em bytes)
    tamanho_necessario = 70
    
    # Chamada da função de alocação
    indice_alocado = best_fit_allocation(blocos_memoria, tamanho_necessario)
    
    if indice_alocado != -1:
        print(f"Bloco {indice_alocado} alocado para a memória.")
    else:
        print("Nenhum bloco adequado encontrado para alocar a memória.")
