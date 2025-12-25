n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a Prime number")
            break
    else:
        print(n, "is a Prime number")
else:
    print(n, "is not a Prime number")
