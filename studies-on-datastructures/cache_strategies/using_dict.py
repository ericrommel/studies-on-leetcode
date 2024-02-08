# https://realpython.com/lru-cache-python/
import requests

cache = dict()


def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text


def get_article(url):
    print("Getting article...")
    if url not in cache:
        print("Not in cache. Adding it...")
        cache[url] = get_article_from_server(url)

    return cache[url]


get_article("https://realpython.com/sorting-algorithms-python/")
print("Getting same article...")
get_article("https://realpython.com/sorting-algorithms-python/")
