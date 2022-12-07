terminal_output = open('input.txt', 'r')
terminal_output_list = terminal_output.read().splitlines()


class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []
        self.parent = None
        self.isFile = False

    def add_new_dir(self, dir_name):
        child = Node(dir_name)
        child.parent = self
        self.children.append(child)

    def add_new_file(self, file_name, size):
        child = Node(file_name, size)
        child.parent = self
        child.isFile = True
        self.children.append(child)

    def get_dir(self, name_dir):
        return list(filter(lambda child: child.name == name_dir, self.children))[0]


root = Node('/')
current_dir = root
for i in range(1, len(terminal_output_list)):
    if '$ cd' in terminal_output_list[i] and 'cd ..' not in terminal_output_list[i]:
        current_dir = current_dir.get_dir(terminal_output_list[i].split()[-1])
    if '$ cd ..' in terminal_output_list[i]:
        current_dir = current_dir.parent
    if 'dir ' in terminal_output_list[i]:
        current_dir.add_new_dir(terminal_output_list[i].split()[-1])
    if terminal_output_list[i][0].isdigit():
        current_dir.add_new_file(terminal_output_list[i].split()[1], int(terminal_output_list[i].split()[0]))


def count_size(node: Node) -> int:
    if node.isFile:
        return node.size

    count = 0
    for child in node.children:
        count += count_size(child)
    node.size = count
    return count


def get_first_answer(node: Node) -> int:
    summa = 0
    if node.size <= 100000 and not node.isFile:
        summa += node.size
    for child in node.children:
        summa += get_first_answer(child)
    return summa


def get_second_answer(node: Node, general: int) -> int:
    result = 30000000
    unused_space = 70000000 - general  # 22557601
    to_delete = 30000000 - unused_space
    for child in node.children:
        if child.size >= to_delete and not child.isFile:
            result = min(get_second_answer(child, general), result, child.size)
    return result


all_memory = count_size(root)
print(get_first_answer(root))
print(get_second_answer(root, all_memory))

