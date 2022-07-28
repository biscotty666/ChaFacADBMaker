from sqlalchemy import Column, Integer, String
from createsession import Session, Base, engine
import json

class ModStat(Base):
  __tablename__ = 'mods_stats'
  Id=Column(Integer(), primary_key=True)
  ModId=Column(String())
  UnitStat=Column(Integer())
  Value=Column(Integer())
  Roll=Column(Integer())
  StatType=Column(String())

def create_mod_stats():
  Base.metadata.create_all(engine)

  with open('player.json') as f:
    config = json.load(f)

  roster = config[0]['roster']

  local_session = Session(bind=engine)

  for toon in roster:
    mods = toon['mods']
    for mod in mods:
      pstats = mod['primaryStat']
      new_mod_stat = ModStat(ModId = mod['id'],\
        UnitStat = pstats['unitStat'],\
        Value = pstats['value'],\
        StatType = 'P'
      )
      local_session.add(new_mod_stat)
      local_session.commit

      for modstat in mod['secondaryStat']:
        new_mod_stat = ModStat(ModId = mod['id'],\
          UnitStat = modstat['unitStat'],\
          Value = modstat['value'],\
          Roll = modstat['roll'],\
          StatType = 'S'
        )

        local_session.add(new_mod_stat)
        local_session.commit()