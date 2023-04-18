num=int(input("enter a number"))
rem=0
l=len(str(num))
sum=0
n=num
while(num!=0):
  rem=num%10
  sum=sum+rem**l 
  num=num//10
if(sum==n):
    print("number is aarmstrong")
else:
    print("its not aarmstrong")


#  write the program for find the HCF of two numbers;