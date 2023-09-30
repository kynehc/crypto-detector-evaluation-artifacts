with open(f'raw_report.log', 'r') as fd:
    lines = fd.readlines()

data = ''
count = 0
s = 0
for line in lines:
    if 'Data:' in line:
        data = line[len('Data: '):-1]
    elif 'Count:' in line and data == 'rand() without srand()':
        tmp = int(line[len('Count: '):-1])
        if tmp < 5:
            count += tmp

total = count + 328 + 260 + 38 + 137
per = (328 + 260 + 38) / total
print(total, per)