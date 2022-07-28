from createsession import Session, Base, engine
from sqlalchemy import Column, String, Integer, DateTime
import json
from datetime import datetime

class Player(Base):
  __tablename__ = 'player'
  Id = Column(Integer(), primary_key=True)
  PlayerId = Column(String())
  AllyCode = Column(Integer())
  Name = Column(String(), nullable=False, unique=True)
  Level = Column(Integer())
  GuildRefId = Column(String())
  GuildName = Column(String())
  GuildBannerColor = Column(String())
  GuildBannerLogo = Column(String())
  GuildTypeId = Column(String())
  GrandArenaLifeTime = Column(Integer())
  Updated = Column(Integer())
  TimeStamp = Column(DateTime(), default=datetime.now)

def create_player():
  Base.metadata.create_all(engine)

  with open('player.json') as f:
    config = json.load(f)

  config = config[0]
  local_session = Session(bind=engine)

  new_player = Player(PlayerId = config['id'],\
      Name = config['name'],\
      AllyCode = config['allyCode'],\
      Level = config['level'],\
      GuildRefId = config['guildRefId'],\
      GuildName = config['guildName'],\
      GuildBannerColor = config['guildBannerColor'],\
      GuildBannerLogo = config['guildBannerLogo'],\
      GuildTypeId = config['guildTypeId'],\
      GrandArenaLifeTime = config['grandArenaLifeTime'],\
      Updated = config['updated']
  )

  local_session.add(new_player)

  local_session.commit()