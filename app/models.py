"""
Models
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()


class Record(Base):
    """
    Record Model
    """
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    workclass_id = Column(Integer, ForeignKey('workclasses.id'))
    education_level_id = Column(Integer, ForeignKey('education_levels.id'))
    marital_status_id = Column(Integer, ForeignKey('marital_statuses.id'))
    occupation_id = Column(Integer, ForeignKey('occupations.id'))
    relationship_id = Column(Integer, ForeignKey('relationships.id'))
    race_id = Column(Integer, ForeignKey('races.id'))
    sex_id = Column(Integer, ForeignKey('sexes.id'))
    country_id = Column(Integer, ForeignKey('countries.id'))
    age = Column(Integer)
    education_num = Column(Integer)
    capital_gain = Column(Integer)
    capital_loss = Column(Integer)
    hours_week = Column(Integer)
    over_50k = Column(Boolean)

    @property
    def serialize(self):
        """serialize the object"""
        return {
            'id': self.id,
            'age': self.age,
            'education_num': self.education_num,
            'capital_gain': self.capital_gain,
            'capital_loss': self.capital_loss,
            'hours_week': self.hours_week,
            'over_50k': self.over_50k,
            'workclass_id': self.workclass_id,
            'education_level_id': self.education_level_id,
            'marital_status_id': self.marital_status_id,
            'occupation_id': self.occupation_id,
            'relationship_id': self.relationship_id,
            'race_id': self.race_id,
            'sex_id': self.sex_id,
            'country_id': self.country_id
        }


class Country(Base):
    """
    Country model
    """
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}


class EducationLevel(Base):
    """
    Education Level model
    """
    __tablename__ = "education_levels"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}


class MaritalStatus(Base):
    """
    Marital Status model
    """
    __tablename__ = "marital_statuses"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}


class Occupation(Base):
    """
    Occupation model
    """
    __tablename__ = "occupations"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}


class Race(Base):
    """
    Race model
    """
    __tablename__ = "races"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}


class Relationship(Base):
    """
    Relationship model
    """
    __tablename__ = "relationships"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}


class Sex(Base):
    """
    Gender model
    """
    __tablename__ = "sexes"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}


class WorkClass(Base):
    """
    Work class model
    """
    __tablename__ = "workclasses"
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    @property
    def serialize(self):
        """serialize the object"""
        return {'id': self.id, 'name': self.name}
