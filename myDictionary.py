#myDict = {}
myDict = {"Indispensable":"Absolutely Necessary","Boisterous":"Scandalous",
          "Present":["Existing or occuring now","A gift"]}

addWords = True

while addWords == True:
    print("Would you like to add another word to you dictionary? (y/n)")
    answer = input().lower()
    if (answer == 'y'):
        print("What is the word?")
        word = input().lower()
        print("What is the definition of the word?")
        definition = input().lower()
        
        myDict[word] = definition
    elif (answer == 'n'):
        print("Your dictionary has been saved1")
        addWords = False
    else:
        print("Please enter 'y' or 'n'")

        
#print(myDict)
print("MY DICTIONARY:")
print()

for item in myDict:
    
    print("Word: " + item)
    definition = myDict[item]
    defineType = type(definition)
    
    if (defineType == str):
        print("Definition: " + myDict[item])
        
    elif(defineType == list):
        
        for x in definition:
            print("-" + X)
    
    print()
