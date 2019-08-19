bus_capacity = 0
stops = [(14, 0), (8, 9), (32, 16), (7, 15)]
num_stops = 0
for on, off in stops:
    bus_capacity += on - off
    num_stops += 1
    if bus_capacity >= 40:
       break
print("Bus capacity:", bus_capacity)
print("Number of stops:",num_stops)

bus_capacity = 0
stops = [(2,0), (3,0), (14,5), (0,14)]
num_stops = 0
for on, off in stops:
    bus_capacity += on - off
    num_stops += 1
    if bus_capacity > 25:
        break
print("Bus capacity is:", bus_capacity)
print("Stops are:", num_stops)

