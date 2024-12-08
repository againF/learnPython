import math
import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

result = math.sqrt(num1) + math.sqrt(num2)
print(f"num1: {num1}, num2: {num2}")
print(f"useMath.py result: {result:.4f}")