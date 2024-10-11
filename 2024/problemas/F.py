N = int(input())

fibonacci = [1, 1]

for i in range(2, N):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print(fibonacci[N - 1])
