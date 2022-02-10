def first(tree):
    for name in tree:
        s = tree[name]
        if s[0] == '':
            return name


def tree_up(tree, name):
    # количество элементов над NAME
    s = tree[name]
    if s[0] == '':
        return 0
    else:
        return 1 + tree_up(tree, s[0])


def tree_down(tree, name):
    # количество элементов под NAME
    s = tree[name]
    if s[1] == 0:
        return 0
    else:
        big = 0
        for n in s[2:]:
            down = tree_down(tree, n)  # максимальное количество уровней вниз
            if down > big:
                big = down
        return 1 + big


# константа выбора чтения из файла 'f' или командой input 'i'
const_input = 'f'

if const_input == 'f':
    f = open('data_input.txt', 'r')
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
# { потомок : родитель }
for s in data_input[1:]:
    ss = s.split()
    chil_fath[ss[0]] = ss[1]

tree = {}  # { name : ['father', num_children, 'child1', 'child2', ...] }
for name in chil_fath:
    if name not in tree:
        # создание нового элемента, если нет с таким именем
        s = []
        s.append(chil_fath[name])  # РОДИТЕЛЬ
        s.append(0)  # 0 ПОТОМКОВ
        tree[name] = s.copy()
        if chil_fath[name] not in tree:
            # создание нового элемента, если нет и такого родителя
            s = []
            s.append('')  # РОДИТЕЛЬ
            s.append(1)
            s.append(name)
            tree[chil_fath[name]] = s.copy()
        else:
            # добавление информации о потомке, если родитель уже есть
            s = tree[chil_fath[name]]
            s[1] += 1
            s.append(name)
            tree[chil_fath[name]] = s.copy()
    else:
        # добавление информации о родителе
        s = tree[name]
        s[0] = chil_fath[name]
        tree[name] = s.copy()
        if chil_fath[name] not in tree:
            # создание нового элемента, если нет и родителя
            s = []
            s.append('')  # РОДИТЕЛЬ
            s.append(1)
            s.append(name)
            tree[chil_fath[name]] = s.copy()
        else:
            # добавление информации о потомке, если родитель уже есть
            s = tree[chil_fath[name]]
            s[1] += 1
            s.append(name)
            tree[chil_fath[name]] = s.copy()

root = first(tree)
print('корневой родитель: ', root, ' имеет', tree_down(tree, root), 'уровней вниз')

for name in sorted(tree):
    print(name, tree_up(tree, name))