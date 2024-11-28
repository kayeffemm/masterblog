from flask import Flask, render_template, request
from werkzeug.utils import redirect

from storage.json_reader import *

app = Flask(__name__)


@app.route('/')
def index():
    """
    Adds all posts from blog_posts.json to the index.html.
    :return: index.html with blog posts added.
    """
    blog_posts = load_blog_posts()
    return render_template('index.html', posts = blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handle Post request, create a new blog post with data from user.
    After this redirects user to index.html
    :return: redirect to index.html
    """
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']
        add_blog_post(author, title, content)
        return redirect('/')

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
