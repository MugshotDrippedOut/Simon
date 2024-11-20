# Find places of interest in selected state and/or city
- API (free):
    - [amadeus](https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/points-of-interest)
    - [serpapi](https://serpapi.com/popular-destinations)

## Recipe Finder app
- Ingredient Selection:
    - User selects items they already have (from a list or by typing).
    - Use a database of common ingredients to populate suggestions dynamically.
- Recipe Suggestions:
    - Fetch recipes from an API like Spoonacular or Edamam based on the selected ingredients.
    - Display recipes with images, preparation time, difficulty, and step-by-step instructions.
- "Missing Ingredients" Suggestions:
    - Fetch recipes that require only one or two additional ingredients.
    - Highlight the missing items needed to complete the recipe.
- Shopping List Generator:
    - Allow users to save "missing items" as a shopping list.
    - Optionally group items by type (e.g., produce, dairy).
- Favorites:
    - Users can save their favorite recipes for quick access.
    - Use local storage or a simple database like Firebase for storage.
- Filters and Sorting:
    - Filters: Cuisine type, dietary preferences (e.g., vegan, gluten-free), difficulty level.
    - Sort by: Preparation time, popularity, or number of missing ingredients.
- Progressive Web App (PWA):
  - Enable offline access for saved recipes or the shopping list.

