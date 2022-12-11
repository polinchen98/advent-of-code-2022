import itertools

signal_strengths = [x.split() for x in open("input.txt").readlines()]

cycle = 0
x = 1
result = []

for signal in signal_strengths:
    if signal[0] == 'noop':
        cycle += 1
        if cycle in {20, 60, 100, 140, 180, 220}:
            result.append(cycle * x)
    elif signal[0] == 'addx':
        cycle += 1
        if cycle in {20, 60, 100, 140, 180, 220}:
            result.append(cycle * x)
        cycle += 1
        if cycle in {20, 60, 100, 140, 180, 220}:
            result.append(cycle * x)
        x += int(signal[1])

print(sum(result))

# ---

signal_strengths = list(itertools.chain(*[x.replace('\n', '').split() for x in open("input.txt").readlines()]))

thresholds = [20, 60, 100, 140, 180, 220]

x = 1
result = []

for index, value in enumerate(signal_strengths):
    cycle = index + 1

    if cycle in thresholds:
        result.append(x * cycle)

    if value.isdigit() or '-' in value:
        x += int(value)


print(sum(result))

