n, m = map(int, input().split())
mat = []
for i in range(n):
    l = list(map(int, input().split()))
    mat.append(l)
sum = 0
for i in range(n):
    for j in range(m):
        if i == j or i + j == n - 1:
            sum += mat[i][j]

print(sum)
