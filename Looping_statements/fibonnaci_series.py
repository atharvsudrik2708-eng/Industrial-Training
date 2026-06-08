num = int(input('enter number'))

n1 =0
n2 = 1

for i in range (n1,num,n1+n2):
    print (n1)
    n3 = n1+ n2
    n1 = n2 
    n2 = n3
    