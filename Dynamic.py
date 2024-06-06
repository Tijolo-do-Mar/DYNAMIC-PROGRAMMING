import numpy as np

# Definição das áreas marinhas com dados fictícios
areas_marinhas = [
    {'id': 1, 'biodiversidade': 8, 'vulnerabilidade': 7, 'conectividade': 5, 'custo': 10},
    {'id': 2, 'biodiversidade': 6, 'vulnerabilidade': 5, 'conectividade': 8, 'custo': 8},
    {'id': 3, 'biodiversidade': 7, 'vulnerabilidade': 6, 'conectividade': 6, 'custo': 7},
    {'id': 4, 'biodiversidade': 5, 'vulnerabilidade': 8, 'conectividade': 7, 'custo': 9},
    {'id': 5, 'biodiversidade': 9, 'vulnerabilidade': 6, 'conectividade': 4, 'custo': 11},
]

# Função para calcular o valor de uma área marinha
calcular_valor = lambda area: 0.4 * area['biodiversidade'] + 0.3 * area['vulnerabilidade'] + 0.3 * area['conectividade']

# Função para otimizar a alocação de recursos usando programação dinâmica
def otimizar_alocacao(areas, recursos_totais):
    n = len(areas)
    dp = np.zeros((n+1, recursos_totais+1))
    
    for i in range(1, n+1):
        area = areas[i-1]
        custo = area['custo']
        valor = calcular_valor(area)
        
        for j in range(recursos_totais+1):
            if custo <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-custo] + valor)
            else:
                dp[i][j] = dp[i-1][j]
    
    # Identificação das áreas selecionadas
    recursos_restantes = recursos_totais
    areas_selecionadas = []
    
    for i in range(n, 0, -1):
        if dp[i][recursos_restantes] != dp[i-1][recursos_restantes]:
            areas_selecionadas.append(areas[i-1])
            recursos_restantes -= areas[i-1]['custo']
    
    return dp[n][recursos_totais], areas_selecionadas

# Exemplo de uso com dados fictícios
recursos_totais = 20
valor_otimo, areas_selecionadas = otimizar_alocacao(areas_marinhas, recursos_totais)

print(f'Valor ótimo de conservação: {valor_otimo}')
print('Áreas marinhas selecionadas:')
for area in areas_selecionadas:
    print(f'ID: {area["id"]}, Valor: {calcular_valor(area)}, Custo: {area["custo"]}')

