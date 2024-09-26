#Please give me any sample example to Combining knowledge graphs and LLMs

#Example: Personalized Recipe Recommendations with Knowledge Graphs and LLMs

import random
from typing import Dict, List

# Simulating a simplified knowledge graph using dictionaries
# In a real scenario, this would be a database or graph database
ingredients = {
    "tomato": {"type": "vegetable", "flavor": ["savory", "sweet"], "suitable_for": ["vegan", "vegetarian"]},
    "onion": {"type": "vegetable", "flavor": ["savory"], "suitable_for": ["vegan", "vegetarian"]},
    "garlic": {"type": "vegetable", "flavor": ["savory"], "suitable_for": ["vegan", "vegetarian"]},
    "basil": {"type": "herb", "flavor": ["herbaceous", "aromatic"], "suitable_for": ["vegan", "vegetarian"]},
    "chickpea": {"type": "legume", "flavor": ["nutty"], "suitable_for": ["vegan", "vegetarian"]},
    "spinach": {"type": "vegetable", "flavor": ["savory"], "suitable_for": ["vegan", "vegetarian"]}
}

recipes = {
    "Tomato Soup": {
        "cuisine": "Italian",
        "ingredients": ["tomato", "onion", "garlic", "basil"],
        "techniques": ["boiling"],
        "flavor": ["savory", "sweet"],
        "suitable_for": ["vegan", "vegetarian"]
    },
    "Chickpea Curry": {
        "cuisine": "Indian",
        "ingredients": ["chickpea", "onion", "garlic", "tomato", "spinach"],
        "techniques": ["frying", "boiling"],
        "flavor": ["spicy", "savory"],
        "suitable_for": ["vegan", "vegetarian"]
    },
    # Add more recipes as needed
}

# Simple LLM simulation using a random choice function
def generate_description(recipe: Dict) -> str:
    """Generates a simple description for a recipe."""
    description = f"This {recipe['cuisine']} dish features {', '.join(recipe['ingredients'])} and is {', '.join(recipe['flavor'])}."
    description += f" It is prepared using techniques like {', '.join(recipe['techniques'])} and is suitable for {', '.join(recipe['suitable_for'])} diets."
    return description

def recommend_recipes(user_preferences: Dict) -> List[str]:
    """Recommends recipes based on user preferences."""
    recommended = []
    for recipe_name, recipe in recipes.items():
        # Simple matching for demonstration
        if (
            user_preferences.get("cuisine", None) in [recipe["cuisine"]]
            and all(
                preference in recipe["suitable_for"]
                for preference in user_preferences.get("dietary", [])
            )
        ):
            recommended.append(recipe_name)

    # Shuffle recommendations for variety
    random.shuffle(recommended)

    return recommended

# User preferences example
user_preferences = {"cuisine": "Italian", "dietary": ["vegan"]}

# Get recommendations
recommendations = recommend_recipes(user_preferences)

# Display recommendations with descriptions
for recipe_name in recommendations:
    print(f"Recommendation: {recipe_name}")
    print(generate_description(recipes[recipe_name]))
    print("-" * 20)