n1 = input("Enter your numbers :")
l = list(n1)
l1 = len(l)
n2 = {0: "zero", 1:"one", 2 : "two", 3: "three", 4: "four"}
i = 0;
while i<l1:
    print(n2[int(l[i])], end=" ")
    i = i+1

