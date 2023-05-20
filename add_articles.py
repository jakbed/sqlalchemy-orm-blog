from models import Author, Article
from session import session
from faker import Faker


def main():
    author = session.query(Author).get(12)
    fake = Faker()
    article = Article(
        title=fake.sentence(),
        content=fake.sentence(),
    )

    author.articles.append(article)
    session.commit()


if __name__ == '__main__':
    main()
