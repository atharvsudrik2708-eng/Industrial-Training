#WAp to print this pattern.
#D D D D
#C C C
#B B
#A

ch = ord("D")
for i in range(1,5):
    for j in range(1,6-i):
        print(chr(ch),end = " ")
    ch-= 1
    print()    