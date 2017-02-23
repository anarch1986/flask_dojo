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
        db.db.drop_tables([Counter], safe=True)
        db.db.create_tables([Counter], safe=True)
        Counter.create(get_counter=0, post_counter=0)
        print("Database connection established.")
    except:
        print("Can't connect to database.\nPlease check your connection.txt file.")


@app.route('/')
def main():
    return render_template('main.html', mode=None)


@app.route('/request_counter')
def get_request_counter():
    get_update = Counter.update(
        get_counter=Counter.get_counter + 1).where(Counter.id == 1)
    get_update.execute()
    return render_template('main.html', mode="get_request")


@app.route('/request_counter', methods=['POST'])
def post_request_counter():
    post_update = Counter.update(
        post_counter=Counter.post_counter + 1).where(Counter.id == 1)
    post_update.execute()
    return render_template('main.html', mode="post_request")


@app.route('/statistics')
def statistics():
    counter = Counter.get()
    return render_template('main.html', mode="statistics", counter=counter)

if __name__ == "__main__":
    init_db()
    app.run()
