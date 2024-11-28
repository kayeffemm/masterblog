from flask import Flask, render_template, request, redirect
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
    :return: redirect to index.html if Post request or redirect to add.html if GET request
    """
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']
        add_blog_post(author, title, content)
        return redirect('/')

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['GET'])
def delete(post_id):
    """
    Delete a blog post by its ID.
    :param post_id: int
    :return: redirect to index.html
    """
    blog_posts = load_blog_posts()
    updated_posts = [post for post in blog_posts if post['id'] != post_id]

    save_blog_posts(updated_posts)

    return redirect('/')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Fetch the post from the JSON file, update it and redirect back to index
    :param post_id: int
    :return: redirect to index.html if POST request or render update.html template if GET request
    """
    blog_posts = load_blog_posts()
    post_to_update = next((post for post in blog_posts if post['id'] == post_id), None)

    if post_to_update is None:
        return "Post not found", 404

    if request.method == 'POST':
        post_to_update['title'] = request.form['title']
        post_to_update['content'] = request.form['content']
        post_to_update['author'] = request.form['author']

        with open(DATA_FILE, 'w') as handle:
            json.dump(blog_posts, handle, indent=4)

        return redirect('/')

    return render_template('update.html', post=post_to_update)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
