from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/posts')
def post_list():
    posts = [
        {'title': 'First Post', 'content': 'This is my first post.'},
        {'title': 'Second Post', 'content': 'This is my second post.'},
        {'title': 'Third Post', 'content': 'This is my third post.'}
    ]
    return render_template('post_list.html', posts=posts)


