def display_the_skill_level():
    input("what are your top skills related to this course? ")
    input("do you have any prior experience? yes/no ")
    level = int(input("state the level of the skills you mentioned above between 1 - 3?. "))
    if level == 3:
        print("Your level is: Advance")
    if level == 2:
        print("Your level is: Intermediate")
    if level == 1:
        print("Your level is: Beginner")



display_the_skill_level()