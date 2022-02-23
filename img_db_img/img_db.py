import os
import sqlite3
from flask import Flask, render_template, url_for, make_response, request

app = Flask(__name__)

def read_imgfile(path, filename):
    # Принимает имя файла, читает его в папке path
    # Возвразает картинку в бинарном виде для записи в БД

    try:
        f = open(os.path.join(path, filename), 'rb')
        # Получаем бинарные данные нашего файла
        img = f.read()
        # Конвертируем данные
        dat = sqlite3.Binary(img)  # у меня работает и без нее
        f.close()
        return dat
    except FileNotFoundError as e:
        print('файл не найден: ' + str(e))
        return False


def save_imgfile(img, path, filename):
    # Принимает изображение в бинарном виде, полученное из БД в ячейке BLOB, путь и имя файла
    # Записывает его в папку static с именем filename
    # Возвращает True или False в зависимости от успеха

    try:
        f = open(os.path.join(path, filename), 'wb')
        # записываем картинку в файл
        f.write(img)
        f.close()
        return True
    except FileNotFoundError as e:
        print('файл не найден: ' + str(e))
        return False


def read_db(id):
    # Принимает значение id строки из которой читается изображение из БД test_db, таблицы images
    # Возвращает изображение или False, eсли id не найден

    with sqlite3.connect("test.db") as con:
        # или так:  con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS images(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    avatar BLOB)""")
        # считываем из базы аватар в строке с id
        cur.execute(f"SELECT avatar FROM Images WHERE id = {id}")
        s = cur.fetchone()  # возвращает картеж
        img = s[0]  # берем 0 элемент картежа
    if img:
        return img
    else:
        return False


def save_db(img, id='no'):
    # Принимает изображение
    # Если нет id, добавляет новую строку в БД test.db таблицы images
    # Если есть id, обновляет изображение в БД в строке с id

    dat = sqlite3.Binary(img)
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS images(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    avatar BLOB)""")
        if id == 'no':
            # добавляем новую строку в базу
            cur.execute("INSERT INTO Images(avatar) VALUES (?)", (dat,))
        else:
            # изменяем аватарку в строке с id
            cur.execute("UPDATE Images SET avatar = ? WHERE id = ?", (dat, id))
        con.commit()
    return

@app.route("/", methods=["POST", "GET"])
def index():
    print(url_for('index'))
    if request.method == "POST":
        # получены данные методом POST
        print('получены данные методом POST')
        if request.files:
            # есть переданный файл
            print('есть переданный файл')
            f = request.files['file']
            print(f)
            print(f.headers) # заголовок который пришел с файлом
            print(f.name)  # имя аргумента переданного файла 'file'
            print(f.filename) # имя переданного файла
            print(f.content_type) # тип файла
            if f.filename:
                try:
                    img = f.read() # читает изображение
                    ext = f.filename.split('.')[1] # выбирает расширение
                    f = open(os.path.join('static\images', 'insert_img.'+ext), 'wb')
                    f.write(img)
                    f.close()
                    return render_template('index.html', ext=ext)
                except FileNotFoundError as e:
                    print('Ошибка чтения файла'+str(e))

    return render_template('index.html')

@app.route("/userava")
def userava():
    img = read_db(2)
    h = make_response(img)
    #h.headers['Content-Type'] = 'image/png'
    return h


#img = read_imgfile('static\images', '2.jpg')
#save_db(img, 2)
#img = read_db(2)
#save_imgfile(img, 'static', '2_new.jpg')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)