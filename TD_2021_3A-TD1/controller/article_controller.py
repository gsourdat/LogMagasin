import re

from model.dao.article_dao import ArticleDAO
from exceptions import Error, InvalidData

class ArticleController :
    
    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_articles(self):
        with self._database_engine.new_session() as session:
            articles = ArticleDAO(session).get_all()
            articles_data = [articles.to_dict() for articles in articles]
        return articles_data

    def get_articles(self, member_id):
        with self._database_engine.new_session() as session:
            member = MemberDAO(session).get(member_id)
            member_data = member.to_dict()
        return member_data

    def create_articles(self, data):

        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                member = MemberDAO(session).create(data)
                member_data = member.to_dict()
                return member_data
        except Error as e:
            # log error
            raise e

    def update_articles(self, member_id, member_data):

        self._check_profile_data(member_data, update=True)
        with self._database_engine.new_session() as session:
            member_dao = MemberDAO(session)
            member = member_dao.get(member_id)
            member = member_dao.update(member, member_data)
            return member.to_dict()

    def delete_articles(self, member_id):

        with self._database_engine.new_session() as session:
            member_dao = MemberDAO(session)
            member = member_dao.get(member_id)
            member_dao.delete(member)

    def search_articles(self, firstname, lastname):

        # Query database
        with self._database_engine.new_session() as session:
            member_dao = MemberDAO(session)
            member = member_dao.get_by_name(firstname, lastname)
            return member.to_dict()

   