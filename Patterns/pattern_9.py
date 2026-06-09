#WAp to print this pattern.
#A
#b C
#d E f
#G h I j

ch = ord("A")
for i in range(1,5):
    for j in range(1,i+1):
        
        if ch % 2 == 0:
            print(chr(ch).lower(),end= " ")
            ch += 1
        else:
            print(chr(ch),end = " ")
            ch += 1
    print()    