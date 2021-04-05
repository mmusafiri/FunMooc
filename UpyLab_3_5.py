a = abs(int(input()))
b = abs(int(input()))

if b >= a:
    denum = a
    num = b
else:
    denum = b
    num = a

if num%denum != 0:
    print("True")
else:
    print("False")