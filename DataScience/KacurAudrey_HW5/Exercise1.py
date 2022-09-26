
# using a lambda that accepts the parameters distance and speed compute the time to collision (in seconds)
# speed v = s/t where s is distance and t is time
# result = lambda s, v: s/v
#t = s/v
def result(s, v): return s/v


print("You are driving on a highway with your vehicle - in front of you a car stopped")
# enter your speed of the vehicle in (km/h)
v = int(input("Please enter the speed your care is going in km/h: "))
# enter the distance between your vehicle and stopped one in meters
s = int(input("Please enter the distance between your vehicle and stopped one in meters: "))
print(result(s, v))
