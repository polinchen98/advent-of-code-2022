assignment_pairs = open('input.txt', 'r')
assignment_pairs_list = assignment_pairs.read().splitlines()

list_with_pairs = list(map(lambda pair: pair.split(','), assignment_pairs_list))


def is_subset_sets(list_with_sets):
    if list_with_sets[0].issubset(list_with_sets[1]) or list_with_sets[1].issubset(list_with_sets[0]):
        return True


def is_intersection_sets(list_with_sets):
    if list_with_sets[0].intersection(list_with_sets[1]) or list_with_sets[1].intersection(list_with_sets[0]):
        return True


count_part_1 = 0
count_part_2 = 0
for item in list_with_pairs:
    x = list(map(lambda pair: pair.split('-'), item))
    y = [[int(digit) for digit in pair] for pair in x]
    z = [set(range(pair[0], pair[1]+1)) for pair in y]
    if is_intersection_sets(z):
        count_part_2 += 1
    if is_subset_sets(z):
        count_part_1 += 1

print(count_part_1)
print(count_part_2)
