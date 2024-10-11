N = int(input())
K = int(input())

D = (K - (N - 1)) // N if N != 1 else K // N

print(D)
