from sqlalchemy import Column, String, Integer
from createsession import Session, Base, engine
import json

class Mod(Base):
  __tablename__ = 'toons_mods'
  Id=Column(Integer(), primary_key=True)
  ToonId=Column(String())
  ModId=Column(String())
  Level=Column(Integer())
  Tier=Column(Integer())
  Slot=Column(Integer())
  Set=Column(Integer())
  Pips=Column(Integer())

def create_mods():
  Base.metadata.create_all(engine)

  with open('player.json') as f:
    config = json.load(f)

  roster = config[0]['roster']

  local_session = Session(bind=engine)

  for toon in roster:
    mods = toon['mods']
    for mod in mods:
      new_mod = Mod(ToonId = toon['id'],\
        ModId = mod['id'],\
        Level = mod['level'],\
        Tier = mod['tier'],\
        Slot = mod['slot'],\
        Set = mod['set'],\
        Pips = mod['pips'],\
      )
      local_session.add(new_mod)

      local_session.commit()