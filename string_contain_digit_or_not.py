s=input()
count=0
for i in s:
    if i.isdigit():
        count+=1
if count>=1:
   x="Contains {} digit"
   print(x.format(count))
else:
   print("Doesn't contain digit")
      
