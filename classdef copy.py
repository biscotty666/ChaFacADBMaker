from curses import echo
from email.policy import default
from sqlalchemy.orm import declarative_base, sessionmaker, relationships
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, create_engine

from datetime import datetime
import os

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.relpath(__file__))
connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'cfa.db')
engine = create_engine(connection_string, echo=True)

Session = sessionmaker()

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

class ModStat(Base):
  __tablename__ = 'mods_stats'
  Id=Column(Integer(), primary_key=True)
  ModId=Column(String())
  UnitStat=Column(Integer())
  Value=Column(Integer())
  Roll=Column(Integer())
  StatType=Column(String())
  
class Gear(Base):
  __tablename__ = 'toons_gear'
  Id=Column(Integer(), primary_key=True)
  ToonId=Column(String())
  GearId=Column(String())
  Slot=Column(Integer())
  NameKey=Column(String())

class Skill(Base):
  __tablename__ = 'toons_skills'
  Id=Column(Integer(), primary_key=True)
  ToonId=Column(String())
  SkillId=Column(String())
  Tier=Column(Integer())
  NameKey=Column(String())
  IsZeta=Column(Boolean())
  Tiers=Column(Integer())
  
