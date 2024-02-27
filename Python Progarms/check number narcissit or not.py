a = 1534
s = 0

while a != 0:
    r = a%10
    s = s + (r*r*r*r)
    a = a // 10

if a == s:
    print("Armstrong", s)
else:
    print("Not Armstrong", s)
