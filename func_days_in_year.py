def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    a = is_year_leap(year)
    if month in [4,6,9,11]:
        return 30
    elif month in [1,3,5,7,8,10,12]:
        return 31
    elif month is 2 and a == True:
        return 29
    elif month is 2 and a == False:
        return 28
    else:
        return None

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
