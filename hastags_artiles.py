from session import session
from models import Hashtag, Article


def main():
    hashtag = session.query(Hashtag).get(3)
    print(f"Articles with hashtags: {hashtag.name}")
    for article in hashtag.articles:
        print(article.title)

    print("-" * 20)

    for article in session.query(Article):
        print(article.title)
        for hashtag in article.hashtags:
            print(f" #{hashtag.name}")


if __name__ == '__main__':
    main()
