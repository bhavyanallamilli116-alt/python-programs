#write a program to print first 10 natural numbers

n=int(input("enter the number"))
i=0
for i in range(n):
    if(i%2==0):
       print(i)
    i+=1
