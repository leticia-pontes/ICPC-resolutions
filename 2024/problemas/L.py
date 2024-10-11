N = int(input())
A = [int(a) for a in input().split()]

A_ordenado = sorted(A, reverse=True)
binarios_ordenados = [format(a, 'b') for a in A_ordenado]

binarios_invertidos = [b[::-1] for b in binarios_ordenados]
tamanho_maximo = len(binarios_invertidos[0])

binarios_preenchidos = [b.ljust(tamanho_maximo, '0') for b in binarios_invertidos]
binarios_para_trocar = binarios_preenchidos[::-1]

for indice_bit in range(tamanho_maximo):
    if binarios_preenchidos[0][indice_bit] == '0':
        for indice_num, numero in enumerate(binarios_para_trocar):
            if numero[indice_bit] == '1':
                # Troca o bit 0 pelo bit 1 no primeiro binário
                binarios_preenchidos[0] = binarios_preenchidos[0][:indice_bit] + '1' + binarios_preenchidos[0][indice_bit + 1:]
                # Troca o bit 1 pelo bit 0 no binário correspondente
                binarios_para_trocar[indice_num] = binarios_para_trocar[indice_num][:indice_bit] + '0' + binarios_para_trocar[indice_num][indice_bit + 1:]
                # Atualiza o binário original
                binarios_preenchidos[-1 - indice_num] = binarios_para_trocar[indice_num][::-1]
                break

resultado = ' '.join([str(int(numero, 2)) for numero in binarios_preenchidos])
print(resultado)
