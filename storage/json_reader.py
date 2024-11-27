import json


def load_blog_posts() -> list:
    """
    Loads the blog_posts.json file and returns content as a list of dictionaries.
    :return: list[dictionaries]
    """
    with open('../data/blog_posts.json', "r") as handle:
        data = json.load(handle)
    return data

