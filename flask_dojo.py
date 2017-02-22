from models import *
from flask import Flask, request, g, redirect, url_for, \
    render_template

DEBUG = True
DATABASE = 'flask_dojo.db'
USERNAME = 'tomi'

app = Flask(__name__, static_url_path="/templates",
            static_folder="templates")
app.config.from_object(__name__)


def init_db():
    db = CreateDatabase()
    try:
        db.db.connect()
        db.db.create_tables([Counter], safe=True)
        Counter.create(get_counter=0, post_counter=0)
        print("Database connection established.")
    except:
        print("Can't connect to database.\nPlease check your connection.txt file.")


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/request_counter')
def get_request_counter():
    get_update = Counter.update(get_counter=0)


@app.route('/statistics')
def statistics():
    return render_template('main.html')

if __name__ == "__main__":
    init_db()
    app.run()
