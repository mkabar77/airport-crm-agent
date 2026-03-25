from langchain.tools import Tool
from typing import Optional
from database.db_handler import DatabaseHandler

db = DatabaseHandler()

def lookup_passenger(email: str) -> str:
    """Look up passenger information by email"""
    passenger = db.get_passenger_by_email(email)
    if passenger:
        return f"""Passenger Found:
Name: {passenger.first_name} {passenger.last_name}
ID: {passenger.passenger_id}
Email: {passenger.email}
Phone: {passenger.phone}
Frequent Flyer: {passenger.frequent_flyer_number}
Tier Status: {passenger.tier_status}
Total Miles: {passenger.total_miles:,}"""
    return "Passenger not found in our system."

def lookup_booking(booking_reference: str) -> str:
    """Look up booking details by reference number"""
    booking = db.get_booking_by_reference(booking_reference)
    if booking:
        return f"""Booking Details:
Reference: {booking.booking_reference}
Flight: {booking.flight_number}
Route: {booking.departure_airport} → {booking.arrival_airport}
Departure: {booking.departure_time.strftime('%Y-%m-%d %H:%M')}
Arrival: {booking.arrival_time.strftime('%Y-%m-%d %H:%M')}
Seat: {booking.seat_number}
Class: {booking.class_type}
Status: {booking.status}
Price: ${booking.price:.2f}"""
    return "Booking not found."

def check_flight_status(flight_number: str) -> str:
    """Check real-time flight status"""
    flight = db.get_flight_status(flight_number)
    if flight:
        status_msg = f"""Flight Status for {flight.flight_number}:
Route: {flight.departure_airport} → {flight.arrival_airport}
Scheduled Departure: {flight.scheduled_departure.strftime('%Y-%m-%d %H:%M')}
Scheduled Arrival: {flight.scheduled_arrival.strftime('%Y-%m-%d %H:%M')}
Status: {flight.status}
Gate: {flight.gate}
Terminal: {flight.terminal}"""
        if flight.delay_minutes > 0:
            status_msg += f"\nDelay: {flight.delay_minutes} minutes"
        return status_msg
    return "Flight not found."

def create_service_request(service_type: str, passenger_id: str, 
                          booking_reference: str = "", notes: str = "") -> str:
    """Create a service request for passenger"""
    service = db.create_service_request(
        service_type, 
        passenger_id, 
        booking_reference if booking_reference else None,
        notes if notes else None
    )
    return f"Service request created successfully. Request ID: {service.id}. Type: {service_type}. Status: {service.status}"

# Define tools for the agent
tools = [
    Tool(
        name="LookupPassenger",
        func=lookup_passenger,
        description="Look up passenger information using their email address. Use this when you need to find passenger details, tier status, or frequent flyer information. Input should be a valid email address."
    ),
    Tool(
        name="LookupBooking",
        func=lookup_booking,
        description="Look up booking details using the booking reference number. Use this to find flight details, seat assignments, and booking status. Input should be a booking reference like 'BK001'."
    ),
    Tool(
        name="CheckFlightStatus",
        func=check_flight_status,
        description="Check real-time flight status using the flight number. Use this to provide information about delays, gates, and departure times. Input should be a flight number like 'AA101'."
    ),
    Tool(
        name="CreateServiceRequest",
        func=create_service_request,
        description="Create a service request for a passenger. Service types include: Lounge, FastTrack, Baggage, Wheelchair. Input format: 'service_type, passenger_id, booking_reference (optional), notes (optional)'. Example: 'Wheelchair, PAX001, BK001, Needs assistance at gate'."
    )
]
