s=int(input())
for i in range(s):
    n=input()
    x=n[::-1]
    if n==x and len(n)%2==0:
        print("YES EVEN")
    elif n==x and len(n)%2!=0:
        print("YES ODD")
    else:
        print("NO")