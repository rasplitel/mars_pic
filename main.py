from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def begin():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    frases = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!, Присоединяйся!']
    return '</br>'.join(frases)


@app.route('/image_mars')
def mars_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}">
                        <br>
                        Вот она какая, красная планета.
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
