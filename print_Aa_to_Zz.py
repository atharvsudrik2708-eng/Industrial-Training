ch = ord("A")
ch1 = ord("a")

while(ch <= ord("Z")) and (ch1 <= ord("z")):
    print(chr(ch)+chr(ch1),end =" ")
    ch += 1
    ch1 += 1