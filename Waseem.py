import random as rd

def view_random_recipe():
    """"Generate A Random Recipe from Available Recipes"""
    try:
        index = rd.randint(len(recipes))
        i = 1
        while i == 1:  
            print(f"\n=========== Here is a Random Recipe you can try ===============\n\n")
            print(recipes[index])
            i = (int(input("Enter '1' to generate another random recipe or '0' to exit ")))
    
    except:
        print("Please Retry again")
        break
