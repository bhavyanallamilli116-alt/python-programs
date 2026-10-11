#check whether the given number is prime or not
'''n=int(input("enter a number"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print("prime")
else:
        print("not prime")'''




#print all the prime numbers
n = int(input("Enter number"))
for num in range(2, n + 1):
    count = 0
    for i in range(2, num):
     if (num % i == 0):
      count = count + 1
    if (count == 0):
     print(num, end=" ")
