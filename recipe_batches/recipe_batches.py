#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  for key in recipe:
    if key not in ingredients or len(recipe) > len(ingredients):
      return 0
    else:
      batches = [0] * len(recipe)
      index = 0
      # Get the number of batches per ingredient
      for key, value in recipe.items():
        batches[index] = ingredients[key] // recipe[key]
        index += 1
      return min(batches)
print(recipe_batches({'milk': 100, 'butter': 50, 'flour': 5},{'milk': 138, 'butter': 52, 'flour': 51}))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))