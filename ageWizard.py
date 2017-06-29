

print("I am the age wizard. What is your name?")
name = input()

print (" What is your age?")
age2 = input()

#print(type(age))

age2 = int(age2)

if age2 >= 100:
    print("Wow you old as hell")
elif age2 > 12 and age2 < 20:
    print ("you are a teenager")
else:
    print("Under a 100 years old? Quite the younin'")

print("I'm going to tell you something about uou...")
print("Your name is %s and your age is %d." %(name, age2))
