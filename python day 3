distance_mi = 4
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1:
    if is_raining == False:
        print(True)
    if is_raining == True:
        print(False)

elif 1 < distance_mi <= 6:
    if is_raining == True and has_bike == False:
        print(False)
    if is_raining == False and has_bike == False:
        print(False)
    if is_raining == False and has_bike == True:
        print(True)

elif distance_mi > 6:
    if has_ride_share_app == True:
        print(True)
    if has_car == True:
        print(True)
    if has_car == False and has_ride_share_app == False:
        print(False)
