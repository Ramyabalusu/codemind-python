s=input()
count=0
for i in s:
    if i.isdigit():
       count=count+int(i) 
print(count)