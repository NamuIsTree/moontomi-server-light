from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session


class MoontomiSession(Session):
    def __init__(self, session: Session):
        super().__init__()
        self.autoflush = session.autoflush
        self.autocommit = session.autocommit
        self.bind = session.bind

    def insert(self, data):
        super().add(data)
        super().commit()

    def insert_all(self, data: list):
        for d in data:
            super().add(d)
        super().commit()

    def update(self, data):
        super().add(data)
        super().commit()
