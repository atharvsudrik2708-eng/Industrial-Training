#WAp to print this pattern.
#A
#B C
#D E F
#G H I J

ch = ord("A")
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(ch),end = " ")
        ch+= 1
    print()    