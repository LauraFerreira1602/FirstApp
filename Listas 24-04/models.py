from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:///db_session.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Usuario(Base):
    __tablename__ = 'TAB_USUARIOS'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    profissao = Column(String, nullable=False)
    salario = Column(String, nullable=False)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_usuario(self):
        dados_usuario = {
            "Nome": self.nome,
            "profissao": self.profissao,
            "Salario": self.salario
        }

        return dados_usuario

class Livro(Base):
    __tablename__ = 'TAB_LIVROS'
    id = Column(Integer, primary_key=True)
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