myCon = {"Emergency": "911"}

#number = int


addInfo = True

while addInfo == True:
    print("Would you like to add a contact? (y/n)")
    answer = input().lower()
    if (answer == 'y'):
        print("What is your Contact Name?")
        name = input().lower()
        print("Do you want to add a phone number?(y/n)")
        answer = input().lower()
        if (answer == 'y'):
            print("What is the phone number?")
            number = input().lower()
            myCon[name] = number
        print("Alright. Would you like to add an address? (y/n)")
        answer = input().lower()
        if (answer == "y"):
            print("What is the address?")
            address = input().lower()
        elif (answer == 'n'):
            print ("OKAY...")
            

