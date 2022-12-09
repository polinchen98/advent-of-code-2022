greed_of_trees = open('input.txt', 'r')
greed_example = [[int(tree) for tree in line] for line in greed_of_trees.read().splitlines()]


def check_tree(trees_array: list, current_i: int, current_j: int):
    i = current_i
    j = current_j
    while trees_array[current_i][current_j] > trees_array[i+1][current_j]:
        i += 1
        if i == len(trees_array)-1:
            return True

    i = current_i
    j = current_j
    while trees_array[current_i][current_j] > trees_array[i-1][current_j]:
        i -= 1
        if i == 0:
            return True

    i = current_i
    j = current_j
    while trees_array[current_i][current_j] > trees_array[current_i][j+1]:
        j += 1
        if j == len(trees_array[0])-1:
            return True

    i = current_i
    j = current_j
    while trees_array[current_i][current_j] > trees_array[current_i][j-1]:
        j -= 1
        if j == 0:
            return True
    return False


visible_trees = 0
for i in range(1, len(greed_example) - 1):
    for j in range(1, len(greed_example[i]) - 1):
        if check_tree(greed_example, i, j):
            visible_trees += 1


round_trees = len(greed_example[0]) * 4 - 4

print(visible_trees + round_trees)


def count_tree_on_top(trees_array: list, current_i: int, current_j: int):
    i = current_i
    count = 0
    while i > 0 and trees_array[current_i][current_j] >= trees_array[i-1][current_j]:
        i -= 1
        count += 1
        if trees_array[current_i][current_j] == trees_array[i][current_j]:
            break
    return count


def count_tree_on_down(trees_array: list, current_i: int, current_j: int):
    i = current_i
    count = 0
    while i < len(trees_array)-1 and trees_array[current_i][current_j] >= trees_array[i+1][current_j]:
        i += 1
        count += 1
        if trees_array[current_i][current_j] == trees_array[i][current_j]:
            break
    return count


def count_tree_on_left(trees_array: list, current_i: int, current_j: int):
    j = current_j
    count = 0
    while j > 0 and trees_array[current_i][current_j] >= trees_array[current_i][j-1]:
        j -= 1
        count += 1
        if trees_array[current_i][current_j] == trees_array[current_i][j]:
            break
    return count


def count_tree_on_right(trees_array: list, current_i: int, current_j: int):
    j = current_j
    count = 0
    while j < len(trees_array[0])-1 and trees_array[current_i][current_j] >= trees_array[current_i][j+1]:
        j += 1
        count += 1
        if trees_array[current_i][current_j] == trees_array[current_i][j]:
            break
    return count


max_count = 0
for i in range(len(greed_example)):
    for j in range(len(greed_example[i])):
        top = count_tree_on_top(greed_example, i, j)
        down = count_tree_on_down(greed_example, i, j)
        left = count_tree_on_left(greed_example, i, j)
        right = count_tree_on_right(greed_example, i, j)
        result = top*down*left*right
        if result > max_count:
            max_count = result

print(max_count)
