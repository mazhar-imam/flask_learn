from flask import Flask, render_template

app = Flask(__name__)


posts = [

    {
        'author':  'Corey Schafer',
        'title': 'Bog Post 1',
        'content': 'First post content',
        'date_posted': 'april 20, 2018'
    },
    {

        'author':  'jane Doe',
        'title': 'Bog Post 2',
        'content': 'Second post content',
        'date_posted': 'april 21, 2018'
    }

]




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')
