# Week 2 task
rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

# Print names of rivers
print("\n")
print("The names of the riveres are: ")
for river in rivers:
    print(river["name"])

print("\n")
total_length_of_rivers = 0
for river in rivers:
    total_length_of_rivers += river["length"]
print("The total length of rivers is: ", total_length_of_rivers)

# Print names of rivers that start with "M"
print("\n")
print("The following rivers start with letter M:")
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])

print("\n")
# Length of rivers in kilometers
print("The length of rivers in kilometers:")
conversion_factor = 1.6

for river in rivers:
    length_km = river["length"] * conversion_factor
    print(f"{river['name']} - Length: {length_km:.2f} km")
