#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on March 11
# This program checks if the user is older enough to vote


def main():
    # Get user age_input(age)
    user_age = int(input("Enter an age : "))

    # if the age is greater than 18, then the user can vote
    if user_age > 18:
        print("You are old enough to vote.")

    # if the age is less than 18, then you are to young
    elif user_age < 18:
        print("You are underage.")
    # if the user_age is 0, then it's not possible
    else:
        print("it is impossible.")


if __name__ == "__main__":
    main()
