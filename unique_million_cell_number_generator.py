# write unique million cell numbers into file
import random
import sys
# writing to file
sys.stdout = open("unique_million_cell_numbers.txt", "w")


# random cell numbers generator with pointers and limit for performance
cell_numbers = []
while len(cell_numbers) < 1004000:
    num1 = 0
    num2 = random.randint(6, 7)
    num3 = random.randint(1, 9)
    num4 = random.randint(0, 9)
    num5 = random.randint(0, 9)
    num6 = random.randint(0, 9)
    num7 = random.randint(0, 9)
    num8 = random.randint(0, 9)
    num9 = random.randint(0, 9)
    num10 = random.randint(0, 9)
    num = (num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
    cell_numbers.append(num)
unique_numbers = set(cell_numbers)


# unique million cell numbers selector
million_numbers = []
for item in unique_numbers:
    if len(million_numbers) < 10**6:
        million_numbers.append(item)


# print unique million cell numbers into file
for cell_num in million_numbers:
    print(*cell_num, sep="")

sys.stdout.close()
