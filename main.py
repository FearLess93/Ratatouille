import csv
import uuid
import datetime
import random as rd


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
            cook()
        elif choice == 8:
            nostalgic_recipes()
        elif choice == 9:
            scaling_ingredients()
        elif choice == 10:
            shopping_list()
        elif choice == 11:
            print("Thank you for using Ratatouille. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

def display_menu():
    """Display the main menu options."""
    print("\n=== Ratatouille ===")
    print("1. Add a new recipe to the collection")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. View a random recipe suggestion")
    print("5. Rate a recipe")
    print("6. View recipes sorted by rating")
    print("7. Cook a recipe")
    print("8. View recipes that you didn't cook in a while")
    print("9. Scale ingredients for a recipe")
    print("10. Create a shopping list")
    print("11. Exit")
    return int(input("Enter your choice (1-11): "))

def view_all_recipes():
    """View all recipes in the database from the CSV file."""
    try:
        with open('recipes.csv', 'r') as file:
            recipes = list(csv.DictReader(file))
            
        if not recipes:
            print("No recipes found in the database.")
            return
            
        print("\n=== All Recipes ===")
        for i, recipe in enumerate(recipes, 1):
            print(f"\n{i}. Recipe Name: {recipe['name']}")
            print(f"   Ingredients: {recipe['ingredients']}")
            print(f"   Preparation Time: {recipe['prep_time']} minutes")
            print(f"   Difficulty: {recipe['difficulty']}")
            print(f"   Category: {recipe['category']}")
            print(f"   Instructions: {recipe['cooking_instructions']}")
            rating = recipe['rating'] if recipe['rating'] else 'Not rated'
            print(f"   Rating: {rating}")
            last_cooked = recipe['last_cooked'] if recipe['last_cooked'] else 'Not cooked yet'
            print(f"   Last Cooked: {last_cooked}")
            print("-" * 50)
            
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except Exception as e:
        print(f"An error occurred while reading recipes: {e}")

def recipes_by_ingredients():
    ingredients = input('Which ingredient would you like to search for?  ').lower()
    found = False 
    try:
        with open('recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if ingredients in row['ingredients'].lower():
                    print(f"\n {row['name']}")
                    print(f"Ingredients: {row['ingredients']}")
                    print(f"Instructions: {row['cooking_instructions']}\n")
                    print(f"Preperation Time: {row['prep_time']}")
                    found = True
            if not found:
                print(f" No recipes found with '{ingredients}' ")
    except:
        print("No ingredient found! Try again.")
        return

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
            writer.writerow(['recipe_id', 'name', 'ingredients','prep_time', 'cooking_instructions', 'difficulty', 'category','rating','last_cooked'])
            print('\n Your Recipes File is Now Created! Enjoy Adding Your Tasty Recipes :)')

    print('\nWell, it is time to add your lovely recipe now!') #tell the user that they have loaded their file with a nice welcoming message
    recipe_id = str(uuid.uuid4()) # we here are creating a unique id for each recipe. this can help us in the future.
    name = input('What is the name of your recipe 👀? ')

    ingredients = input('\nWhat ingredients would we need for this dish? 🥕 \n(separate them by commas. Eg: milk 40ml, coffee 30g, .. etc) ')
    valid_prep = True # creating the loop turn on condition
    
    while valid_prep:
        try:
            prep_time = int(input('\nand how many mins would this dish take to get ready ⏲️? \n numbers only please: '))
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
        inst_done = input('\nPress "Enter" to add another step, write "Done" to confirm your instructions: ')
        if inst_done.lower() == 'done':
            no_instructions = False #end loop when "done" is inputted

    
    #Now we will create a valid diffuclty case
    valid_difficulty = ['easy','medium','hard']
    while True:
        difficulty = input('\nWhat is the difficulty of this wonderful dish🫢 [Easy, Medium, Hard]\nChoose one of the options above!: ')
        if difficulty.lower() in valid_difficulty:
            break
        else:
            print('\nThat option does not exist! Please Try Again')

        #Now will create a category
    valid_category = ['breakfast','lunch','dinner', 'dessert']
    while True:
        category = input('\nWhat do you consider this meal to be?😋 [Breakfast, Lunch, Dinner, Dessert]\nChoose one of the options above!: ')
        if category.lower() in valid_category:
            break
        else:
            print('\nThat option does not exist! Please Try Again')

    #finally we will create the recipe
    rating = None
    last_cooked = None
    new_recipe = {
        'recipe_id': recipe_id,
        'name': name,
        'ingredients': ingredients,
        'prep_time': prep_time,
        'cooking_instructions': cooking_instructions,
        'difficulty' : difficulty,
        'category': category,
        'rating': rating,
        'last_cooked': last_cooked
    }
    try:
        with open('recipes.csv', 'a', newline='') as file:
            fn = ['recipe_id', 'name', 'ingredients','prep_time', 'cooking_instructions', 'difficulty', 'category', 'rating', 'last_cooked']
            writer = csv.DictWriter(file, fieldnames=fn)
            writer.writerow(new_recipe)
            print('\nYUM! THIS RECIPE SMELLS GOOD! 🍲\n*RECIPE ADDED SUCCESFULY*')   
    except Exception:
        print('\nUh.. Oh.. Someone Spilled The Pot!\n*ERROR ADDING YOUR RECIPE')

def cook():
    """Cooks a recipe and adds the current date to last cooked"""
    try:
        # Read existing recipes
        with open('recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            recipes = list(reader)
            
        if not recipes:
            print("No recipes found. Please add some recipes first!")
            return
            
        # Display available recipes
        print("\nAvailable recipes to cook:")
        for i, recipe in enumerate(recipes, 1):
            last_cooked = recipe.get('last_cooked', 'Never')
            print(f"{i}. {recipe['name']} (Last cooked: {last_cooked})")
        
        cook_choice = input('\nWhich recipe would you like to cook? (Enter the recipe name): ').strip()
        
        # Find the recipe
        recipe_found = False
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        
        for recipe in recipes:
            if recipe['name'].lower() == cook_choice.lower():
                recipe_found = True
                recipe['last_cooked'] = current_date
                
                # Display the recipe details
                print(f"\n🍳 Cooking: {recipe['name']} 🍳")
                print(f"Ingredients: {recipe['ingredients']}")
                print(f"Instructions: {recipe['cooking_instructions']}")
                print(f"Prep time: {recipe['prep_time']} minutes")
                print(f"Difficulty: {recipe['difficulty']}")
                print(f"Category: {recipe['category']}")
                break
        
        if not recipe_found:
            print('Recipe not found. Please check the name and try again.')
            return
            
        # Write updated recipes back to CSV
        with open('recipes.csv', 'w', newline='') as file:
            # Ensure 'last_cooked' is in the fieldnames
            fieldnames = ['recipe_id', 'name', 'ingredients', 'prep_time', 'cooking_instructions', 'difficulty', 'category', 'rating', 'last_cooked']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for recipe in recipes:
                # Ensure all recipes have the last_cooked field
                if 'last_cooked' not in recipe:
                    recipe['last_cooked'] = ''
                writer.writerow(recipe)
                
        print(f"\n✅ Marked '{cook_choice}' as cooked on {current_date}!")
        print("Enjoy your meal! 🍽️")
        
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except Exception as e:
        print(f'An error occurred while updating the recipe: {e}')

def nostalgic_recipes():
    """View recipes that were not cooked in the last 3 days"""
    try:
        current_date = datetime.date.today()
        with open('recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            not_cooked_recently = []
            for row in reader:
                if row['last_cooked']:
                    last_cooked_date = datetime.datetime.strptime(row['last_cooked'], "%Y-%m-%d").date()
                    days_since_cooked = (current_date - last_cooked_date).days
                    if days_since_cooked > 3:
                        not_cooked_recently.append(row)
            if not_cooked_recently:
                print("\nRecipes not cooked in the last 3 days:")
                for recipe in not_cooked_recently:
                    print(f"- {recipe['name']} last cooked on {recipe['last_cooked']}")
            else:
                print('Looks like you have been doing a lot of cooking lately! NOTHING TO SEE HERE!')
    except Exception:
        print('Uh Oh.. WE DEFINITELY DID NOT FORGET WHERE WE HAVE PUT THAT RECIPE!\n*ERROR FETCHING NOSTALGIC RECIPES')

def recipe_category():
    """View recipes by category"""
    try:
        with open('recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            recipes = list(reader)
            if recipes == []:
                print('We did not find any recipes, GO ADD SOME!')
            elif recipes['category'] is None:
                print('well the categories are here but.. it looks like you did not categorize them!')
            else: 
                for recipe in recipes:
                    if recipe['category'] is not None:
                        print(f"\n {recipe['name']} - Category: {recipe['category']}")
    except Exception:
        print('BREATH... do not worry, we got the recipes.. just gotta get my glasses.. \n*ERROR FETCHING CATEGORIES')

def shopping_list():
    """Shopping list management with options: add recipe to list, view list, and exit"""
    while True:
        print("\n🛒 === Shopping List Manager === 🛒")
        print("1. Add a recipe to the shopping list")
        print("2. View shopping list")
        print("3. Exit shopping list")
        
        try:
            choice = int(input("Choose an option (1-3): "))
            
            if choice == 1:
                add_recipe_to_shopping_list()
            elif choice == 2:
                view_shopping_list()
            elif choice == 3:
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        except ValueError:
            print("Please enter a valid number (1-3).")
        except Exception as e:
            print(f"An error occurred: {e}")

def add_recipe_to_shopping_list():
    """Add a recipe's ingredients to the shopping list"""
    try:
        # Read existing recipes
        with open('recipes.csv', 'r') as file:
            recipes = list(csv.DictReader(file))
            
        if not recipes:
            print('No recipes found. Please add some recipes first!')
            return
            
        # Display available recipes
        print('\n📋 Available recipes to add to shopping list:')
        for i, recipe in enumerate(recipes, 1):
            print(f"{i}. {recipe['name']}")
        
        choice = input('\nWhich recipe would you like to add to your shopping list? (Enter the recipe name): ').strip()
        
        # Find the selected recipe
        recipe_found = False
        for recipe in recipes:
            if recipe['name'].lower() == choice.lower():
                recipe_found = True
                
                # Prepare shopping list entry
                shopping_entry = {
                    'recipe_name': recipe['name'],
                    'ingredients': recipe['ingredients'],
                    'date_added': datetime.date.today().strftime("%Y-%m-%d")
                }
                
                # Read existing shopping list or create new one
                shopping_list_items = []
                try:
                    with open('shopping_list.csv', 'r') as file:
                        shopping_list_items = list(csv.DictReader(file))
                except FileNotFoundError:
                    # Create new shopping list file with headers
                    with open('shopping_list.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(['recipe_name', 'ingredients', 'date_added'])
                
                # Check if recipe is already in shopping list
                already_exists = False
                for item in shopping_list_items:
                    if item['recipe_name'].lower() == choice.lower():
                        already_exists = True
                        break
                
                if already_exists:
                    print(f"'{recipe['name']}' is already in your shopping list!")
                else:
                    # Add to shopping list
                    with open('shopping_list.csv', 'a', newline='') as file:
                        fieldnames = ['recipe_name', 'ingredients', 'date_added']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow(shopping_entry)
                    
                    print(f"\n✅ Added '{recipe['name']}' to your shopping list!")
                    print(f"Ingredients needed: {recipe['ingredients']}")
                break
        
        if not recipe_found:
            print(f"Recipe '{choice}' not found. Please check the name and try again.")
            
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except Exception as e:
        print(f'An error occurred while adding to shopping list: {e}')

def view_shopping_list():
    """View all items in the shopping list"""
    try:
        with open('shopping_list.csv', 'r') as file:
            shopping_items = list(csv.DictReader(file))
            
        if not shopping_items:
            print("\n🛒 Your shopping list is empty!")
            print("Use option 1 to add recipes to your shopping list.")
            return
            
        print("\n🛒 === Your Shopping List === 🛒")
        print("-" * 50)
        
        for i, item in enumerate(shopping_items, 1):
            print(f"{i}. Recipe: {item['recipe_name']}")
            print(f"   Ingredients: {item['ingredients']}")
            print(f"   Added on: {item['date_added']}")
            print("-" * 50)
        
        # Option to clear shopping list
        clear_choice = input("\nWould you like to clear your shopping list? (y/n): ").lower().strip()
        if clear_choice in ['y', 'yes']:
            with open('shopping_list.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['recipe_name', 'ingredients', 'date_added'])
            print("🗑️ Shopping list cleared!")
            
    except FileNotFoundError:
        print("\n🛒 Your shopping list is empty!")
        print("Use option 1 to add recipes to your shopping list.")
    except Exception as e:
        print(f'An error occurred while viewing shopping list: {e}')               

def view_random_recipe():
    """Generate A Random Recipe from Available Recipes"""
    try:
        with open('recipes.csv', 'r') as file:
            recipes = list(csv.DictReader(file))
            
        if not recipes:
            print("No recipes available for random selection.")
            return
            
        i = 1
        while i != 0:
            try:
                i = int(input("Enter '1' to generate another random recipe or '0' to exit: "))

                if i == 1:
                    index = rd.randint(0, len(recipes) - 1)
                    recipe = recipes[index]

                    print(f"\n=========== Here is a Random Recipe you can try ===============\n")
                    print(f"Recipe Name: {recipe['name']}")
                    print(f"Ingredients: {recipe['ingredients']}")
                    print(f"Preparation Time: {recipe['prep_time']} minutes")
                    print(f"Difficulty: {recipe['difficulty']}")
                    print(f"Category: {recipe['category']}")
                    print(f"Instructions: {recipe['cooking_instructions']}")
                    rating = recipe['rating'] if recipe['rating'] else 'Not rated'
                    print(f"Rating: {rating}")
                    print("=" * 65)
                    
                elif i == 0:
                    print("Thank you for using the recipe app!")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number (1 or 0).")
                
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except Exception as e:
        print(f"An error occurred: {e}")

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
                                fieldnames = ['recipe_id', 'name', 'ingredients', 'prep_time', 'cooking_instructions', 'difficulty', 'category', 'rating', 'last_cooked']
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
        def get_rating(recipe):
            return recipe["rating"]
        recipes.sort(key=get_rating, reverse=True)
        
        print("\n=== Recipes Sorted by Rating ===")
        for recipe in recipes:
            rating_display = f"{recipe['rating']} stars" if recipe['rating'] > 0 else "Not rated"
            print(f"{recipe['name']} - {rating_display}")
            
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except Exception as e:
        print(f"An error occurred: {e}")
def scaling_ingredients():
    """" Scaling the Quantity of ingredients based on Number of Servings"""
    try:
        # Read existing recipes
        with open('recipes.csv', 'r') as file:
            reader = csv.DictReader(file)
            recipes = list(reader)
            
        if not recipes:
            print("No recipes found. Please add some recipes first!")
            return
            
        # Display available recipes
        print("\nAvailable recipes to scale:")
        for i, recipe in enumerate(recipes, 1):
            print(f"{i}. {recipe['name']}")
            
        choice = input('\nWhich recipe would you like to scale? (Enter the recipe name): ')
        
        # Find the recipe
        recipe_found = False
        selected_recipe = None
        
        for recipe in recipes:
            if recipe['name'].lower() == choice.lower():
                recipe_found = True
                selected_recipe = recipe
                break
        
        if not recipe_found:
            print('Recipe not found. Please check the name and try again.')
            return
            
        # Display the recipe details
        print(f"\nRecipe: {selected_recipe['name']}")
        print(f"Ingredients: {selected_recipe['ingredients']}")
        print(f"Instructions: {selected_recipe['cooking_instructions']}")
        print(f"Prep time: {selected_recipe['prep_time']} minutes")
        print(f"Difficulty: {selected_recipe['difficulty']}")
        print(f"Category: {selected_recipe['category']}")
        
        servings = int(input("\nEnter number of servings: "))
        print("\n===============The Quantity of ingredients you require================")
        print(f"For {servings} servings of {selected_recipe['name']}")
        print(f"You will need: {servings} x {selected_recipe['ingredients']}")
        print("===================================================================")
        
    except FileNotFoundError:
        print("No recipes file found. Please add some recipes first!")
    except ValueError:
        print("Please enter a valid number for servings.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

