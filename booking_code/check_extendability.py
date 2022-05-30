"""
Code to check if stay can be extended
"""
from roombook.models import Booking


def check_extendability(room, check_in, check_out):
    """
    function to check if a particular stay can be extended

    Parameters:
        room:object an instance of Room
            check_in: datetime object
            check_out: datetime object

        Returns: a boolean

    """
    avail_list = []
    bookings = Booking.objects.filter(room_number=room)
    for booking in bookings:
        if booking.check_in > check_out or booking.check_out <= check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)
