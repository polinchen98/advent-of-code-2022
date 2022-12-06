dataset_buffer = open('input.txt', 'r').read()

for i in range(len(dataset_buffer) - 3):
    window_set = set()
    for j in range(4):
        window_set.add(dataset_buffer[i + j])
    if len(window_set) == 4:
        print(i+4)
        break

for i in range(len(dataset_buffer) - 13):
    window_set = set()
    for j in range(14):
        window_set.add(dataset_buffer[i + j])
    if len(window_set) == 14:
        print(i+14)
        break
