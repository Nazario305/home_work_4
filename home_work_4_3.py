import random

NUMS_SIZE = random.randint(3,10)
numbers = []
# print(NUMS_SIZE)
#
for i in range(NUMS_SIZE):
    numbers.append(random.randint(1, 10))
#
print(numbers, 'Результат ->')
result = [numbers[0], numbers[2], numbers[-2]]
print(result)