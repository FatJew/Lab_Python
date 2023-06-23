class Hotel:
    default_hotel = None

    def __init__(self, name="", total_rooms=0, rating=0):
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms
        self.rating = rating
        self.booked_rooms_count = 0

    def book_room(self):
        if self.available_rooms > 0:
            self.available_rooms -= 1
            self.booked_rooms_count += 1
            print("Your room is ready")
        else:
            print("All rooms are booked")

    def release_room(self):
        if self.booked_rooms_count > 0:
            self.available_rooms += 1
            self.booked_rooms_count -= 1
        else:
            print("All rooms are available")

    def __str__(self):
        return f"Hotel(name='{self.name}', total_rooms={self.total_rooms}, rating={self.rating})"

    @staticmethod
    def get_instance():
        if not Hotel.default_hotel:
            Hotel.default_hotel = Hotel()
        return Hotel.default_hotel


if __name__ == '__main__':
    print("Welcome to our hotel!")
    hotel = Hotel("Eurohotel", 50, 4)
    print("Available rooms:", hotel.available_rooms)
    print("Booked rooms:", hotel.booked_rooms_count)
    hotel.book_room()
    hotel.book_room()
    hotel.release_room()
    print("Available rooms:", hotel.available_rooms)
    print("Booked rooms:", hotel.booked_rooms_count)

    hotels = [Hotel(), Hotel("Eurohotel", 50, 4), Hotel.get_instance(), Hotel.get_instance()]

    for h in hotels:
        print(h)