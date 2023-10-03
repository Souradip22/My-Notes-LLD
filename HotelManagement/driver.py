
from models.hotel import Hotel
from models.hotel_location import HotelLocation
from models.notification import Notification
from models.room import Room
from models.room_booking import RoomBooking

# Create a Hotel object
my_hotel = Hotel("The Sun Palace")

# Add some locations to the hotel
location1 = HotelLocation("Udaipur", "Street 1", 9876543)
location2 = HotelLocation("Jaipur", "Street 5", 7654321)
my_hotel.add_location(location1)
my_hotel.add_location(location2)

# Get the name and locations of the hotel
print("Hotel Name:", my_hotel.get_name())
print("Hotel Locations:")
locations = my_hotel.get_locations()
for location in locations:
    print("Location:", location.get_location())
    print("Address:", location.get_address())
    print("Phone Number:", location.get_phone_number())
    print()

# Create a Room object
room1 = Room(101, "Deluxe", 2500)
room2 = Room(102, "AC", 2000)
room3 = Room(103, "Non - AC", 1500)

my_hotel.rooms.extend([room1, room2, room3])

# Create a RoomBooking object
booking1 = RoomBooking(room1, "Souradip Chandra", 3)

# Get the details of the RoomBooking
print("Guest Name:", booking1.get_guest_name())
print("Room Number:", booking1.get_room().get_room_number())
print("Room Style:", booking1.get_room().get_room_style())
print("Booking Price:", booking1.get_room().get_booking_price())
print("Number of Nights:", booking1.get_number_of_nights())

# Create a Notification object
notification1 = Notification("Your booking has been confirmed.", "Souradip Chandra")

# Get the details of the Notification
print("Message:", notification1.get_message())
print("Recipient:", notification1.get_recipient())