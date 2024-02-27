n = input("n : ")
num = int(n)

factor = []

for i in range(1, num + 1):
    if num % i == 0 :
        factor.append(i)
print(factor)

# o/p :- n : 6
#        [1, 2, 3, 6]