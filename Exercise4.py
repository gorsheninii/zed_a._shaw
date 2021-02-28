cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There is", cars, "cars")
print("And only", drivers, "drivers, that can work")
print("That's why, only", cars_not_driven, "cars is empty")
print("We can transfer today:", carpool_capacity, "passengers")
print("Today we need to transfer", passengers, "passengers")
print("Average passengers in the car is", average_passengers_per_car)