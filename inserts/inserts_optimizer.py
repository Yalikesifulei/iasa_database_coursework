def optimize(fname):
    with open(f'./inserts/{fname}.sql', encoding='utf-8') as fin, open(f'./inserts/optimize/{fname}.sql', 'w', encoding='utf-8') as fout:
        inp_lines = fin.readlines()
        for i, line in enumerate(inp_lines):
            val_ind = line.find('VALUES') + 7
            if i == 0:
                fout.write(line.strip()[:val_ind] + '\n')
                fout.write('\t' + line[val_ind:][:-2] + ',\n')
            elif i < len(inp_lines) - 1:
                fout.write('\t' + line[val_ind:][:-2] + ',\n')
            else:
                fout.write('\t' + line[val_ind:])

files = ['faculties', 'chairs', 'teachers', 'groups', 'students', 'subjects', 'schedule', 'mega_session']
for file in files:
    optimize(file)