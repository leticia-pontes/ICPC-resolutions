def transformar_binarios(seq_binaria):
    possibilidades = []

    def backtrack(indice, atual):
        if indice == len(seq_binaria):
            possibilidades.append(int("".join(atual), 2))
            return

        if seq_binaria[indice] == '*':
            for bit in ['0', '1']:
                atual[indice] = bit
                backtrack(indice + 1, atual)
        else:
            atual[indice] = seq_binaria[indice]
            backtrack(indice + 1, atual)
    
    backtrack(0, [''] * len(seq_binaria))
    return possibilidades

M = list(input().strip())
N = list(input().strip())

msg = transformar_binarios(M)
seq = transformar_binarios(N)

for i in msg:
    for s in seq:
        if s != 0 and i % s == 0:
            print(format(i, 'b'))
            exit()
