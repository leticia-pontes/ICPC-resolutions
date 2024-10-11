N = int(input())
K = [list(map(int, input().split())) for _ in range(N)]

menor = float('inf')
indices = [0, 0]

for i in range(N):
    for j in range(N):
        if K[i][j] < menor:
            menor = K[i][j]
            indices = [i, j]

D = [
    [0, 0],
    [0, N - 1],
    [N - 1, N - 1],
    [N - 1, 0]
]

print(D.index(indices))
