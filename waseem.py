import random as rd

def view_random_recipe():
    """"Generate A Random Recipe from Available Recipes"""

    i = 1
    while i == 1:
        try:  
            index = rd.randint(len(recipes))
            print(f"\n=========== Here is a Random Recipe you can try ===============\n\n")
            print(recipes[index])
            i = (int(input("Enter '1' to generate another random recipe or '0' to exit: ")))
        except ValueError:
            if i > 1 or (i != 1 and i != 0): 
                i = int(input("Please Enter Correct Values (1 or 0): "))

def 
