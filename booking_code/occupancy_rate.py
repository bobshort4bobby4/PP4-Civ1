"""
Calculates if a sale should be declared
based on the occupancy rate
"""


import datetime
from roombook.models import Room, Booking


def occupancy_rate(data):
    """
    A function to calculate occupancy rate

    Parameters:
        data:dictionary

    Returns: boolean
    """
    bookings = Booking.objects.all()
    rooms = Room.objects.all()
    bookedrooms = []
    # convert to datetime object
    y = int(data['check_in'][0:4])
    m = int(data['check_in'][5:7])
    d = int(data['check_in'][8:10])

    cin = datetime.date(y, m, d)
    for room in rooms:
        for booking in bookings:
            if booking.room_number_id == room.room_number:
                # if check-in falls within existing bookings date range
                # add that room to list
                if cin >= booking.check_in:
                    if cin <= booking.check_out:
                        bookedrooms.append(room)

    countbookedrooms = int(len(bookedrooms))
    counttotalroom = Room.objects.all().count()
    # if occupancy rate below 50% set sale flag to true
    occrate = (countbookedrooms/counttotalroom)*100
    if (occrate) < 50:
        sale_flag = True
    else:
        sale_flag = False

    return sale_flag
