#Imagine that you develop a piece of software for an automatic weather station. 
# The device records the air temperature on an hourly basis and does it throughout the month. 
# This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.
######################################################################################################################---------------------
#Now it's time to determine the monthly average noon temperature. Add up all 31 readings recorded at noon and divide the sum by 31. 
# You can assume that the midnight temperature is stored first. Here's the relevant code:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

#Note: the day variable used by the for loop is not a scalar - each pass through the temps matrix assigns it with the subsequent rows of the matrix;
# hence, it's a list. It has to be indexed with 11 to access the temperature value measured at noon.

######################------------------------------------------------------------------------------------------------>>>>>>>>>>>>>>>>>>>>>>>>>

# Now find the highest temperature during the whole month:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

############################################################################################################################3

#Now count the days when the temperature at noon was at least 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")