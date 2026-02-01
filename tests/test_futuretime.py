#FutureTime.py
#Name: Afrah Mohamoud
#Date: 1/31/2026
#Assignment: Lab 2
#Purpose:
# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now(now.hour - 6) % 24  
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  moreMins = 30  

  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60 
  
  print(extraHour) 
  
  print(futureMins) 
  #Calculate the time after the user-supplied time has passed.
  futureHour = (currentHour + extraHour) % 24   
  #Do not use any if statements in calculating the time.
  
  #Output the future time in standard format "HH:MM"

if __name__ == '__main__':
  main()