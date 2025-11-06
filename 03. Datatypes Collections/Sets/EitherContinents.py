asia_pacific = {"Japan", "India", "Australia"}
europe = {"France", "Germany", "Italy"}

all_countries = asia_pacific | europe   # union
print(all_countries)
# {'Japan', 'India', 'Australia', 'France', 'Germany', 'Italy'}