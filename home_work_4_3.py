numbers = [1, 4, 0, 6, 8, 0, 2]

num = numbers.count(0)

i = 0
while i < num:
        numbers.remove(0)
        # print(numbers)
        i += 1
i = 0
while i < num:
        numbers.append(0)
        # print(numbers)
        i += 1
print(numbers)