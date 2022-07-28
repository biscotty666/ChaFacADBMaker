from createsession import Session, Base, engine
from sqlalchemy import Column, String, Integer, Boolean
import json

class Skill(Base):
  __tablename__ = 'toons_skills'
  Id=Column(Integer(), primary_key=True)
  ToonId=Column(String())
  SkillId=Column(String())
  Tier=Column(Integer())
  NameKey=Column(String())
  IsZeta=Column(Boolean())
  Tiers=Column(Integer())

def create_skills():

  Base.metadata.create_all(engine)

  with open('player.json') as f:
    config = json.load(f)

  roster = config[0]['roster']

  local_session = Session(bind=engine)

  for toon in roster:
    skills = toon['skills']
    for skill in skills:
      new_skill = Skill(ToonId = toon['id'],\
        SkillId = skill['id'],\
        Tier = skill['tier'],\
        NameKey = skill['nameKey'],\
        IsZeta = skill['isZeta'],\
        Tiers = skill['tiers']
      )

      local_session.add(new_skill)

      local_session.commit()
