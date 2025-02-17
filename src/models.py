import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey, Column, Integer
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    email = Column(String(75), nullable=False)
    password = Column(String(100), nullable=False)
    username = Column(String(75), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(75), nullable=False)
    phone = Column(String(75), nullable=False)
    subscription_date = Column(String(50), nullable=False)
    people = relationship('People', backref= 'user')
    vehicles = relationship('Vehicles', backref= 'user')
    planets = relationship('Planets', backref= 'user')

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    films_id = Column(Integer, ForeignKey('films.id'))
    name = Column(String(75), nullable=False)
    birth_year = Column(String(25), nullable=False)
    gender = Column(String(15), nullable=False)
    height = Column(String(25), nullable=False)
    mass = Column(String(15), nullable=False)
    eye_color = Column(String(10), nullable=False) 
    hair_color = Column(String(25), nullable=False)
    skin_color = Column(String(25), nullable=False) 
    homeworld = Column(String(250), nullable=False) 
    created = Column(String(100), nullable=False) 
    edited = Column(String(100), nullable=False) 
    url = Column(String(500), nullable=False)
    films = Column(String(500), nullable=False)
    species = Column(String(100), nullable=False)
    starships = Column(String(500), nullable=False)
    vehicles = Column(String(100), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    films_id = Column(Integer, ForeignKey('films.id'))
    name = Column(String(75), nullable=False)
    max_atmosphering_speed = Column(String(25), nullable=False)
    crew = Column(String(25), nullable=False)
    model = Column(String(75), nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    cargo_capacity = Column(String(75), nullable=False)
    consumables = Column(String(50), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    length = Column(String(25), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    passengers = Column(String(25), nullable=False)
    pilots = Column(String(300), nullable=False)
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)
    url = Column(String(500), nullable=False)
    films = Column(String(500), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    films_id = Column(Integer, ForeignKey('films.id'))
    climate = Column(String(75), nullable=False)
    created = Column(String(75), nullable=False)
    diameter = Column(String(75), nullable=False)
    edited = Column(String(75), nullable=False)
    gravity = Column(String(75), nullable=False)
    name = Column(String(75), nullable=False)
    orbital_period = Column(String(75), nullable=False)
    population = Column(String(75), nullable=False)
    rotation_period = Column(String(75), nullable=False)
    surface_water = Column(String(75), nullable=False)
    terrain = Column(String(75), nullable=False)
    url = Column(String(500), nullable=False)
    films = Column(String(500), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user = relationship('User', backref= 'favorites')
    people = relationship('People', backref= 'favorites')
    vehicles = relationship('Vehicles', backref= 'favorites')
    planets = relationship('Planets', backref= 'favorites')

class Films(Base):
    __tablename__='films'

    id = Column(Integer, primary_key=True)
    characters = Column(String(300), nullable=False)
    created = Column(String(75), nullable=False)
    director = Column(String(75), nullable=False)
    edited = Column(String(75), nullable=False)
    episode_id = Column(String(10), nullable=False)
    opening_crawl = Column(String(50), nullable=False)
    planets = Column(String(300), nullable=False)
    producer = Column(String(50), nullable=False)
    release_date = Column(String(50), nullable=False)
    species = Column(String(300), nullable=False)
    starships = Column(String(300), nullable=False)
    title = Column(String(150), nullable=False)
    url = Column(String(500), nullable=False)
    vehicles = Column(String(250), nullable=False)
    people_films = relationship('People', backref= 'films')
    vehicles_films = relationship('Vehicles', backref= 'films')
    planets_films = relationship('Planets', backref= 'films')
    starships_films = relationship('Starships', backref= 'films')
    species_films = relationship('Species', backref= 'films')

class Starships(Base):
    __tablename__='starships'

    id = Column(Integer, primary_key=True)
    films_id = Column(Integer, ForeignKey('films.id'))
    MGLT = Column(String(25), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    consumables = Column(String(25), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    created = Column(String(75), nullable=False)
    crew = Column(String(25), nullable=False)
    edited = Column(String(75), nullable=False)
    hyperdrive_rating = Column(String(25), nullable=False)
    length = Column(String(25), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    max_atmosphering_speed = Column(String(25), nullable=False)
    model = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    passengers = Column(String(15), nullable=False)
    films = Column(String(500), nullable=False)
    pilots = Column(String(100), nullable=False)
    starship_class = Column(String(150), nullable=False)
    url = Column(String(500), nullable=False)


class Species(Base):
    __tablename__='species'

    id = Column(Integer, primary_key=True)
    films_id = Column(Integer, ForeignKey('films.id'))
    average_height = Column(String(25), nullable=False)
    average_lifespan = Column(String(25), nullable=False)
    classification = Column(String(15), nullable=False)
    created = Column(String(75), nullable=False)
    designation = Column(String(15), nullable=False)
    edited = Column(String(75), nullable=False)
    eye_colors = Column(String(100), nullable=False)
    hair_colors = Column(String(100), nullable=False)
    homeworld = Column(String(100), nullable=False)
    language = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    people = Column(String(100), nullable=False)
    films = Column(String(100), nullable=False)
    skin_colors = Column(String(25), nullable=False)
    url = Column(String(500), nullable=False)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
