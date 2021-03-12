from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.article import Article
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class ArticleDAO(DAO):
    """
    Article Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Article).filter_by(id=id).order_by(Member.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Article).order_by(Member.name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, name: str):
        try:
            return self._database_session.query(Aticle).filter_by(name=name)\
                .order_by(Article.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            article = Article(name=data.get('name'), type=data.get('type'), description=data.get('description'), provenance=data.get('provenance'))
            self._database_session.add(article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Article already exists")
        return article

    def update(self, article: Article, data: dict):
        if 'name' in data:
            article.name = data['name']
        if 'type' in data:
            article.type = data['type']
        if 'provenance' in data:
            article.provenance = data['provenance']
        if 'description' in data:
            article.description = data['description']
        try:
            self._database_session.merge(article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return article

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
