# Hotel cost
# function to calculate hotel cost per night
def hotel_cost(nights):
    return 140*nights

# function to calculate plane ride depending on the city
def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return 2000
    elif city == "BFN":
        return 1800


# function to calculate cost of renting a car and discount
def rental_car_cost(days):
    car_cost = 40*days
    if days >=7 :
        car_cost = car_cost - 50 # discount if days >=7
    elif days >= 3 and days <7:
        car_cost = car_cost - 20 # discount if days
    return car_cost
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print(trip_cost("Cape Town",6,1000))






