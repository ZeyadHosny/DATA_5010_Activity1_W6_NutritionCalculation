# Nutrition Calculator (Q2: Nutritional Information)
Zeyad Hosny: Class Participation Activity 1, BGSU, Fall 2026.

A small Python program that reads a food or drink (name, grams of fat, carbohydrates and protein, and a number of servings) and prints its nutrition per serving and its calories for one serving and for the requested number of servings (if number of servings != 1). It is built around a FoodItem class and validates every input, so bad or missing values never crash the program or silently corrupt a result.



## 1. Repository contents

- food_item.py: the FoodItem class. It stores the name and the grams of fat, carbohydrates and protein, computes calories for one serving, prints the nutrition information (including the total for the requested number of servings when it is not equal to 1).
- nutrition.py: the program. It prompts for each input, validates it, creates a FoodItem instance, prints the nutrition information, and asks whether to continue. This is the file you run.
- README.md: this file.

- Note: nutrition.py imports food_item.py, so keep both files in the same folder.


## 2. Environment setup

- Python 3 (developed and tested on Python 3.12.10).
- Standard library only: no third-party packages and nothing to install. The code uses only Python's built-in functions and string methods; the only import is food_item, from the same folder. There is no requirements.txt because there is nothing to install.
- Tested in Windows PowerShell and Git Bash. Nothing in the code is platform-specific, so it should run in any terminal that has Python 3.

- Note: to check your Python version:
```
python --version
```


## 3. Dataset

This project uses no dataset. The program is interactive: all data is typed in at the prompts. The reference cases are the two worked examples from the assignment (Water and M&M's), reproduced as Examples 1 and 2 in section 9.


## 4. How to run

Open a terminal in the folder that contains food_item.py and nutrition.py, then run:

```
python nutrition.py
```

Note: (On macOS/Linux you may need "python3 nutrition.py")

The program asks for five values in order, prints the nutrition result, then asks whether you want to print the nutrition information for another food item. Answer 'n' to finish.

To stop at any time, press Ctrl+C. Signalling end of input (Ctrl+D in macOS/Linux terminals, Ctrl+Z then Enter in a Windows console) does the same. In both cases the program prints "Input ended unexpectedly. Exiting." and exits cleanly instead of showing an error trace.


## 5. Inputs

The program prompts for these values, in this order:

1. Food item name (string): up to 200 characters, must contain at least one letter, not only digits. Default if left blank: "Water".
2. Grams of fat (float): 0 to 10000, decimals allowed. Default if left blank: 0.00.
3. Grams of carbohydrates (float): 0 to 10000, decimals allowed. Default if left blank: 0.00.
4. Grams of protein (float): 0 to 10000, decimals allowed. Default if left blank: 0.00.
5. Number of servings (float): greater than 0, up to 100000, decimals allowed (e.g. 0.5). Default if left blank: 1.00.
6. Print another food item? (string): y, Y, n or N. No default: a blank answer is asked again.

Note:
- Leading and trailing spaces are ignored.
- Leaving a field blank (by pressing Enter) is a deliberate "skip": the default is used and no error is shown. 
- Typing -0 for fat, carbohydrates or protein is treated as 0 (shown as 0.00 g, never -0.00 g).


## 6. How to read the output

Using Example 2 (below), the result block reads like this:

```
Nutritional information per serving of M&M's:       <- the food item name
Fat: 10.00 g                                        <- grams of fat in ONE serving
Carbohydrates: 34.00 g                              <- grams of carbohydrates in ONE serving
Protein: 2.00 g                                     <- grams of protein in ONE serving
Number of calories for 1.00 serving(s): 234.00      <- always printed: calories in one serving
Number of calories for 3.00 serving(s): 702.00      <- printed only if number of servings is not 1
```

- Calories for one serving (kcal) = 9 x fat + 4 x carbohydrates + 4 x protein (9 kcal per gram of fat, 4 kcal per gram of carbohydrates and protein). For M&M's: 10 x 9 + 34 x 4 + 2 x 4 = 234.
- Calories for N servings (kcal) = calories for one serving x N (234 x 3 = 702). This second line appears only when the number of servings is different from 1; when it is exactly 1 the two lines would be identical, so only one is shown (see Example 1).
- All numbers are shown with two decimal places.
- Unit note: "calories" here follows the assignment's wording and the way food labels use the word. Technically these are kilocalories (kcal), which is what the 9/4/4 factors are defined in.


## 7. Error handling

Every prompt is validated. The rules are:

- Food item name: rejected when it is only digits, has no letters at all, or is longer than 200 characters. Examples: 12345, !!!, 123!
- Fat, carbohydrates, protein: rejected when the text is not plain numeric (contains letters or _), is a malformed number, is negative, or is above 10000. Examples: abc, nan, inf, 1e10, 1_000, 1.2.3, -5, 20000
- Number of servings: rejected for the same reasons as fat, carbohydrates and protein, and also when it is equal to zero or above 100000. Examples: 0, -1, 200000
- Print another food item?: rejected when it is anything other than y, Y, n or N (including blank). Example: maybe

What happens on a rejected entry:

1. The program prints a message naming the exact reason, for example: Invalid fat: 'abc' is not a valid number. Please try again.
2. It asks again, once.
3. If the retry is also invalid, it prints the reason, uses the default value and continues.
4. The Y/N question is different: it has no sensible default, so it keeps asking until it gets a valid answer.

Entries such as nan, inf, 1e10 and 1_000 are rejected on purpose, even though Python's float() would accept them, because they are not what a person means by a plain amount.


## 8. Parameters

There are no command-line options or configuration files. The limits and defaults are constants at the top of the two source files; edit them there if you want different values.

In nutrition.py:

- MAX_NAME_LENGTH = 200: longest accepted food item name.
- MAX_NUTRIENT_GRAMS = 10000: largest accepted grams of fat, carbohydrates or protein.
- MAX_SERVINGS = 100000: largest accepted number of servings.
- MAX_NUM_ATTEMPTS = 2: maximim attempts per input (first entry + one retry). Must be an integer greater than 0.
- DEFAULT_SERVINGS_VALUE = 1.0: default number of servings (used when value is blank, or still invalid after the last attempt).

In food_item.py (also imported by nutrition.py):

- DEFAULT_NAME_ATTRIBUTE_VALUE = "Water": default name in the FoodItem constructor, and what nutrition.py falls back to for the name.
- DEFAULT_NUMERIC_ATTRIBUTE_VALUE = 0.0: default fat, carbohydrates and protein in the FoodItem constructor, and what nutrition.py falls back to for those.

Note: DEFAULT_NAME_ATTRIBUTE_VALUE and DEFAULT_NUMERIC_ATTRIBUTE_VALUE are defined in food_item.py and are imported into nutrition.py, so the two files can't drift apart on what a default food item looks like. DEFAULT_SERVINGS_VALUE has no equivalent in food_item.py (servings is not a FoodItem attribute) and stays local to nutrition.py.


## 9. Working examples

- Five examples, each run with the real program. Text after a prompt's colon is what was typed.
- When Enter is pressed on a blank line, you will see nothing follows the colon. 
- Examples 1 and 2 are the two examples given in the assignment.

- Example 1, Water: everything else left blank. Result: 0.00 calories (1 serving, single line). Shows: assignment example 1, defaults.
- Example 2, M&M's: fat 10.0, carbs 34.0, protein 2.0, 3.0 servings. Result: 234.00 (1 serving), 702.00 (3 servings). Shows: assignment example 2.
- Example 3, Yogurt: fat 2.5, carbs 6, protein 5.5, 0.5 servings. Result: 68.50 (1 serving), 34.25 (0.5 servings). Shows: decimal amounts, fractional servings.
- Example 4, Almonds: fat 14, carbs 6, protein blank, 2 servings. Result: 150.00 (1 serving), 300.00 (2 servings). Shows: one missing value.
- Example 5, Cola: invalid name and invalid fat entries. Result: 156.00 (1 serving). Shows: error handling, retry, defaults.

### Example 1: Water (assignment example 1)

```
Enter the food item name (up to 200 characters, or leave blank to use the default 'Water'): Water
Enter grams of fat (0-10000, or leave blank to use the default of 0.00 g): 
Enter grams of carbohydrates (0-10000, or leave blank to use the default of 0.00 g): 
Enter grams of protein (0-10000, or leave blank to use the default of 0.00 g): 
Enter the number of servings (0-100000, or leave blank to use the default of 1.00 serving(s)): 
Nutritional information per serving of Water:
Fat: 0.00 g
Carbohydrates: 0.00 g
Protein: 0.00 g
Number of calories for 1.00 serving(s): 0.00

Do you want to print the nutrition information for any other food item? 'y/Y' or 'n/N': n
```

### Example 2: M&M's (assignment example 2)

```
Enter the food item name (up to 200 characters, or leave blank to use the default 'Water'): M&M's
Enter grams of fat (0-10000, or leave blank to use the default of 0.00 g): 10.0
Enter grams of carbohydrates (0-10000, or leave blank to use the default of 0.00 g): 34.0
Enter grams of protein (0-10000, or leave blank to use the default of 0.00 g): 2.0
Enter the number of servings (0-100000, or leave blank to use the default of 1.00 serving(s)): 3.0
Nutritional information per serving of M&M's:
Fat: 10.00 g
Carbohydrates: 34.00 g
Protein: 2.00 g
Number of calories for 1.00 serving(s): 234.00
Number of calories for 3.00 serving(s): 702.00

Do you want to print the nutrition information for any other food item? 'y/Y' or 'n/N': n
```


### Example 3: Decimal amounts and a fractional serving

2.5 x 9 + 6 x 4 + 5.5 x 4 = 68.5 calories per serving; half a serving is 34.25.

```
Enter the food item name (up to 200 characters, or leave blank to use the default 'Water'): Yogurt
Enter grams of fat (0-10000, or leave blank to use the default of 0.00 g): 2.5
Enter grams of carbohydrates (0-10000, or leave blank to use the default of 0.00 g): 6
Enter grams of protein (0-10000, or leave blank to use the default of 0.00 g): 5.5
Enter the number of servings (0-100000, or leave blank to use the default of 1.00 serving(s)): 0.5
Nutritional information per serving of Yogurt:
Fat: 2.50 g
Carbohydrates: 6.00 g
Protein: 5.50 g
Number of calories for 1.00 serving(s): 68.50
Number of calories for 0.50 serving(s): 34.25

Do you want to print the nutrition information for any other food item? 'y/Y' or 'n/N': n
```

### Example 4: One missing value

Protein was left blank, so it counts as 0.00 g and simply contributes nothing to the total: 14 x 9 + 6 x 4 + 0 x 4 = 150.

```
Enter the food item name (up to 200 characters, or leave blank to use the default 'Water'): Almonds
Enter grams of fat (0-10000, or leave blank to use the default of 0.00 g): 14
Enter grams of carbohydrates (0-10000, or leave blank to use the default of 0.00 g): 6
Enter grams of protein (0-10000, or leave blank to use the default of 0.00 g): 
Enter the number of servings (0-100000, or leave blank to use the default of 1.00 serving(s)): 2
Nutritional information per serving of Almonds:
Fat: 14.00 g
Carbohydrates: 6.00 g
Protein: 0.00 g
Number of calories for 1.00 serving(s): 150.00
Number of calories for 2.00 serving(s): 300.00

Do you want to print the nutrition information for any other food item? 'y/Y' or 'n/N': n
```

### Example 5: Error handling

- The name 12345 is rejected (digits only); the retry Cola is accepted.
- Fat abc is rejected; the retry nan is also rejected, so fat falls back to 0.00.
- Carbohydrates 39 is valid; protein and servings are left blank (0.00 and 1.00).
- At the final question, maybe is not a valid answer, so it is asked again.
- Calories result: 39 x 4 = 156.

```
Enter the food item name (up to 200 characters, or leave blank to use the default 'Water'): 12345
Invalid name: '12345' is made up entirely of numbers. Please try again.
Enter the food item name (up to 200 characters, or leave blank to use the default 'Water'): Cola
Enter grams of fat (0-10000, or leave blank to use the default of 0.00 g): abc
Invalid fat: 'abc' is not a valid number. Please try again.
Enter grams of fat (0-10000, or leave blank to use the default of 0.00 g): nan
Invalid fat: 'nan' is not a valid number. Using default value 0.00.
Enter grams of carbohydrates (0-10000, or leave blank to use the default of 0.00 g): 39
Enter grams of protein (0-10000, or leave blank to use the default of 0.00 g): 
Enter the number of servings (0-100000, or leave blank to use the default of 1.00 serving(s)): 
Nutritional information per serving of Cola:
Fat: 0.00 g
Carbohydrates: 39.00 g
Protein: 0.00 g
Number of calories for 1.00 serving(s): 156.00

Do you want to print the nutrition information for any other food item? 'y/Y' or 'n/N': maybe
Invalid response: 'maybe' is not 'Y' or 'N'. Please try again.

Do you want to print the nutrition information for any other food item? 'y/Y' or 'n/N': n
```
