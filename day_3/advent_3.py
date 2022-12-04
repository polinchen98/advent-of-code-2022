import string
import re

rucksacks_content = open('input.txt', 'r')
rucksacks_content_list = rucksacks_content.read().splitlines()

alphabet_lowercase = list(string.ascii_lowercase)
priority_lowercase_letters = {}
for i in range(len(alphabet_lowercase)):
    priority_lowercase_letters[alphabet_lowercase[i]] = i + 1

alphabet_uppercase = list(string.ascii_uppercase)
priority_uppercase_letters = {}
for i in range(len(alphabet_uppercase)):
    priority_uppercase_letters[alphabet_uppercase[i]] = i + 27

common_items = []
for line in rucksacks_content_list:
    mid = len(line) // 2
    compartment_1 = line[:mid]
    compartment_2 = line[mid:]
    for i in range(mid):
        if compartment_1[i] in compartment_2:
            common_items.append(compartment_1[i])
            break

count_priority = 0
for item in common_items:
    if re.search('[a-z]', item):
        count_priority += priority_lowercase_letters[item]
    if re.search('[A-Z]', item):
        count_priority += priority_uppercase_letters[item]

print(count_priority)

common_items_part_2 = []
for i in range(0, len(rucksacks_content_list) - 2, 3):
    group = [rucksacks_content_list[i], rucksacks_content_list[i+1], rucksacks_content_list[i+2]]
    for j in range(len(group)-2):
        for letter in group[0]:
            if letter in group[j+1] and letter in group[j+2]:
                common_items_part_2.append(letter)
                break

count_priority_part_2 = 0
for item in common_items_part_2:
    if re.search('[a-z]', item):
        count_priority_part_2 += priority_lowercase_letters[item]
    if re.search('[A-Z]', item):
        count_priority_part_2 += priority_uppercase_letters[item]

print(count_priority_part_2)
