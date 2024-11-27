from flask import Flask, render_template
from storage.json_reader import load_blog_posts

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_blog_posts()
    return render_template('index.html', posts = blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)