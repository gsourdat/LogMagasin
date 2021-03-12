from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint


class Article(Base):
    __tablename__ = 'articles'
    __table_args__ = (UniqueConstraint('id',)

    id = Column(String(36), default=generate_id, primary_key=True)

    name = Column(String(50), nullable=False)
    description = Column(String(256), nullable=False)
    type = Column(String(50), nullable=False)
    provenance = Column(String(50), nullable=False)

    
    def __repr__(self):
        return "<Member(%s %s %s)>" % (self.name, self.provenance,self.description, self.type)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description" : self.description,
            "type": self.type
            "provenance" : self.provenance
        }
