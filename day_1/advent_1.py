elves_calories_items = open('input.txt', 'r')
calories_items_list = elves_calories_items.read().splitlines()

count_calories_per_elf = []
count = 0

for item in calories_items_list:
    try:
        count += int(item)
    except ValueError:
        count_calories_per_elf.append(count)
        count = 0

# first part
max_count_of_calories = max(count_calories_per_elf)

# second part
sum_of_top = sum(sorted(count_calories_per_elf)[-3:])


