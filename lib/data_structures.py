spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['spiciness_level'] > 5]
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name, cuisine, heat_level = food
        heat_icons = '🌶' * len(heat_level)  # Use the length of the heat level string
        print(f"{name} ({cuisine}) | Heat Level: {heat_icons}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return {'name': food['name'], 'cuisine': food['cuisine'], 'heat_level': food['heat_level']}
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return int(average)

# Example data
spicy_foods = [
    {'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9},
    {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3},
    {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}
]

# Testing the functions
print_spicy_foods(spicy_foods)
print()

american_food = get_spicy_food_by_cuisine(spicy_foods, "American")
if american_food:
    print(american_food)
else:
    print("No American spicy food found.")
print()

print_spiciest_foods(spicy_foods)
print()

avg_heat = average_heat_level(spicy_foods)
print(f"Average Heat Level: {avg_heat}")
