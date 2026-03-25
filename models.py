from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Passenger(Base):
    __tablename__ = 'passengers'
    
    id = Column(Integer, primary_key=True)
    passenger_id = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    frequent_flyer_number = Column(String)
    tier_status = Column(String, default='Bronze')
    total_miles = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True)
    booking_reference = Column(String, unique=True, nullable=False)
    passenger_id = Column(String, nullable=False)
    flight_number = Column(String, nullable=False)
    departure_airport = Column(String, nullable=False)
    arrival_airport = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    seat_number = Column(String)
    class_type = Column(String)
    status = Column(String, default='Confirmed')
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class FlightStatus(Base):
    __tablename__ = 'flight_status'
    
    id = Column(Integer, primary_key=True)
    flight_number = Column(String, nullable=False)
    departure_airport = Column(String, nullable=False)
    arrival_airport = Column(String, nullable=False)
    scheduled_departure = Column(DateTime, nullable=False)
    scheduled_arrival = Column(DateTime, nullable=False)
    actual_departure = Column(DateTime)
    actual_arrival = Column(DateTime)
    status = Column(String, default='On Time')
    gate = Column(String)
    terminal = Column(String)
    delay_minutes = Column(Integer, default=0)

class Service(Base):
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True)
    service_type = Column(String, nullable=False)
    passenger_id = Column(String, nullable=False)
    booking_reference = Column(String)
    status = Column(String, default='Pending')
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
