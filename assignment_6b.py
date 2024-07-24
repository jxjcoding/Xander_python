# Author: Xander Wang
# Date: 2024-7-22
# ------------------------------------------------------------------------------------------------------------------
# Question: Create a dictionary with 4 entries: 
# a string, integer, boolean, and a list. Then, 
# print, change value of str, print, print all values of dict,
# remove int, loop, print, copy to another dict, and finally print again. 

# Create dictionary with 4 entries:
our_ascent = {
    "color": "blue", 
    "year": 2020, 
    "brand_new": True, 
    "places": ["blue_ridge", "hilton_head", "myrtle_beach"]
}

# Print: 
print(our_ascent)

# Change value of str:
our_ascent["color"] = "white"

# Print
print(our_ascent)

# Print all values: 
x = our_ascent.values()
print(x)

# Remove int:
our_ascent.pop("year")
print(our_ascent)

# Loop:
for y in our_ascent:
    print(y)

# Print
print(our_ascent)

# Copy:
our_ascent_2 = our_ascent.copy()
print(our_ascent_2)

# Print
print(our_ascent_2)

# Thank you!