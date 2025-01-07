#functions are ways to wrap your code
#into reuseable units

#how to define a function
#i onlt define the function once
# whatever I pass inside the parentheses is called a parameter
# def sayHello(name,age,height):
#     print(f"say hello {name}")
#     print(f"Hello Governor")
#     print(f"welcome back")
#     print(f"your age is {age}")
#     print(f"you are {height} tall")

# # once you define a function
# # you must call or invoke the function
# # when i pass infomation throuh a funcion its called an arugument 
# sayHello("Armando",18,"6 ft")


# def determineEligibility(age):
#     #if your age is over 18,you can vote, otherwise you cant
#     if age >= 18:
#         print("you can vote")
#     else:
#         print("you cant vote")

# determineEligibility(13)
# determineEligibility(45)
# determineEligibility(16)

# def willYouGraduate(gpa,credits,sat):
#     #gpa: number variable
#     # credits: number variable
#     # passed sat: Boolean t or f
#     if (gpa>=3.0) and (credits >= 28) and (sat == True):
#         print("you passed. Good Luck in College")
#     elif (gpa<3.0) or (credits <28) or (sat != False):
#         print("back to the drawing board")
#     else:
#         print("talk to your counselor")
# willYouGraduate(2.8,15,True)
# willYouGraduate(4,29,True)
# willYouGraduate(3.0,14,False)


#return = statements used to end a function and send a result back to the caller
#return,  means stop in the function, it prints, than stops the program
#print, prints things, continue to use it
# def add(x,y):
#     z = x + y
#     return z
# def subtract(x,y):
#     z = x - y
#     return z 
# def mutliply(x,y):
#     z = x * y
#     return z 
# def divide(x,y):
#     z = x / y
#     return z
# print(add(1,2))
# print(subtract(1,2))
# print(mutliply(1,2))
# print(divide(1,2))

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " +last
full_name = create_name("spongebob", "squarepants")
print(full_name)


