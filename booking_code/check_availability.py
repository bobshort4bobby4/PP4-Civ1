"""
Code to check availability of
room for a specific set of dates

"""
from roombook.models import Booking


def check_availability(room, check_in, check_out):
    """
        Function to check availability of
        room for a specific set of dates.

        Parameters:
            room:object an instance of Room
            check_in: datetime object
            check_out: datetime object

        Returns: a boolean
    """
    # create empty list
    avail_list = []
    # get all bookings for that room
    bookings = Booking.objects.filter(room_number=room)
    # for each booking if existing booking does not overlap
    # desired booking append true to list
    for booking in bookings:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    # return true if all items in list are true
    # ie no existing booking clashes with desired booking
    return all(avail_list)
