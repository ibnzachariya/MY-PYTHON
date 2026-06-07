# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
# print(travel_log["France"][1])
# print(travel_log["Germany"][0])

# Nested list
nested_list = ["A", "B", ["C", ["f", "g"], "D"]]
# print(nested_list[2][1][0]) #to print f

travel_log = {
    "France": {"cities_Visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
               },
    "Germany": {"cities_Visited": ["Stuttgart", "Berlin", "Hamburg"], "total_visits": 5
                },
}
print(travel_log["Germany"]["cities_Visited"][0])
