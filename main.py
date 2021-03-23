sentence = ("TODAY IS CLOUDY")
print(sentence.lower())

sen2 = ("Have a great spring break")
print(sen2.upper())

sen3 = ("I like python")
print(len(sen3))

str1 = ("I am learning how to code in python")
check ="learning" in str1
print(check)


#how to format the given string
#putting variable inside {}
place = input("What is your favourite place to visit? ")
print(f"Hello, your favourite place is {place}")
#using .format and give variable (multiple variables used)
name = input("What is your name?")
age = input('How old are you? ')
print("Hello, {0}you are {1} Yeas old !".format(name,age))
#Old version. "Words" + variable + "Words"
animal = input ("What is your favourite animal?")
print("Hello, your favourite animal is a " + animal + "!")