s=input()
count=1
for i in range(1,len(s)):
    if s[i].isupper():
        count+=1
print(count)