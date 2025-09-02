import csv
import uuid

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
