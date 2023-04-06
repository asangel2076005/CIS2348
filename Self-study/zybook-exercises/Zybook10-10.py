class FoodItem:

    def __init__(self, name="Water", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * servings
        return calories

    def print_info(self):
        print(f"Nutritional information per serving of {self.name}:")
        print(f"  Fat: {self.fat:.2f} g")
        print(f"  Carbohydrates: {self.carbs:.2f} g")
        print(f"  Protein: {self.protein:.2f} g")


if __name__ == "__main__":
    name_food = input()
    if name_food == "Water" or name_food == "water":
        food = FoodItem()
        food.print_info()
        print(f"Number of calories for {1:.2f} serving(s): {food.get_calories(1):.2f}")
    else:
        name_fat = float(input())
        name_carbs = float(input())
        name_protein = float(input())
        servings = float(input())

        food = FoodItem(name_food, name_fat, name_carbs, name_protein)
        food.print_info()
        print(f"Number of calories for {1:.2f} serving(s): {food.get_calories(1):.2f}")
        print(f"Number of calories for {servings:.2f} serving(s): {food.get_calories(servings):.2f}")