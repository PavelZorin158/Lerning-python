import os
import sqlite3

try:
    f = open(os.path.join('static\images', '2.jpg'), 'rb')
    # Получаем бинарные данные нашего файла
    img = f.read()
    # Конвертируем данные
    dat = sqlite3.Binary(img) # у меня работает и без нее
    f.close()
except FileNotFoundError as e:
    print('файл не найден: '+str(e))

with sqlite3.connect("test.db.db") as con:
    # или так:  con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS images(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                avatar BLOB)""")
    #cur.execute("INSERT INTO Images(avatar) VALUES (?)", (dat,)) # добавляем новую строку в базу
    id = 1
    cur.execute("UPDATE Images SET avatar = ? WHERE id = ?", (dat, id)) # изменяем аватарку в строке с id
    con.commit()

    cur.execute("SELECT avatar FROM Images WHERE id = 1") # считываем из базы аватар в строке с id=1
    s = cur.fetchone() # возвращает картеж
    img = s[0] # берем 0 элемент картежа

f = open(os.path.join('static', '2_new.jpg'), 'wb')
# записываем картинку в файл
f.write(img)
f.close()