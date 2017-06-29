print("Welcome to The Carnival!")
print("BIG RIDES ARE 7 TICKETS (bumper cars, carousel)")
print("SMALL RIDES ARE 3 TICKETS (slide, train ride)")
print("You have 15 tickets to spend.")
 
choosingRide = True
 
tickets = 15
 

 
while choosingRide == True:
    
    print("Which rides would you like go on?")
    rideChoice = input()
   
        

    if(rideChoice == "bumper cars"):
        print("Good Choice! Have a crashing time!!")
        tickets = tickets - 7
        print("You have %d left." %(tickets))
        if (tickets < 3):
            print ("You don't have enough tickets for another ride! Goodbye!")
        print("Would you like to ride another ride?")
        answer = input()
        if answer != "yes":
            print("GOOD-BYE")
            choosingRide = False
 
    elif(rideChoice == "carousel"):
        print("Great Choice! Don't fall!")
        tickets = tickets - 7
        print("You have %d left." %(tickets))
        if (tickets < 3):
            print ("You don't have enough tickets for another ride! Goodbye!")
        print("Would you like to ride another ride?")
        answer = input()
        if answer != "yes":
            print("GOOD-BYE")
            choosingRide = False
 
 
    elif(rideChoice == "slide" or "train"):
        print("Have Fun!")
        tickets = tickets - 3
         if (tickets < 3):
            print ("You don't have enough tickets for another ride! Goodbye!")
            exit()
        print("You have %d left." %(tickets))
          print("Would you like to ride another ride?")
        answer = input()
        if answer != "yes":
            print("GOOD-BYE")
            choosingRide = False

    else:
        print("Sorry that is not an Option, pick again."
