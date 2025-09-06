# 🍳 Ratatouille - Digital Recipe Book

A comprehensive Python-based recipe management application that helps you store, organize, and manage your favorite recipes in a digital format.

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Functions Overview](#functions-overview)
- [CSV File Format](#csv-file-format)
- [Contributing](#contributing)
- [Author](#author)

## ✨ Features

### 🍽️ Core Recipe Management
- **Add New Recipes**: Store recipes with detailed information including ingredients, instructions, prep time, difficulty, and category
- **View All Recipes**: Display all stored recipes with complete details
- **Search by Ingredient**: Find recipes containing specific ingredients
- **Random Recipe Suggestion**: Get random recipe recommendations

### ⭐ Rating & Organization
- **Rate Recipes**: Add 1-5 star ratings to your recipes
- **View by Rating**: See recipes sorted by their ratings
- **Recipe Categories**: Organize recipes by meal type (Breakfast, Lunch, Dinner, Dessert)
- **Difficulty Levels**: Classify recipes as Easy, Medium, or Hard

### 👨‍🍳 Cooking Features
- **Cook Tracking**: Mark recipes as cooked and track cooking dates
- **Nostalgic Recipes**: View recipes you haven't cooked in a while (3+ days)
- **Ingredient Scaling**: Scale recipe ingredients for different serving sizes

### 🛒 Shopping List Management
- **Add to Shopping List**: Add recipe ingredients to a persistent shopping list
- **View Shopping List**: See all recipes and ingredients you plan to buy
- **Clear Shopping List**: Remove all items when shopping is complete
- **Date Tracking**: Track when recipes were added to the shopping list

## 🚀 Installation

### Prerequisites
- Python 3.x
- Standard Python libraries (csv, random, uuid, datetime)

### Setup
1. Clone or download the repository
2. Ensure you have Python installed on your system
3. Navigate to the project directory
4. Run the application:
```bash
python main.py
```

## 💻 Usage

### Starting the Application
Run the main.py file to start the Ratatouille application:

```bash
python main.py
```

### Main Menu Options
```
=== Ratatouille ===
1. Add a new recipe to the collection
2. Search for recipes by ingredient
3. View all recipes
4. View a random recipe suggestion
5. Rate a recipe
6. View recipes sorted by rating
7. Cook a recipe
8. View recipes that you didn't cook in a while
9. Scale ingredients for a recipe
10. Create a shopping list
11. Exit
```

### Shopping List Submenu
```
🛒 === Shopping List Manager === 🛒
1. Add a recipe to the shopping list
2. View shopping list
3. Exit shopping list
```

## 📁 File Structure

```
DSB_projects/
├── main.py                 # Main application file
├── recipes.csv            # Recipe database (auto-created)
├── shopping_list.csv      # Shopping list storage (auto-created)
└── README.md              # This file
```

## 🔧 Functions Overview

### Core Functions
- `main()` - Main application loop and menu handler
- `display_menu()` - Shows the main menu options
- `add_recipe()` - Add new recipes to the database
- `view_all_recipes()` - Display all stored recipes

### Search & Discovery
- `recipes_by_ingredients()` - Search recipes by ingredient
- `view_random_recipe()` - Get random recipe suggestions
- `view_recipes_sorted_by_rating()` - View recipes sorted by rating

### Recipe Management
- `rate_recipe()` - Add or update recipe ratings
- `cook()` - Mark recipes as cooked and update last cooked date
- `nostalgic_recipes()` - Find recipes not cooked recently
- `scaling_ingredients()` - Scale recipe ingredients for different serving sizes

### Shopping List
- `shopping_list()` - Shopping list management menu
- `add_recipe_to_shopping_list()` - Add recipe ingredients to shopping list
- `view_shopping_list()` - View and manage shopping list items

## 📊 CSV File Format

### recipes.csv
```csv
recipe_id,name,ingredients,prep_time,cooking_instructions,difficulty,category,rating,last_cooked
```

### shopping_list.csv
```csv
recipe_name,ingredients,date_added
```

## 🎯 Example Usage

### Adding a Recipe
1. Select option 1 from the main menu
2. Enter recipe name: "Chocolate Chip Cookies"
3. Add ingredients with quantities
4. Set preparation time: 30 minutes
5. Add step-by-step instructions
6. Choose difficulty: Easy
7. Select category: Dessert

### Creating a Shopping List
1. Select option 10 from the main menu
2. Choose option 1 to add a recipe
3. Select "Chocolate Chip Cookies"
4. Recipe ingredients are added to your shopping list
5. Use option 2 to view your complete shopping list

### Rating a Recipe
1. Select option 5 from the main menu
2. Choose a recipe from the displayed list
3. Enter a rating from 1-5 stars
4. Rating is saved and can be viewed in sorted lists

## 🏗️ Data Persistence

- All recipe data is stored in `recipes.csv`
- Shopping list data is stored in `shopping_list.csv`
- Files are automatically created if they don't exist
- Data persists between application sessions

## 🔒 Error Handling

The application includes comprehensive error handling for:
- File not found errors
- Invalid user input
- CSV reading/writing errors
- Recipe not found scenarios
- Invalid rating values

## 🎨 User Experience Features

- **Emoji Integration**: Visual indicators throughout the interface
- **Clear Formatting**: Well-organized output with separators
- **Input Validation**: Prevents invalid data entry
- **User-Friendly Messages**: Clear success and error messages
- **Menu Loop System**: Easy navigation between features

## 🤝 Contributing

This project was developed as part of a Data Science Bootcamp. Contributions and improvements are welcome!

### Development Team Contributors
- Recipe Management Core: Multiple contributors
- Shopping List Feature: Enhanced functionality
- Rating System: Integrated rating and sorting
- User Interface: Menu system and user experience

## 👨‍💻 Author

**Hussain Darwish**
- Data Science Bootcamp Project
- University of Bahrain

## 📝 License

This project is part of an educational program and is intended for learning purposes.

## 🚀 Future Enhancements

Potential features for future versions:
- Recipe import/export functionality
- Nutritional information tracking
- Recipe photos and images
- Meal planning calendar
- Recipe sharing capabilities
- Advanced search filters
- Recipe recommendations based on available ingredients

---

*Enjoy cooking with Ratatouille! 🍳👨‍🍳*
