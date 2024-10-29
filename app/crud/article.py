from datetime import date

from sqlalchemy.orm import Session

from app.entity.article import Article, LawType


def create_article(db: Session, laws_name: LawType, article_number: str, title: str, text: str, last_modified: date):
    new_article = Article(
        laws_name=laws_name,
        article_number=article_number,
        title=title,
        text=text,
        last_modified=last_modified
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()


def get_articles_by_law(db: Session, laws_name: str):
    return db.query(Article).filter(Article.laws_name == laws_name).all()


def update_article(db: Session, article_id: int, title: str = None, text: str = None, last_modified: date = None):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        return None
    if title:
        article.title = title
    if text:
        article.text = text
    if last_modified:
        article.last_modified = last_modified
    db.commit()
    db.refresh(article)
    return article


def delete_article(db: Session, article_id: int):
    article = db.query(Article).filter(Article.id == article_id).first()
    if article:
        db.delete(article)
        db.commit()
        return True
    return False
