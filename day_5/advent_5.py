stack_dict = {1: ['R', 'G', 'H', 'O', 'S', 'B', 'T', 'N'],
              2: ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
              3: ['Z', 'H', 'V'],
              4: ['M', 'Z', 'J', 'F', 'G', 'H'],
              5: ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
              6: ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
              7: ['T', 'F', 'P', 'L', 'Z'],
              8: ['Q', 'V', 'W', 'S'],
              9: ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']}

rearrangement_procedure = open('input.txt', 'r')
rearrangement_procedure_list = [procedure.split() for procedure in rearrangement_procedure.read().splitlines()]

result_list = []
for procedure in rearrangement_procedure_list:
    result_list.append({procedure[0]: int(procedure[1]),
                        procedure[2]: int(procedure[3]),
                        procedure[4]: int(procedure[5])})


def get_answer(stacks: dict):
    return ''.join([stack[-1] for stack in stacks.values()])


for item in result_list:
    for i in range(item['move'], 0, -1):
        a = stack_dict[item['from']].pop()
        stack_dict[item['to']].append(a)

print(get_answer(stack_dict))

stack_dict_2 = {1: ['R', 'G', 'H', 'O', 'S', 'B', 'T', 'N'],
                2: ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
                3: ['Z', 'H', 'V'],
                4: ['M', 'Z', 'J', 'F', 'G', 'H'],
                5: ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
                6: ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
                7: ['T', 'F', 'P', 'L', 'Z'],
                8: ['Q', 'V', 'W', 'S'],
                9: ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']}

for item in result_list:
    stack_dict_2[10] = []
    for i in range(item['move'], 0, -1):
        last_elem = stack_dict_2[item['from']].pop()
        stack_dict_2[10].append(last_elem)

    for i in range(len(stack_dict_2[10])):
        a = stack_dict_2[10].pop()
        stack_dict_2[item['to']].append(a)

stack_dict_2.pop(10)

print(get_answer(stack_dict_2))
