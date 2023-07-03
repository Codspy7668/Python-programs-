import calendar

# Enter the month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
dd=int(input("Enter day"))

# display the calendar
print(calendar.month(yy, mm, dd))