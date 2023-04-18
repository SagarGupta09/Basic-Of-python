n1 = input("Enter your numbers: ")
l = list(n1)
l1 = len(l)
n2 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
i = 0
while i < l1:
    print(n2[int(l[i])])
    i = i + 1

