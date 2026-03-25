from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Passenger, Booking, FlightStatus, Service
from datetime import datetime, timedelta

class DatabaseHandler:
    def __init__(self, db_url='sqlite:///airport_crm.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self._populate_demo_data()
    
    def _populate_demo_data(self):
        """Populate database with demo data if empty"""
        if self.session.query(Passenger).count() == 0:
            self._add_demo_passengers()
            self._add_demo_bookings()
            self._add_demo_flights()
    
    def _add_demo_passengers(self):
        passengers = [
            Passenger(
                passenger_id='PAX001',
                first_name='John',
                last_name='Smith',
                email='john.smith@email.com',
                phone='+1-555-0101',
                frequent_flyer_number='FF123456',
                tier_status='Gold',
                total_miles=45000
            ),
            Passenger(
                passenger_id='PAX002',
                first_name='Sarah',
                last_name='Johnson',
                email='sarah.j@email.com',
                phone='+1-555-0102',
                frequent_flyer_number='FF789012',
                tier_status='Platinum',
                total_miles=87000
            ),
            Passenger(
                passenger_id='PAX003',
                first_name='Michael',
                last_name='Brown',
                email='m.brown@email.com',
                phone='+1-555-0103',
                tier_status='Bronze',
                total_miles=5000
            ),
        ]
        self.session.add_all(passengers)
        self.session.commit()
    
    def _add_demo_bookings(self):
        bookings = [
            Booking(
                booking_reference='BK001',
                passenger_id='PAX001',
                flight_number='AA101',
                departure_airport='JFK',
                arrival_airport='LAX',
                departure_time=datetime.now() + timedelta(days=2, hours=8),
                arrival_time=datetime.now() + timedelta(days=2, hours=14),
                seat_number='12A',
                class_type='Business',
                price=850.00
            ),
            Booking(
                booking_reference='BK002',
                passenger_id='PAX002',
                flight_number='UA202',
                departure_airport='ORD',
                arrival_airport='MIA',
                departure_time=datetime.now() + timedelta(days=1, hours=10),
                arrival_time=datetime.now() + timedelta(days=1, hours=14),
                seat_number='8C',
                class_type='First',
                price=1250.00
            ),
        ]
        self.session.add_all(bookings)
        self.session.commit()
    
    def _add_demo_flights(self):
        flights = [
            FlightStatus(
                flight_number='AA101',
                departure_airport='JFK',
                arrival_airport='LAX',
                scheduled_departure=datetime.now() + timedelta(days=2, hours=8),
                scheduled_arrival=datetime.now() + timedelta(days=2, hours=14),
                status='On Time',
                gate='B12',
                terminal='4'
            ),
            FlightStatus(
                flight_number='UA202',
                departure_airport='ORD',
                arrival_airport='MIA',
                scheduled_departure=datetime.now() + timedelta(days=1, hours=10),
                scheduled_arrival=datetime.now() + timedelta(days=1, hours=14),
                status='Delayed',
                gate='C7',
                terminal='1',
                delay_minutes=30
            ),
        ]
        self.session.add_all(flights)
        self.session.commit()
    
    def get_passenger_by_email(self, email):
        return self.session.query(Passenger).filter_by(email=email).first()
    
    def get_booking_by_reference(self, booking_ref):
        return self.session.query(Booking).filter_by(booking_reference=booking_ref).first()
    
    def get_flight_status(self, flight_number):
        return self.session.query(FlightStatus).filter_by(flight_number=flight_number).first()
    
    def get_passenger_bookings(self, passenger_id):
        return self.session.query(Booking).filter_by(passenger_id=passenger_id).all()
    
    def create_service_request(self, service_type, passenger_id, booking_ref=None, notes=None):
        service = Service(
            service_type=service_type,
            passenger_id=passenger_id,
            booking_reference=booking_ref,
            notes=notes
        )
        self.session.add(service)
        self.session.commit()
        return service
