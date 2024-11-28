from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / 'data' / 'blog_posts.json'


def load_blog_posts() -> list:
    """
    Loads the blog_posts.json file and returns content as a list of dictionaries.
    :return: list[dictionaries]
    """
    with open(DATA_FILE, "r") as handle:
        data = json.load(handle)
    return data


def save_blog_posts(new_content: list[dict]) -> None:
    """
    saves updated list to blog_posts.json
    :return: None
    """
    with open(DATA_FILE, "w") as handle:
        json.dump(new_content, handle, indent=4)


def add_blog_post(author: str, title: str, content: str) -> None:
    """
    Add a new post to blog_posts.json.
    :param author: str
    :param title: str
    :param content: str
    :return: None
    """
    blog_posts = load_blog_posts()
    new_post_dict = {
        "id": len(blog_posts) + 1,
        "author": author,
        "title": title,
        "content": content
    }
    blog_posts.append(new_post_dict)
    with open(DATA_FILE, "w") as handle:
        json.dump(blog_posts, handle, indent=4)
