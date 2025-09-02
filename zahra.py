import csv
import random
import uuid

recipes = [{'name':'cookies','prep_time':'25'},{'name':'cake','prep_time':'55'}]

def view_all_recipes(i):
    '''View all recipies in the database.'''
    if len(recipes) > 0:
        for i in recipes:
            print(f"Recipe Name: {i['name']} \nPreperation Time: {i['prep_time']} minutes \n\n")
    else:
        print('No Recipes Found')

view_all_recipes(recipes)
