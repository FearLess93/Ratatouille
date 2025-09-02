import csv
import random as rd
import uuid


# Hussain Darwish

def main(i):
    """Main application function."""
    print("Welcome to Ratatouille!")
    print("This app helps you to create a digital recipe book that allows users to store, retrieve, and manage your favorite recipes in a .csv file.")

    while True:
        choice = display_menu()
        if choice == 1:
            add_recipe()
        elif choice == 2:
            recipes_by_ingredients()
        elif choice == 3:
            view_all_recipes(i)
        elif choice == 4:
            view_random_recipe()
        elif choice == 5:
            rate_recipe()
        elif choice == 6:
            print("Thank you for using Ratatouille. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def display_menu():
    """Display the main menu options."""
    print("\n=== Ratatouille ===")
    print("1. Add a new recipe to the collection")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. View a random recipe suggestion ")
    print("5. Exit")
    return int(input("Enter your choice (1-5): "))
#Zahra

recipes = [{'name':'cookies','prep_time':'25'},{'name':'cake','prep_time':'55'}]

def view_all_recipes(i):
    '''View all recipies in the database.'''
    if len(recipes) > 0:
        for i in recipes:
            print(f"Recipe Name: {i['name']} \nPreperation Time: {i['prep_time']} minutes \n\n")
    else:
        print('No Recipes Found')

view_all_recipes(recipes)

#Maryam

def recipes_by_ingredients():
    ingredients = input('Which ingredient would you like to search for?  ').lower()
    found = False 
    try:
        with open('recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if ingredients in row['Ingredients'].lower():
                    print(f"\n {row['Name']}")
                    print(f"Ingredients: {row['Ingredients']}")
                    print(f"Instructions: {row['Instructions']}\n")
                    print(f"Preperation Time: {row['PrepTime']}")
                    found = True 
                if not found:
                    print(f" No recipes found with '{ingredients}' ")
                    break 
    except:
        print("No ingredient found! Try again.")
        return
#Sayed Hussain

#Waseem

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

def rate_recipe():
    recipes = ()
    with open('recipes.csv', "r") as file:
        recipes = list(csv.DictReader(file))
        if not recipes:
            print("No recipes to rate")
            return
        recipe_name = input("Enter the recipe name to rate: ").lower()
        found = False
        for recipe in recipes:
            if recipe['Name'].lower() == recipe_name:
                rating = input("Enter your rating (1-5): ")
                if rating <= 1 and rating >=5:
                    print(f" Rating updated for recipe to {rating}")
                else:
                    print("Invalid rating")
                found = True
                break
            if not found:
                print(f"Recipe {'recipe_name'} not found")

if __name__ == "__main__":
    main(recipes)
