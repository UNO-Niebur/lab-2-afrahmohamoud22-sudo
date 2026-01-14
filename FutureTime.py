#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
