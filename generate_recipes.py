
import json
import os

dataPath = "data/"
namespacePath = "stereo_recipes/"
recipesPath = "recipes/"
fullPath = dataPath + namespacePath + recipesPath

with open("stonecutting_recipes.json", "r") as f:
    cutting_recipes = json.load(f)

with open("blasting_recipes.json", "r") as f:
    blasting_recipes = json.load(f)

if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists("data/stereo_recipes"):
    os.mkdir("data/stereo_recipes")

if not os.path.exists("data/stereo_recipes/recipes"):
    os.mkdir("data/stereo_recipes/recipes")

def template(type ,input, output): 
    if type == "stonecutting":
        if "slab" in output:
            count = 2
        elif "button" in output:
            count = 8
        elif "trapdoor" in output:
            count = 3
        elif "fence" in output:
            count = 2
        elif "sign" in output:
            count = 2
        elif "plate" in output:
            count = 4
        elif "planks" in output:
            count = 4
        elif "mosaic" in output:
            count = 2
        else:
            count = 1
        template = {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"minecraft:{input}"
            },
            "result": f"minecraft:{output}",
            "count": count
        }
        return template
    if type == "blasting":
        template = {
            "type": "minecraft:blasting",
            "ingredient": {
                "item": f"minecraft:{input}"
            },
            "result": f"minecraft:{output}",
            "experience": 0.1,
            "cookingtime": 100
        }
        return template

for type in cutting_recipes:
    for block in cutting_recipes[type]:
        print(type)
        print(block)
        with open(fullPath + type + "_to_" + cutting_recipes[type][block] + ".json", "w") as f:
            json.dump(template("stonecutting", type, cutting_recipes[type][block]), f, indent=4)

for type in blasting_recipes:
    for block in blasting_recipes[type]:
        with open(fullPath + type + "_to_" + blasting_recipes[type] + ".json", "w") as f:
            json.dump(template("blasting", type, blasting_recipes[type]), f, indent=4)



