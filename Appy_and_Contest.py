t = int(input())
for i in range(t):
    n,a,b,k=map(int, input().split())
    if (n // a) + (n // b) - 2 * (n // (a * b)) >= k:
        print("Win")
    else:
        print("Lose")
