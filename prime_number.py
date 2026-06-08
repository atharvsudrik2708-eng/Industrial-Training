num = int(input('enter number'))

for i in range (2,n):
    if(num%i==0):
        print ('not prime number')
        break
else:
    print('prime number')    