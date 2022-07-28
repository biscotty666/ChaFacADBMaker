from createsession import Session, Base, engine
from sqlalchemy import Column, String, Integer

class Toon(Base):
  __tablename__ = 'player_toons'
  Id = Column(Integer(), primary_key=True)
  ToonId=Column(String())
  PlayerId = Column(String())
  DefId = Column(String())
  NameKey = Column(String())
  Rarity = Column(Integer())
  Level = Column(Integer())
  Xp = Column(Integer())
  Gear = Column(Integer())
  CombatType = Column(Integer())
  Gp = Column(Integer())
  PrimaryUnitStat = Column(String())
  Relic = Column(Integer())


def create_toons():
  import json
  from datetime import datetime

  from pprint import pprint

  Base.metadata.create_all(engine)

  with open('player.json') as f:
    config = json.load(f)

  roster = config[0]['roster']
  local_session = Session(bind=engine)

  for toon in roster:
    relic = toon['relic']
    if toon['relic']==None:
      relic=0

    else:
      relic=toon['relic']['currentTier']

    new_toon = Toon(ToonId=toon['id'],\
      PlayerId = config[0]['id'],\
      DefId = toon['defId'],\
      NameKey = toon['nameKey'],\
      Rarity = toon['rarity'],\
      Level = toon['level'],\
      Xp = toon['xp'],\
      Gear = toon['gear'],\
      CombatType = toon['combatType'],\
      Gp = toon['gp'],\
      PrimaryUnitStat = toon['primaryUnitStat'],\
      Relic = relic,\
    )

    local_session.add(new_toon)

    local_session.commit()