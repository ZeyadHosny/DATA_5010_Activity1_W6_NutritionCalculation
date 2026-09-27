from food_item import FoodItem, DEFAULT_NAME_ATTRIBUTE_VALUE, DEFAULT_NUMERIC_ATTRIBUTE_VALUE

# Zero value to avoid magic numbers.
ZERO_VALUE = 0.0
# Default value for number of servings when unknown.
DEFAULT_SERVINGS_VALUE = 1.0
# --- Input limits ------------------------------------------------
# Maximum number of characters in a food name.
MAX_NAME_LENGTH = 200
# Maximum grams accepted for each nutrient (fat, carbohydrates, protein).
MAX_NUTRIENT_GRAMS = 10000
# Maximum number of servings.
MAX_SERVINGS = 100000
# Maximum number of attempts allowed per input (initial entry + retries). Must be an integer greater than 0.
MAX_NUM_ATTEMPTS = 2
# Index of the last attempt (attempt indices run 0 .. MAX_NUM_ATTEMPTS - 1).
LAST_ATTEMPT = MAX_NUM_ATTEMPTS - 1


def looks_numeric(text):
    """
    Description:
    - Check if a string does not contain letters and underscores.
    - Decimal values such as "1.5" are valid, since amounts are floats.
    - Other examples of rejected formats are ("nan", "inf", "1e10", "1_000").
    - The malformed text (e.g. "1.2.3", "5-5") passes this check
    and is rejected afterwards by float() itself.

    Input arguments:
        text (str): The string to check.

    Return:
        bool: True if `text` does not contain letters and underscores, False otherwise.
    """
    for character in text:
        # A letter or underscore means the text is not plain numeric input.
        if character.isalpha() or character == "_":
            return False
    return True


def read_item_name():
    """
    Description:
    - Prompt for the food item name and return it.
    - A blank entry returns the default "Water". An invalid entry is
    re-prompted until the last allowed attempt, then "Water" is used.

    Input arguments:
        None

    Return:
        str: The food item name.
    """
    prompt = (f"Enter the food item name (up to {MAX_NAME_LENGTH} characters, "
              f"or leave blank to use the default '{DEFAULT_NAME_ATTRIBUTE_VALUE}'): ")

    # Retries until the last allowed attempt (MAX_NUM_ATTEMPTS total), then falls back to the default.
    for attempt in range(MAX_NUM_ATTEMPTS):
        # Request the user to input the food item name and deletes trailing/leading whitespace.
        raw_name = input(prompt).strip()

        # Blank input is a deliberate skip, not an error. It is checked before
        # validation so it is never reported as an invalid name.
        if raw_name == "":
            return DEFAULT_NAME_ATTRIBUTE_VALUE

        # Each check below raises ValueError with a message naming its problem.
        try:
            # Error handled: name consists only of digits (e.g. "12345").
            if raw_name.isdigit():
                raise ValueError(f"'{raw_name}' is made up entirely of numbers")
            # Error handled: name has no letters, e.g. symbols only ("!!!")
            # or digits mixed with symbols ("123!").
            if not any(character.isalpha() for character in raw_name):
                raise ValueError(f"'{raw_name}' does not contain any letters")
            # Error handled: name is longer than MAX_NAME_LENGTH characters.
            if len(raw_name) > MAX_NAME_LENGTH:
                raise ValueError(f"exceeds the {MAX_NAME_LENGTH}-character limit")
        # Error handled: any invalid-name ValueError raised above.
        except ValueError as error:
            # Last allowed attempt: report the reason and use the default.
            if attempt == LAST_ATTEMPT:
                print(f"Invalid name: {error}. Using default value '{DEFAULT_NAME_ATTRIBUTE_VALUE}'.")
                return DEFAULT_NAME_ATTRIBUTE_VALUE
            # Not the last allowed attempt yet: report the reason and ask again.
            print(f"Invalid name: {error}. Please try again.")
            continue
        # Error handled: any unexpected exception other than ValueError
        # (safety procedure), treated like an invalid entry.
        except:
            if attempt == LAST_ATTEMPT:
                print(f"Something unexpected happened while reading the name. "
                      f"Using default value '{DEFAULT_NAME_ATTRIBUTE_VALUE}'.")
                return DEFAULT_NAME_ATTRIBUTE_VALUE
            print("Something unexpected happened while reading the name. "
                  "Please try again.")
            continue

        return str(raw_name)


def read_nutrient(field_label):
    """
    Description:
    - Prompt for one nutrient amount in grams and return it as a float.
    - A blank entry returns 0.0, which is harmless because nutrients are
    summed.
    - An invalid entry is re-prompted until the last allowed
    attempt, then defaults to 0.0.

    Input arguments:
        field_label (str): The label for the nutrient field (fat or carbohydrates or protein).

    Return:
        float: The nutrient amount in grams.
    """
    prompt = (f"Enter grams of {field_label} (0-{MAX_NUTRIENT_GRAMS}, "
              f"or leave blank to use the default of {DEFAULT_NUMERIC_ATTRIBUTE_VALUE:.2f} g): ")

    # Retries until the last allowed attempt (MAX_NUM_ATTEMPTS total), then falls back to the default.
    for attempt in range(MAX_NUM_ATTEMPTS):
        # Request the user to input the nutrient amount and deletes trailing/leading whitespace.
        raw_value = input(prompt).strip()

        # Blank input is a deliberate skip, not an error. It is checked before
        # validation so it is never reported as an invalid number.
        if raw_value == "":
            return DEFAULT_NUMERIC_ATTRIBUTE_VALUE

        # Each check below raises ValueError with a message naming its problem.
        try:
            # Error handled: text contains a letter or an underscore ("abc", "1_000", "1e100").
            if not looks_numeric(raw_value):
                raise ValueError(f"'{raw_value}' is not a valid number")
            # Error handled: float() raises ValueError itself for malformed
            # text that passed the check above ("1.2.3", "5-5", "1 0", "-").
            value = float(raw_value)
            # Error handled: negative amount.
            if value < ZERO_VALUE:
                raise ValueError(f"{value} is negative")
            # Error handled: amount above MAX_NUTRIENT_GRAMS.
            if value > float(MAX_NUTRIENT_GRAMS):
                raise ValueError(f"{value} exceeds the maximum of {MAX_NUTRIENT_GRAMS}g")
        # Error handled: any invalid-amount ValueError raised above.
        except ValueError as error:
            # Last allowed attempt: report the reason and use the default.
            if attempt == LAST_ATTEMPT:
                print(f"Invalid {field_label}: {error}. Using default value {DEFAULT_NUMERIC_ATTRIBUTE_VALUE:.2f}.")
                return DEFAULT_NUMERIC_ATTRIBUTE_VALUE
            # Not the last allowed attempt yet: report the reason and ask again.
            print(f"Invalid {field_label}: {error}. Please try again.")
            continue
        # Error handled: any unexpected exception other than ValueError
        # (safety procedure), treated like an invalid entry.
        except:
            if attempt == LAST_ATTEMPT:
                print(f"Something unexpected happened while reading {field_label}. "
                      f"Using default value {DEFAULT_NUMERIC_ATTRIBUTE_VALUE:.2f}.")
                return DEFAULT_NUMERIC_ATTRIBUTE_VALUE
            print(f"Something unexpected happened while reading {field_label}. "
                  f"Please try again.")
            continue

        # Check if the entered value is "-0" and return it as "0"
        if value == ZERO_VALUE:
            return ZERO_VALUE
        
        return float(value)


def read_num_servings():
    """
    Description:
    - Prompt for the number of servings and return it as a float.
    - A blank entry returns 1.0. An invalid entry is re-prompted until the
    last allowed attempt, then defaults to 1.0.

    Input arguments:
        None

    Return:
        float: The number of servings.
    """
    prompt = (f"Enter the number of servings (0-{MAX_SERVINGS}, "
              f"or leave blank to use the default of {DEFAULT_SERVINGS_VALUE:.2f} serving(s)): ")

    # Retries until the last allowed attempt (MAX_NUM_ATTEMPTS total), then falls back to the default.
    for attempt in range(MAX_NUM_ATTEMPTS):
        # Request the user to input the number of servings and deletes trailing/leading whitespace.
        raw_value = input(prompt).strip()

        # Blank input is a deliberate skip, not an error. It is checked before
        # validation so it is never reported as an invalid number.
        if raw_value == "":
            return DEFAULT_SERVINGS_VALUE

        # Each check below raises ValueError with a message naming its problem.
        try:
            # Error handled: text is not plain numeric, i.e. it contains a
            # letter or underscore ("abc", "1_000").
            if not looks_numeric(raw_value):
                raise ValueError(f"'{raw_value}' is not a valid number")
            # Error handled: float() raises ValueError itself for malformed
            # text that passed the check above ("1.2.3", "5-5", "1 0", "-").
            value = float(raw_value)
            # Error handled: negative number of servings.
            if value < ZERO_VALUE:
                raise ValueError(f"{value} is negative")
            # Error handled: zero servings (the count must be positive).
            if value == ZERO_VALUE:
                raise ValueError("0 servings is not meaningful")
            # Error handled: number of servings above MAX_SERVINGS.
            if value > float(MAX_SERVINGS):
                raise ValueError(f"{value} exceeds the maximum of {MAX_SERVINGS}")
        # Error handled: any invalid-servings ValueError raised above.
        except ValueError as error:
            # Last allowed attempt: report the reason and use the default.
            if attempt == LAST_ATTEMPT:
                print(f"Invalid number of servings: {error}. Using default value {DEFAULT_SERVINGS_VALUE:.2f}.")
                return DEFAULT_SERVINGS_VALUE
            # Not the last allowed attempt yet: report the reason and ask again.
            print(f"Invalid number of servings: {error}. Please try again.")
            continue
        # Error handled: any unexpected exception other than ValueError
        # (safety procedure), treated like an invalid entry.
        except:
            if attempt == LAST_ATTEMPT:
                print(f"Something unexpected happened while reading the number "
                      f"of servings. Using default value {DEFAULT_SERVINGS_VALUE:.2f}.")
                return DEFAULT_SERVINGS_VALUE
            print("Something unexpected happened while reading the number of "
                  "servings. Please try again.")
            continue

        return float(value)


def read_continue_choice():
    """
    Description:
    - Ask whether to print the nutrition information for another food item and return "y/Y" or "n/N".
    - Re-prompts until the answer is valid.
    - If "Ctrl+C" or "end of input" is entered, it will be handled in the main loop.

    Input arguments:
        None

    Return:
        str: "y" or "n" based on the user's choice.
    """
    prompt = "\nDo you want to print the nutrition information for any other food item? 'y/Y' or 'n/N': "

    while True:
        # Request the user to input their choice and deletes trailing/leading whitespace and lowercases it.
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice
        # Error handled: any answer other than Y/y/N/n (including blank);
        # report it and ask again.
        print(f"Invalid response: '{choice}' is not 'Y' or 'N'. Please try again.")


def main():
    """
    Description:
    - Run the program: each pass reads one food item, prints its nutrition information, then asks
    whether to continue, so the loop always runs at least once.
    - Any input() call can raise EOFError or KeyboardInterrupt, so they are
    handled once here instead of inside every read function.
    """
    try:
        while True:
            # Request the user to input the food item name.
            item_name = read_item_name()
            # Request the user to input the fat amount in grams.
            fat = read_nutrient("fat")
            # Request the user to input the carbohydrates amount in grams.
            carbohydrates = read_nutrient("carbohydrates")
            # Request the user to input the protein amount in grams.
            protein = read_nutrient("protein")
            # Request the user to input the number of servings.
            num_servings = read_num_servings()
            # Create a new FoodItem instance with the provided values.
            food_item = FoodItem(item_name, fat, carbohydrates, protein)
            # Print the nutrition information for the current food item.
            food_item.print_nutrition_info(num_servings)
            # Ask the user whether to continue or not.
            if read_continue_choice() == "n":
                break
    # Error handled: the input stream ended (EOFError, e.g. Ctrl+D "Unix-like terminals" or ctrl +z +enter "windows") or the user
    # pressed Ctrl+C (KeyboardInterrupt); exit cleanly instead of a traceback.
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended unexpectedly. Exiting.")


# Run main() only when this file is executed directly, not when it is imported.
if __name__ == "__main__":
    main()
