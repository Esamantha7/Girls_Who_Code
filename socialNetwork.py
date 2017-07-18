

#GLOBAL VARIABLES

users ={'ESamantha7': ['Samantha Enriquex', 'ESamantha7@gmail.com']}


#FUNCTIONS

def userNameCheck(username):
    if(len(users) == 0):
        return True

    for each in users:
        if username == each:
            return False
    return True

#CLASSES

class User:
    def __init__(self,name,email,userName):
        self.name = name
        self.email = email
        self.userName = userName

        userData = [name,email]
        users[userName] = userData

        self.buddies = []

    def addBuddy(self, buddyUsername):
        buddies = buddyUsername.split()

        for each in buddies:
            self.buddies.append(each)

    def removeBuddy(self, buddyUsername):
        self.buddies.remove(buddyUsername)

    def buddyList(self):
        buddyList = self.buddies
        buddyList.sort()
        print("You have"+ str(len(buddyList))+"buddies")
        print("Here's your list of buddies!")
        for each in buddyList:
            print(each)
        print()


##class Network:
##    def __init__(self):
##        self.users = users


    
#RUNNING CODE


print("Welcone to the New Social Network!")
print("Please enter your full name")
enteredName = input()

print("Please enter your email address")
enteredEmail = input()

print("Please enter your desired username.")
print ("(Please do not have spaces in your usernamme)")

chooseUsername = True

while (chooseUsername):
    enteredUsername  = input()

    result = userNameCheck(enteredUsername)
    if result == True:
        chooseUsername = False
        user1 = User(enteredName,enteredEmail,enteredUsername)
    else:
        print("Sorry, this username has already been taken.")
        print("Please choose another one.")

edit = True
while (edit):
    
    print("Add some buddies!")
    buddies = input()
    user1.addBuddy(buddies)
    user1.buddyList() 

    print("Remove a buddy!")
    buddy = input()
    user1.removeBuddy(buddy)
    user1.buddyList()

print(users)
