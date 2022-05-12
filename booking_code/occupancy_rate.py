from roombook.models import Room, Booking
import datetime


def occupancy_rate(data):
    bookings = Booking.objects.all()
    rooms = Room.objects.all()
    bookedrooms = []
    year = data['check_in']
    y = int(data['check_in'][0:4])
    m = int(data['check_in'][5:7])
    d = int(data['check_in'][8:10])
        
    cin = datetime.date(y, m, d)  
    for room in rooms:
        for booking in bookings:
            if booking.room_number_id == room.room_number:
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