from sqlalchemy import Column, Integer, String
from createsession import Session, Base, engine

import json

class Gear(Base):
  __tablename__ = 'toons_gear'
  Id=Column(Integer(), primary_key=True)
  ToonId=Column(String())
  GearId=Column(String())
  Slot=Column(Integer())
  NameKey=Column(String())

def create_gear():
  Base.metadata.create_all(engine)

  with open('player.json') as f:
    config = json.load(f)

  roster = config[0]['roster']

  local_session = Session(bind=engine)

  for toon in roster:
    gears = toon['equipped']
    for gear in gears:
      new_gear = Gear(ToonId = toon['id'],\
        GearId = gear['equipmentId'],\
        Slot = gear['slot'],\
        NameKey = gear['nameKey']
      )
      local_session.add(new_gear)

      local_session.commit()