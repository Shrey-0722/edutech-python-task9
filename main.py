import os
from datetime import datetime
from math_utils import greet, add, subtract

print(greet  ("Shrey"))
print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Current Date and Time:", datetime.now())
print("Current Working Directory:", os.getcwd())