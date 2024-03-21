# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
yearint=input("Enter a year:")
monthint=input("Enter a month:")
dayint=input("Enter a day:")
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = int(yearint)
month = int(monthint)
day = int(dayint)
testeddate= str(month) +"/" +str(day) + "/" + str(year)

# Get the year, then the month, then the day
# housekeeping()

# Check to be sure date is valid

if (int(year) <= MIN_YEAR or
     int(month) < MIN_MONTH or int(month) > MAX_MONTH or            int(day) < MIN_DAY or int(day) > MAX_DAY):
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
  print(str(testeddate) +" is a valid date")
    # Output statement
else:
    # Output statement
  print(str(testeddate) + " is an invalid date")