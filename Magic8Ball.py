# Magic8Ball.py
# Name: Afrah Mohamoud
# Date: 1/31/2026
# Assignment: Lab 2 
# Purpose:

 #We will need random for this program, import to use this package.
import random

def main():
 #Create a list of yor responses.
 print("Magic 8 Ball")
 # prompt required by the assignment
answers = [ "thing 1", "thing 2", "thing 3", "thing 4", "thing 5", "thing 6", 
          "thing 7", "thing 8", "thing 9", "thing 10"]


 #Answer question randomly with one of the options from your earlier list.
length = len(answers) 
r = random.random() * length 

r = int(r) #cut off deimal values

print(r)
response = answers[r] 
print(response)

if __name__ == '__main__':
    main()
