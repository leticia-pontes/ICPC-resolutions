N, S = map(int, input().split())

# Lista de trabalhos: (l, r, c)
trabalhos = []
for n in range(N):
    l, r, c = map(int, input().split())
    trabalhos.append((l, r, c))

# Ordenar os trabalhos pelo dia de término (r)
trabalhos.sort(key=lambda x: x[1])

# Tabela para armazenar o lucro máximo até o final de cada trabalho
lucro_max = [0] * N

# Inicializar o lucro máximo com o lucro líquido do primeiro trabalho
lucro_max[0] = max(0, (trabalhos[0][1] - trabalhos[0][0] + 1) * S - trabalhos[0][2])

for i in range(1, N):
    l, r, c = trabalhos[i]
    lucro_liquido = (r - l + 1) * S - c

    # O lucro se fizermos apenas o trabalho atual
    lucro_atual = max(0, lucro_liquido)

    # Encontrar o trabalho anterior que não sobrepõe
    for j in range(i - 1, -1, -1):
        if trabalhos[j][1] < l - 1:  # Esse trabalho termina antes de começar o atual
            lucro_atual = max(lucro_atual, lucro_max[j] + lucro_liquido)
            break

    # Atualizar o lucro máximo até o trabalho i
    lucro_max[i] = max(lucro_max[i - 1], lucro_atual)

# O lucro máximo ao final de todos os trabalhos será o último valor em lucro_max
print(lucro_max[-1])
