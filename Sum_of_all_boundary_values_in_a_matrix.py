n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
s=0
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==n-1:
            s+=mat[i][j]
print(s)