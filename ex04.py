# number of cars
cars = 100
# amount space of passengers in a car
space_in_a_car = 4.0
# number of drivers driving a car today
drivers = 30
# number of passengers today
passengers = 190
# number of cars not driven, based on todays number of cars and drivers
cars_not_driven = cars - drivers
# number of cars driven, based on todays number of cars, essentially equal the number of available drivers
cars_driven = drivers
# overall capacity of all cars in the carpool
carpool_capacity = cars_driven * space_in_a_car
# passengers per car based on todays amount of cars driven and number of passengers
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# study drills

# explaining error: car_pool_capacity is an unknown variable name, intended variable was declared as carpool_capacity
# 1. space_in_a_car = 4.0 is assigned a floating point number, in our case it is not neccessary because of having only a multiplication based on the usage of space_in_a_car - therfore changing 4.0 to 4 should not change anything
# 2. carpool_capacity is assigned to the result of the multiplication involving an integer and a floating point number, therefore carpool_capacity is also a floating point number.
# 3. writing comments
# 4. symbol = is called equals and is used to assigning values to variables
# 5. well, as always, underscore is called underscore
# 6. running python as a calculator to calculate my average sleeptime during the last few days
# >>> hours = 5+5+6+4+7
# >>> minutes = 25 + 29 + 25 + 57 + 1
# >>> total = hours + minutes / 60.0
# >>> average = total / 5.0
# >>> average
# 5.8566666666666665
# >>>