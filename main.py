import csv
import random
import uuid

# Hussain Darwish

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
