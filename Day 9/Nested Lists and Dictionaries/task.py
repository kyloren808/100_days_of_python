capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
}

# print "Lille"
print(travel_log["France"][1])

# 2–D list
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

my_travel_log = {
    "France": {
        "number_times_visited": 4,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "number_times_visited": 3,
        "cities_visited": ["Berlin", "Munich", "Hamburg"],
    },
}

print(my_travel_log["Germany"]["cities_visited"][2])
print(my_travel_log["France"]["cities_visited"][2])
