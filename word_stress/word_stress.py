def num_liter(word_t):
    # вщзвращает количество заглавных букв
    input_word = {w for w in word_t}
    lo_word = {w for w in word_t.lower()}
    big_word = input_word - lo_word
    return len(big_word)


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

st_dict = [data_input[n+1] for n in range(int(data_input[0]))]
text = data_input[-1]
st_dict_lo = {w.lower() for w in st_dict} # словарь без ударений
n_err = 0

for word in text.split():
    if num_liter(word) != 1:
        n_err += 1
        continue
    elif word not in st_dict:
        if word.lower() in st_dict_lo:
            n_err += 1
print(n_err)