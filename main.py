import csv
import random as rd
import uuid


# Hussain Darwish

def main():
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
            view_all_recipes()
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
def add_recipe():
    """use this function to add a new recipe to your recipes csv"""

    #try to open the recipe list. if it exists all is good, otherwise create a new one:
    try:
        with open('recipes.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
        print('\nFile Loaded Succesfuly!')
    except FileNotFoundError:
        with open('recipes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['recipe_id', 'name', 'ingredients','prep_time', 'cooking_instructions', 'difficulty', 'category'])
            print('\n Your Recipes File is Now Created! Enjoy Adding Your Tasty Recipes :)')

    print('\nWell, it is time to add your lovely recipe now!') #tell the user that they have loaded their file with a nice welcoming message
    recipe_id = str(uuid.uuid4()) # we here are creating a unique id for each recipe. this can help us in the future.
    name = input('What is the name of your recipe 👀?')

    ingredients = input('\nWhat ingredients would we need for this dish? 🥕 \n(separate them by commas)')
    valid_prep = True # creating the loop turn on condition
    
    while valid_prep:
        try:
            prep_time = int(input('\nand how many mins would this dish take to get ready ⏲️? \n numbers only plzzz...'))
            if type(prep_time) is int:
                valid_prep = False # ending the loop
        except ValueError:
            print('uhh.. i kindly asked for numbers here...')


    cooking_instructions = [] # Creating an empty list

    no_instructions = True #looping for each instruction condition
    print('\nIt is time for the instructions! let us start with the first step📎')
    while no_instructions:
        inst = input('\n Please enter the step here: ')
        cooking_instructions.append(inst)
        print('Step Added succesfuly')
        inst_done = input('\nPress "Enter" to add another step, write "Done" to confirm your instructions')
        if inst_done == 'Done':
            no_instructions = False #end loop when "Done" is inputted

    
    #No we will create a valid diffuclty case
    valid_difficulty = ['easy','medium','hard']
    while True:
        difficulty = input('\nWhat is the difficulty of this wonderful dish🫢 [Easy, Medium, Hard]\nChoose one of the options above!')
        if difficulty.lower() in valid_difficulty:
            break
        else:
            print('\nThat option does not exist! Please Try Again')

        #Now will create a category
    valid_category = ['breakfast','lunch','dinner', 'dessert']
    while True:
        category = input('\nWhat do you consider this meal to be?😋 [Breakfast, Lunch, Dinner, Dessert]\nChoose one of the options above!')
        if category.lower() in valid_category:
            break
        else:
            print('\nThat option does not exist! Please Try Again')

    #finally we will create the recipe

    new_recipe = {
        'recipe_id': recipe_id,
        'name': name,
        'ingredients': ingredients,
        'prep_time': prep_time,
        'cooking_instructions': cooking_instructions,
        'difficulty' : difficulty,
        'category': category
    }
    try:
        with open('recipes.csv', 'a', newline='') as file:
            fn = ['recipe_id', 'name', 'ingredients','prep_time', 'cooking_instructions', 'difficulty', 'category']
            writer = csv.DictWriter(file, fieldnames=fn)
            writer.writerow(new_recipe)
            print('\nYUM! THIS RECIPE SMELLS GOOD! 🍲\n*RECIPE ADDED SUCCESFULY*')   
    except Exception:
        print('\nUh.. Oh.. Someone Spilled The Pot!\n*ERROR ADDING YOUR RECIPE')
#Waseem

def view_random_recipe():
    """"Generate A Random Recipe from Available Recipes"""
    try:
        index = rd.randint(0, len(recipes) - 1)
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
    main()
