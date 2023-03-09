class FoodItem:

    def __init__(self, name=None, fat=0, carbs=0, protein=0 ):
        self.name = name
        self.fat = 0
        self.carbs = 0
        self.protein = 0

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_food_item(self):
        print(f"Nutritional information per serving of {self.name}:")
        print(f"   Fat: {self.fat:.2f} g")
        print(f"   Carbohydrates: {self.carbs:.2f} g")
        print(f"   Protein: {self.protein:.2f} g")

if __name__ == "__main__":
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    servings = float(input())

    food1 = FoodItem()
    food1.print_food_item()
    print(f"Number of calories for {servings:.2f} serving(s): {food1.get_calories(servings):.2f}")
    print()

    food2 = FoodItem(name, fat, carbs, protein)
    food2.print_food_item()
    print(f"Number of calories for {servings:.2f} serving(s): {food2.get_calories(servings):.2f}")