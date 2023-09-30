from collections import defaultdict

rules = ['1', '2', '3', '4', '5', '6-1', '6-2']

for file in [f'Rule-{filename}.md' for filename in rules]:
    with open(file, 'r') as fd:
        lines = fd.readlines()
    print(f'--------------{file}--------------')
    cur_pattern = 0
    raw_misuses = defaultdict(int)
    reported_misuses = defaultdict(int)
    grouped_misuses = defaultdict(int)
    for line in lines:
        if line.startswith('# '):
            cur_pattern = 0
        if cur_pattern == 0 and line.startswith('Pattern:'):
            cur_pattern = f'Pattern-{line[len("Pattern: "):-1]}'
            grouped_misuses[cur_pattern] += 1
        elif line.startswith('Count:'):
            reported_misuses[cur_pattern] += 1
            raw_misuses[cur_pattern] += int(line[len('Count: '):-1])
    print(dict(raw_misuses), f'Total: {sum(raw_misuses.values())}')
    print(dict(reported_misuses), f'Total: {sum(reported_misuses.values())}')
    print(dict(grouped_misuses), f'Total: {sum(grouped_misuses.values())}')