from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:///Livros.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Livro(Base):
    __tablename__ = 'TAB_LIVROS'
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False, unique=True)
    categoria = Column(String, nullable=False)
    autor = Column(String, nullable=False)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_livro(self):
        dados_livro = {
            "Titulo": self.titulo,
            "Descricao": self.descricao,
            "Categoria": self.categoria,
            "Autor": self.autor
        }

        return dados_livro


def init_db():
    Base.metadata.create_all(engine)

    if __name__ == '__main__':
        init_db()