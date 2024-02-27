a = input("a : ")
b = input("b : ")
c = input("c : ")

if a>b and a>c:
    print("a is grater. ", a)
elif b>a and b>c:
    print("b is greater. ", b)
elif c>a and c>b:
    print("c is greater. ", c)
else:
    print("Invalid no.")
    
# o/p : 
    #   a : 1
    #   b : 3 
    #   c : 2
    #   b is greater. 3