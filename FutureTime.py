#FutureTime.py
#Name: Afrah Mohamoud
#Date: 1/31/2026
#Assignment: Lab 2
#Purpose: Calculate future time based on user input

# datetime will allow us to access the system date and time.
import datetime

def main():
    # Getting current time from system, storing to variable
    now = datetime.datetime.now()   
    currentHour = now.hour
    currentMinute = now.minute

    print(f"Current time: {currentHour}:{currentMinute:02d}")  # For checking
    
    # Ask user for hours and minutes
    moreHours = int(input("Hours to add: "))
    moreMins = int(input("Minutes to add: "))
    
    # Calculate future minutes and any extra hour from overflow
    futureMins = (currentMinute + moreMins) % 60
    extraHour = (currentMinute + moreMins) // 60
    
    # Calculate future hour (including the extra hour from minutes overflow)
    futureHour = (currentHour + moreHours + extraHour) % 24
    
    # Output the future time in standard format "HH:MM"
    print(f"The future time is {futureHour:02d}:{futureMins:02d}")

if __name__ == '__main__':
    main() 