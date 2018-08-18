
import calendar

ticket ="Please input a year! \n"
year = input(ticket)

cal = calendar.calendar(int(year))

print("This is the calendar of "+year)
print(cal)
