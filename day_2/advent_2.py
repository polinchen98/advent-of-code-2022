strategy_guide = open('input.txt', 'r')
strategy_guide_list = strategy_guide.read().splitlines()

score_round_part_1 = {'A X': 3, 'B Y': 3, 'C Z': 3, 'A Z': 0, 'B X': 0, 'C B': 0, 'C Y': 0, 'A Y': 6, 'C X': 6, 'B Z': 6}
score_shape_part_1 = {'X': 1, 'Y': 2, 'Z': 3}

result_score_part_1 = 0
for item in strategy_guide_list:
    result_score_part_1 += score_shape_part_1[item[2]]
    result_score_part_1 += score_round_part_1[item]

print(result_score_part_1)

score_round_part_2 = {'A X': 0, 'B X': 0, 'C X': 0, 'B Y': 3, 'C Y': 3, 'A Y': 3, 'C Z': 6, 'A Z': 6, 'B Z': 6}
score_shape_part_2 = {'rock': 1, 'paper': 2, 'scissors': 3}

result_score_part_2 = 0
for item in strategy_guide_list:
    result_score_part_2 += score_round_part_2[item]
    # to end in a draw
    if score_round_part_2[item] == 3 and item[0] == 'A':
        result_score_part_2 += score_shape_part_2['rock']
    if score_round_part_2[item] == 3 and item[0] == 'B':
        result_score_part_2 += score_shape_part_2['paper']
    if score_round_part_2[item] == 3 and item[0] == 'C':
        result_score_part_2 += score_shape_part_2['scissors']
    # lose
    if score_round_part_2[item] == 0 and item[0] == 'A':
        result_score_part_2 += score_shape_part_2['scissors']
    if score_round_part_2[item] == 0 and item[0] == 'B':
        result_score_part_2 += score_shape_part_2['rock']
    if score_round_part_2[item] == 0 and item[0] == 'C':
        result_score_part_2 += score_shape_part_2['paper']
    # win
    if score_round_part_2[item] == 6 and item[0] == 'A':
        result_score_part_2 += score_shape_part_2['paper']
    if score_round_part_2[item] == 6 and item[0] == 'B':
        result_score_part_2 += score_shape_part_2['scissors']
    if score_round_part_2[item] == 6 and item[0] == 'C':
        result_score_part_2 += score_shape_part_2['rock']

print(result_score_part_2)
