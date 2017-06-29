groceryList = []

keepShopping = True
while keepShopping == True:
    print ("Do you want to add an item to your list?(y/n)")
    answer = input()
    if answer == "y" or answer =="Yes" or answer =="yes":
        print ("What would you like to add to your list?")
        item = input()
        groceryList.append(item)
    elif answer == "n" or answer =="No" or answer =="no":
        print ("Okay! Your grocery list is:")
        for x in groceryList:
            print (x)
        keepShopping = False
