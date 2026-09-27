# Default values for numeric nutrition attributes.
DEFAULT_NUMERIC_ATTRIBUTE_VALUE = 0.0
# Default value for food item name.
DEFAULT_NAME_ATTRIBUTE_VALUE = "Water"
# Constant to avoid magic numbers.
ONE_VALUE = 1.0
# Constant for calculating calories (kcal/g) for fat.
CALORIES_PER_GRAM_FAT = 9.0
# Constant for calculating calories (kcal/g) for carbohydrates and protein.
CALORIES_PER_GRAM_CARB_OR_PROTEIN = 4.0

class FoodItem:
    """
    Description:
    - A food or drink item class.

    Attributes:
        item_name (str): The name of the food item.
        fat (float): The amount of fat in grams.
        carbohydrates (float): The amount of carbohydrates in grams.
        protein (float): The amount of protein in grams.

    Methods:
        __init__: constructor.
        get_calories: calculate calories for one serving.
        print_nutrition_info: print nutrition information for the specified number of servings.
    """

    # Constructor
    def __init__(self, item_name = DEFAULT_NAME_ATTRIBUTE_VALUE, fat = DEFAULT_NUMERIC_ATTRIBUTE_VALUE, carbohydrates = DEFAULT_NUMERIC_ATTRIBUTE_VALUE, protein = DEFAULT_NUMERIC_ATTRIBUTE_VALUE):
        """
        Description:
        - Constructor for the FoodItem class.

        Input arguments:
           item_name (str): The name of the food item.
           fat (float): The amount of fat in grams.
           carbohydrates (float): The amount of carbohydrates in grams.
           protein (float): The amount of protein in grams.
        """
        self.item_name = str(item_name)
        self.fat = float(fat)
        self.carbohydrates = float(carbohydrates)
        self.protein = float(protein)

    # Method to calculate calories for one serving
    def get_calories(self):
        """
        Description:
        Calories for ONE serving: 9 kcal/g fat, 4 kcal/g carbohydrates and protein.
        
        Input arguments:
           None
        
        Return:
            float: The total calories for one serving.
        """
        total_calories_per_serving = (self.fat * CALORIES_PER_GRAM_FAT
                                       + self.carbohydrates * CALORIES_PER_GRAM_CARB_OR_PROTEIN
                                       + self.protein * CALORIES_PER_GRAM_CARB_OR_PROTEIN)
        return total_calories_per_serving

    # Method to print nutrition information
    def print_nutrition_info(self, num_servings):
        """
        Description:
        - Print name, per-serving nutrients and calories.
        - The multi-serving calories line is added only when num_servings != 1.
        
        Input arguments:
           num_servings (float): The number of servings.
        
        Return:
            None (prints nutrition information to the output terminal)
        """
        print(f"Nutritional information per serving of {self.item_name}:")
        print(f"Fat: {self.fat:.2f} g")
        print(f"Carbohydrates: {self.carbohydrates:.2f} g")
        print(f"Protein: {self.protein:.2f} g")
        print(f"Number of calories for {ONE_VALUE:.2f} serving(s): {self.get_calories():.2f}")
        if num_servings != ONE_VALUE:
            print(f"Number of calories for {num_servings:.2f} serving(s): {self.get_calories() * num_servings:.2f}")

