from treelib import tree_first, tree_create, tree_print, tree_progenitor

# константа выбора чтения из файла 'f' или командой input 'i'
const_input = 'f'

if const_input == 'f':
    f = open('data_input2.txt', 'r')
    data_input = [line for line in f]
    f.close()
    for n in range(len(data_input)):
        data_input[n] = data_input[n].replace('\n', '')
else:
    data_input = [input()]
    for line in range(int(data_input[0])):
        data_input.append(input())
    data_input.append(input())

chil_fath = {}
input_list = [] # [ [Anna, Nicholaus_I], [.., ..], .. ]
for line in data_input[1:]:
    if line.isdecimal():
        break
    s = line.split()
    chil_fath[s[0]] =s[1]
n_elements = len(chil_fath)
for line in data_input[n_elements+2:]:
    input_list.append(line.split())

tree = tree_create(chil_fath)
tree_print(tree)
print()

for pred, name in input_list:
    print(pred, name, end=' ')
    print(tree_progenitor(tree, pred, name))