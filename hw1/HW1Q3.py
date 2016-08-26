#!/usr/bin/python3.4
#HW1Q3.py
#Python 3.4 
#Panama canal rain calculator

print("Panama canal statistics:")


# to calculate the volume needed to fill a lock of these given dimenstions
def volume_solid(width, length, depth):
    vol = (width * length * depth)
    return vol


# to return the amount of water needed to filkl a lock with the given volume for a full year
def water_needed_perlock(volume):
    ships_per_day = 35
    total_rain = (ships_per_day * 365 * volume)
    return total_rain


# Total amount of water used:
total_water = (water_needed_perlock(volume_solid(32, 320, 10)) * 2)

print("Total volume of water needed for ships:", total_water, "cubic meters")
print("Rain needed:", (total_water / 270), "cubic meters per day")
print("Which converts to", ((total_water / 600000) / 270), "milimeters per day")

# The lock is 102400 cublic meters
# There are two locks
# 600000 cm = 1 ml

