n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
s=0
for i in range(1,n-1):
    for j in range(1,m-1):
        s+=mat[i][j]
print(s)