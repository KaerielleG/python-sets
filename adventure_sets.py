'''    
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
'''

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
print ("Destinations both airlines fly to:", common_destinations)

unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

neither_airline_shares = (our_routes.isdisjoint(competitor_routes))
print("Are there any destinations that neither airline shares?", neither_airline_shares)

