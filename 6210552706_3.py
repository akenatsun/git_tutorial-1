n = int(input("Number: "))
n1 = 0
n2 = 1
count = 0

if n <= 0:
        print("error")
elif n == 1:
        print("fibonacci upto",n,":")
        print(n1)
else:
        print(" ")
        while count < n:
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1
