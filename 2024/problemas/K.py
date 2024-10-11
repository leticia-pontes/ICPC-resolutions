def dividir_doces(sacolas):
    pass

n = int(input())
sacolas = list(map(int, input().split()))

resultado = dividir_doces(sacolas)

if resultado == -1:
    print(-1)
else:
    print(" ".join(map(str, resultado)))
