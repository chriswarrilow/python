# Cars available to drive.
cars = 100

# Space available in cars for passengers.
space_in_a_car = 4

# Number of drivers available.
drivers = 30

# Number of passengers that need a ride.
passengers = 90

# Ammount of cars that wont have enough drivers.
cars_not_driven = cars - drivers

# Ammount of cars that will be driven.
cars_driven = drivers

# Ammount of people that will need a ride.
carpool_capacity = cars_driven * space_in_a_car

# Average ammount of passengers needed to be in each car.
average_passangers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passangers_per_car, "in each car.")
