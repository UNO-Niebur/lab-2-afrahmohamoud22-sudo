# Magic8Ball.py
# Name: Afrah Mohamoud
# Date: 1/31/2026
# Assignment: Lab 2
# Purpose: Prompt the user for a question and display a random Magic 8-Ball response.

import random

def main():
  
    print("Magic 8 Ball")
    question = input("Ask a question: ")  # prompt required by the assignment

    answers = [
        "It is certain.",
        "Ask again later.",
        "Don't count on it.",
        "Yes — definitely.",
        "My sources say no.",
        "Outlook good.",
        "Very doubtful.",
        "Signs point to yes.",
        "Cannot predict now.",
        "Most likely."
    ]

    # use random.choice as required by the README/spec
    response = random.choice(answers)
    print(response)

if __name__ == '__main__':
    main()
