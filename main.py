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
            view_recipes_sorted_by_rating()
        elif choice == 7:
            print("Thank you for using Ratatouille. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def display_menu():
    """Display the main menu options."""
    print("\n=== Ratatouille ===")
    print("1. Add a new recipe to the collection")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. View a random recipe suggestion")
    print("5. Rate a recipe")
    print("6. View recipes sorted by rating")
    print("7. Exit")
    return int(input("Enter your choice (1-7): "))
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
            writer.writerow(['recipe_id', 'name', 'ingredients','prep_time', 'cooking_instructions', 'difficulty', 'category','rating'])
            print('\n Your Recipes File is Now Created! Enjoy Adding Your Tasty Recipes :)')

    print('\nWell, it is time to add your lovely recipe now!') #tell the user that they have loaded their file with a nice welcoming message
    recipe_id = str(uuid.uuid4()) # we here are creating a unique id for each recipe. this can help us in the future.
    name = input('What is the name of your recipe 👀?')

    ingredients = input('\nWhat ingredients would we need for this dish? 🥕 \n(separate them by commas)')
    valid_prep = True # creating the loop turn on condition
    
    while valid_prep:
        try:
            prep_time = int(input('\nand how many mins would this dish take to get ready ⏲️? \n numbers only please...'))
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
    rating = ''
    new_recipe = {
        'recipe_id': recipe_id,
        'name': name,
        'ingredients': ingredients,
        'prep_time': prep_time,
        'cooking_instructions': cooking_instructions,
        'difficulty' : difficulty,
        'category': category,
        'rating': rating
    }
    try:
        with open('recipes.csv', 'a', newline='') as file:
            fn = ['recipe_id', 'name', 'ingredients','prep_time', 'cooking_instructions', 'difficulty', 'category', 'rating']
            writer = csv.DictWriter(file, fieldnames=fn)
            writer.writerow(new_recipe)
            print('\nYUM! THIS RECIPE SMELLS GOOD! 🍲\n*RECIPE ADDED SUCCESFULY*')   
    except Exception:
        print('\nUh.. Oh.. Someone Spilled The Pot!\n*ERROR ADDING YOUR RECIPE')
#Waseem

def view_random_recipe():
    """"Generate A Random Recipe from Available Recipes"""
    i = 1
    while i == 1:
        try:
            index = rd.randint(0, len(recipes) - 1)
            print(f"\n=========== Here is a Random Recipe you can try ===============\n\n")
            print(recipes[index])
            i = (int(input("Enter '1' to generate another random recipe or '0' to exit: ")))
        except ValueError:
            if i > 1 or (i != 1 and i != 0):
                i = int(input("Please Enter Correct Values (1 or 0): "))

def rate_recipe():
    """Rate an existing recipe and update the CSV file."""
    try:
        # Read existing recipes from the same file that add_recipe uses
        with open('recipes.csv', "r") as file:
            recipes = list(csv.DictReader(file))
            
        if not recipes:
            print("No recipes to rate")
            return
            
        # Display available recipes for user to choose from
        print("\nAvailable recipes to rate:")
        for i, recipe in enumerate(recipes, 1):
            current_rating = recipe['rating'] if recipe['rating'] else 'Not rated'
            print(f"{i}. {recipe['name']} (Current rating: {current_rating})")
        
        recipe_name = input("\nEnter the recipe name to rate: ").lower()
        found = False
        
        for i, recipe in enumerate(recipes):
            if recipe['name'].lower() == recipe_name:
                found = True
                while True:
                    try:
                        rating = input("Enter your rating (1-5): ")
                        if rating in ["1", "2", "3", "4", "5"]:
                            recipes[i]["rating"] = rating
                            
                            # Write the updated recipes back to the CSV file
                            with open('recipes.csv', 'w', newline='') as file:
                                fieldnames = ['recipe_id', 'name', 'ingredients', 'prep_time', 'cooking_instructions', 'difficulty', 'category', 'rating']
                                writer = csv.DictWriter(file, fieldnames=fieldnames)
                                writer.writeheader()
                                writer.writerows(recipes)
                            
                            print(f"Rating for '{recipe['name']}' has been updated to {rating} stars!")
                            return
                        else:
                            print("Invalid rating. Please enter a number between 1 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 5.")
        
        if not found:
            print(f"Recipe '{recipe_name}' not found. Please check the spelling and try again.")
            
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_recipes_sorted_by_rating():
    """View all recipes sorted by their rating."""
    try:
        with open('recipes.csv', "r") as file:
            recipes = list(csv.DictReader(file))
            
        if not recipes:
            print("No recipes found")
            return
            
        # Convert ratings to integers for sorting, treating empty/invalid ratings as 0
        for recipe in recipes:
            try:
                recipe["rating"] = int(recipe["rating"]) if recipe["rating"] else 0
            except ValueError:
                recipe["rating"] = 0
        
        # Sort recipes by rating in descending order
        recipes.sort(key=lambda x: x["rating"], reverse=True)
        
        print("\n=== Recipes Sorted by Rating ===")
        for recipe in recipes:
            rating_display = f"{recipe['rating']} stars" if recipe['rating'] > 0 else "Not rated"
            print(f"{recipe['name']} - {rating_display}")
            
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
