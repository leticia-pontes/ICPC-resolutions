D, C, R = map(int, input().split())
c = [int(input()) for _ in range(C)]
r = [int(input()) for _ in range(R)]

total = 0
ic, ir = 0, 0

# enquanto houver atividades
while ic < C or ir < R:
    # se ainda houver atividades cansativas e disposição
    if ic < C and D >= c[ic]:
        D -= c[ic]
        ic += 1
        total += 1
    # se tiver atividades revigorantes
    elif ir < R:
        D += r[ir]
        ir += 1
        total += 1
    # não pode mais fazer atividade
    else:
        break

print(total)
    