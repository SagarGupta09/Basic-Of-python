# x = int(input("Enter any Number:"))
# if(x % 2 == 0):
#     print("%d is even",x)
# else:
#     print("given number is odd")

numbers = (1,2,3,4,5,6,7,9)
count_even = 0
count_odd = 0
for i in numbers:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(count_even)
print(count_odd)
