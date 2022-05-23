from django.shortcuts import render, redirect, reverse
from .models import Room, RoomType, Booking
from forms.forms import AvailabilityForm
from django.contrib import messages
from booking_code.check_availability import check_availability
from booking_code.occupancy_rate import occupancy_rate
from datetime import date, datetime
import json
from urllib.parse import urlencode


def availability_view(request,type):

    if request.method == 'GET':
        # check roomtype is valid, define context,render page if correct
        # otherwise redirect to home with alert
        Room_Types = ['Single', 'Queen', 'Double']
        if  type in Room_Types:
                desc = RoomType.objects.get(type=type)
                form = AvailabilityForm()
                context = {
                 'type': type,
                 'form': form,
                 'desc': desc,
                }
                return render(request, 'roombook/book_1.html', context)
        else:
                messages.warning(request, 'That size unit does not exist..')
                return redirect(reverse('home:home'))

    if request.method == 'POST':
        # convert to int to match type of type_id in table
        # if not valid room type redirect to home with alert
        if type == 'Single':      
            typeint = 1
        elif type == 'Queen':
            typeint = 2
        elif type == 'Double':
            typeint = 3
        else:
            messages.warning(request, 'That size unit does not exist..')
            return redirect(reverse('home:home'))
        
        # get all instances of room type with the chosen type
        room_list = Room.objects.filter(type=typeint)  

        # form with data
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
        else:
            messages.warning(request, 'Form not valid')
            return redirect( reverse('roombook:book_1',kwargs={'type':type}))

        # empty list to hold rooms that have availability for desired dates
        available_rooms = []


        # check dates are chronologicaly correct
        # if dates invalid redirect with alert
        if data['check_in'] < date.today() or data['check_out'] < data['check_in'] or data['check_in'] == data['check_out']:
            messages.warning(request, 'Please enter a valid set of dates')
            return redirect( reverse('roombook:book_1',kwargs={'type':type}))

        # if dates are correct check each room for availability
        else:
            for room in room_list:
                if check_availability(room, data['check_in'], data['check_out']):
        # if room is returned from check_availability function add to list
                    available_rooms.append(room) 

        #if there is at least one room available
        if len(available_rooms) > 0: 
            room = available_rooms[0]
            data = {
                'room_number':str(room),
                'check_in':form.data['check_in'],
                'check_out':form.data['check_out'],
                'is_active':True,
                'type':type

            }

            # convert dict to json string
            with open("context.json", "w") as outfile:
                json.dump(data, outfile)

            data= {
                'context':outfile,
            }
            # join url path and data
            base_url = reverse('roombook:book')
            query_string =  urlencode({'data': data})
            url = '{}?{}'.format(base_url, query_string)
            

            # send to book template
            return redirect(url)
                      
        # if no room available display message and return to home screen                           
        else:
                messages.warning(request, 'All of this size of unit are booked!!\
                                     Try another one')
                return redirect(reverse('home:home'))
   
                


def book_room_view(request):
    # retrieve data
    data = request.GET.get('data')
    # convert json file
    with open('context.json') as json_file:
        data = json.load(json_file)

    if request.method == 'GET':
        # check occupancy rate for checkin date
        sale_flag = occupancy_rate(data)
       # define context and render page
        context = {
            'type':data,
            'sale_flag':sale_flag,
        }
        return render(request, 'roombook/book.html', context)

    if request.method == 'POST':
        #check if user logged in, redirect to home with message alert
        if not request.user.is_authenticated :
            messages.error(request, 'Please sign in to make a Booking .')
            return redirect(reverse('home:home'))
        
        # get instance of Room
        room = Room.objects.get(room_number=data['room_number'])
        # make the booking
        booking = Booking.objects.create(
                        user=request.user,
                        room_number=room,
                        check_in=data['check_in'],
                        check_out=data['check_out'],
                        is_active=True
                    )
        booking.save()   

        messages.success(request, f"Thank you for booking room\
                                 { data['room_number'] } from \
                                 { data['check_in'] } to {data['check_out'] }")
        return redirect(reverse('home:home'))