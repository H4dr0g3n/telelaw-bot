import enum

from sqlalchemy import Column, Integer, String, Text, Date, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LawType(enum.Enum):
    UK_RF = "УК РФ"
    KOAP_RF = "КоАП РФ"


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    laws_name = Column(Enum(LawType), nullable=False)
    article_number = Column(String(255), nullable=False)
    title = Column(String(255))
    text = Column(Text)
    last_modified = Column(Date)

    def __repr__(self):
        return (f"<Article(id={self.id}, laws_name='{self.laws_name}', "
                f"title='{self.title}', text='{self.text}, last_modified='{self.last_modified}')>")
