# библиотека по работе с древовидной системой данных
# tree =  { name : ['father', num_children, 'child1', 'child2', ...] }
# chil_fath = { 'child' : 'father' }


def tree_first(tree):
    # возвращает имя корневого элемента
    for name in tree:
        s = tree[name]
        if s[0] == '':
            return name

def tree_create(chil_fath):
    # возвращает дерево в формате tree по словарю в формате chil_fath
    tree = {}
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
    return tree

def tree_progenitor(tree, pred, name):
    # является ли name предком pred в дереве tree
    # возврвщает 0-если нет и 1-если да
    s = tree[name]
    if s[0] == '':
        return 0
    elif s[0] == pred:
        return 1
    else:
        return tree_progenitor(tree, pred, s[0])


def tree_print(tree):
    for name in sorted(tree):
        line = tree[name]
        childrens = line[2:]
        print(line[0], '**'+name+'**', '('+str(line[1])+')', end='  ')
        for ch in childrens:
            print(ch, end=', ')
        print()