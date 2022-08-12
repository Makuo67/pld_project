#!/usr/bin/python3
""" A function that welcomes the user and creates a user profile for the Train and Match Platform """


def user_profile():
    """Create a user profile for the Train and Match Platform"""
    print('Welcome to the Train and Match Platform!\n\nWe hope to serve you better')

    print("In the Train and Match Platform, we have absolute respect for human dignity and identity")

    fname = input('First name: ')
    lname = input('Last name: ')

    print("Welcome {} {}!".format(fname, lname))
    print("Let's check your skill level :)")
    print("Beginner = 1\nIntermediate = 2\nAdvanced = 3")
    skill1 = int(input('What level is your knowledge of Python programming?(Input number only): '))
    skill2 = int(input('What level is your knowledge in C programming?(Input number only): '))
    skill3 = int(input('What level is your knowledge of Java programming?(Input number only): '))
    skill4 = int(input('What level is your knowledge in other programming languages?(Input number only): '))

    skills = (skill4+skill3+skill2+skill1)
    if skills == 4:
        print('Welcome to the world of technology!\n Choose a course and start your learning!')
    if (skills > 4) and (skills <= 9):
        print("Thank you {}, you can continue learning.".format(fname))
    if skills >= 10:
        print("Congratulations {}!. You are qualified to start searching for a job".format(fname))


user_profile()
