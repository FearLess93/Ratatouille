import csv
import random
import uuid

# Hussain Darwish
def display_menu():
    """Display the main menu options."""
    print("\n=== Ratatouille ===")
    print("1. Add a new recipe to the collection")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. View a random recipe suggestion ")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def main():
    """Main application function."""
    print("Welcome to Ratatouille!")
    print("This app helps you to create a digital recipe book that allows users to store, retrieve, and manage your favorite recipes in a .csv file.")

    while True:
        choice = display_menu()

        if choice == '1':
            add_recipe()
        elif choice == '2':
            recipes_by_ingredients()
        elif choice == '3':
            view_all_recipe()
        elif choice == '4':
            view_random_recipe()
        elif choice == '5':
            print("Thank you for using Ratatouille. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
#Zahra

#Maryam
def recipes_by_ingredients():
    ingredients = input('Which ingredient would you like to search for?  ').lower()
    found = False 
    with open(FILENAME, 'r') as file:
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
#Sayed Hussain

#Waseem
