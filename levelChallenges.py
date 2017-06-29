from random import randint

#Functions##############

def level2(numlist):
    numSum = 0

    for num in numlist:
        if num % 3 == 0 or num % 5 == 0:
            print(num)
            numSum += num
    print("Final sum:")
    print (numSum)
def level3(numlist):
    primeSum = 0
    for num in numlist:
        prime = True
        for x in range (2,num):
            if num % x == 0:
                prime = False
        if prime == True:
            primeSum += num
    print (primeSum)


#Code
randomlist=[]
for x in range (100):
    randnumber = randint(10,99)
    randomlist.append(randnumber)

level2(randomlist)
