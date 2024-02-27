a = int(input("a : "))
b = 0

while a != 0:
    r = a % 10
    rev = b * 10 + r
    a = a // 10
    print(rev, end="")
    
    # o/p:- a : 153
    #       351