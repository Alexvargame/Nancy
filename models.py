from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker, scoped_session, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = create_engine('sqlite:///nancy.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Player(Base):
    __tablename__ = 'player'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    pl_items = relationship('Item', cascade='all,delete',back_populates='player')
    status = mapped_column(String, nullable=False,default='new')
    save_location = mapped_column(String, default= 'locations.location_1')
    balance = mapped_column(Integer, default=0)

    def __str__(self):
        return self.name

    @classmethod
    def add(cls, name):
        player = cls(name=name)
        session.add(player)
        session.commit()
        return player

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()


    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def change_location(cls, name, loc):
        print(loc)
        player = session.query(cls).filter_by(name=name).first()
        player.save_location = loc
        session.commit()
        return player

    # @classmethod
    # def delete_by_id(cls, user_id):
    #     user = session.query(cls).filter_by(id=user_id).first()
    #     if user:
    #         session.delete(user)
    #         session.commit()
    #         return True
    #     return False


class Type_Item(Base):
    __tablename__ = 'types_item'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    items = relationship('Item', cascade='all,delete', back_populates='type')

    def __str__(self):
        return self.name

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def add(cls, name):
        type_item = cls(name=name)
        session.add(type_item)
        session.commit()
        return type_item


class Item(Base):

    __tablename__ = 'item'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    type_id = mapped_column(Integer, ForeignKey('types_item.id'))
    player_id = mapped_column(Integer, ForeignKey('player.id'))
    type = relationship('Type_Item', back_populates='items', foreign_keys=[type_id])
    player = relationship('Player', back_populates='pl_items', foreign_keys=[player_id])
    description = mapped_column(String, nullable=True)
    count = mapped_column(Integer, default=1)
    status = mapped_column(String, default='new')

    def __str__(self):
        return f'{self.name}-{self.player}'
    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_by_player(cls, player, type_id):
        return session.query(cls).filter_by(player=player, type_id=type_id).first()
    @classmethod
    def add(cls, name, player, type, description):
        print(player, type)
        item = cls(name=name, player=player, type=type, description=description )
        session.add(item)
        session.commit()
        return item

    @classmethod
    def change_count(cls, type_id, count):
        print(type_id, count)
        item = session.query(cls).filter_by(type_id=type_id).first()
        if item.count > 0:
            item.count += count
        session.commit()
        return item

Base.metadata.create_all(engine)