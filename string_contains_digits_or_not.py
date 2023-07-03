n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in s:
        if i.isdigit():
           c+=1
        else:
            c+=0
    if c>=1:
        print("Yes")
    else:
        print("No")
