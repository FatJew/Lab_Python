from hotel import Hotel
from resort_hotel import ResortHotel
from motel import Motel
from typing import List, Optional


class HotelManager:
    """Class for managing multiple Hotel objects."""

    def __init__(self, hotels: List[Hotel]):
        self.hotels = hotels

    def display_hotels(self, hotels_list: Optional[List[Hotel]] = None) -> None:
        """Displays the hotels in the provided list. If no list is provided, displays all the hotels."""
        if hotels_list is None:
            hotels_list = self.hotels
        for hotel in hotels_list:
            print(hotel)

    def add_hotel(self, hotel: Hotel) -> None:
        """Adds a new Hotel to the list of hotels."""
        self.hotels.append(hotel)

    def find_all_with_room_greater_than(self, room: int = 100) -> List[Hotel]:
        """Finds and returns all the hotels with total rooms greater than the provided number."""
        return [hotel for hotel in self.hotels if hotel.total_rooms >= room]

    def find_with_pools(self) -> List[Hotel]:
        """Finds and returns all the ResortHotels with a pool for adults."""
        return [hotel for hotel in self.hotels if isinstance(hotel, ResortHotel) and hotel.pool_for_adults]


if __name__ == '__main__':
    hotel1 = ResortHotel("Resort1", 100, 4, True, True, 5, "Paradise Resort")
    hotel2 = Motel("Motel1", 50, 3, 1, 150, "CityA", "CityB")
    hotel3 = ResortHotel("Resort2", 200, 5, True, False, 8, "Beach Resort")

    hotel_manager = HotelManager([hotel1, hotel2, hotel3])
    hotel_manager.display_hotels()

    new_resort = ResortHotel("New Resort", 150, 4, False, True, 6, "Tropical Oasis")
    hotel_manager.add_hotel(new_resort)

    hotels_with_room_greater_than_100 = hotel_manager.find_all_with_room_greater_than(100)
    print("Hotels with room greater than 100:")
    hotel_manager.display_hotels(hotels_with_room_greater_than_100)

    hotels_with_pools = hotel_manager.find_with_pools()
    print("Hotels with pools:")
    hotel_manager.display_hotels(hotels_with_pools)
