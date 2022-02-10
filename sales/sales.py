# константа выбора чтения из файла 'f' или командой input 'i'
const_input = 'f'

if const_input == 'f':
    f = open('data_input.txt', 'r')
    data_input = [line for line in f]
    f.close()
    for n in range(len(data_input)):
        data_input[n] = data_input[n].replace('\n', '')
else:
    data_input = []
    for n in range(int(input('введите количество записей: '))):
        data_input.append(input('введите запись '+str(n+1)+' : '))

# data_input = [ покупатель, продукт, количество ]

data_base = {}
# data_base - вложенный словарь
# data_base = {'Ivanov': {'paper': 17, 'marker': 3, 'envelope': 5}, 'Petrov': {'pens': 5, 'envelope': 20}}

product = {}

for line in data_input:
    line_list = line.split() # ['покупатель','продукт','количество']
    if line_list[0] in data_base:
        # уже есть такой покупатель
        product.clear()
        product = data_base[line_list[0]]
        if line_list[1] in product:
            # уже есть такой продукт у покупателя
            product[line_list[1]] += int(line_list[2])
        else:
            # еще нет такого продукта
            product[line_list[1]] = int(line_list[2])
        data_base[line_list[0]] = product.copy()
    else:
        # еще нет такого покупателя
        product.clear()
        product[line_list[1]] = int(line_list[2])
        data_base[line_list[0]] = product.copy()

for name in sorted(data_base):
    print(name)
    product.clear()
    product = data_base[name].copy()
    for product_name in sorted(data_base[name]):
        print(' ', product_name, product[product_name])