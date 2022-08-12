#!/usr/bin/python3
"""A function the sets the skills of the users
and provide recommendation"""


def user_skill():
    """Display set skills to the user

    The user chooses skills to learn and then recommendation pops up
    """
    skills = ['Machine Learning', 'Virtual reality/Augmented reality',
              'Data Analytics', 'Data Engineering', "Cloud computing/AWS",
              'Cybersecurity', 'UI/UX Design', 'Web development', 'Blockchain']
    for (i, item) in enumerate(skills, start=1):
        print(i, item)
    get_skills = int(input('Enter the skill of your choice: '))
    if get_skills == 1:
        print('Welcome to Machine Learning program!\n'
              'Program requirements\n'
              'Ensure you have a strong background in Mathematics\n'
              'Refer to the link: https://alison.com/tag/machine-learning')
    if get_skills == 2:
        print('Welcome to VR/AR program!\n'
              'Program requirements\n'
              '1. Ensure you have a strong background in Mathematics and Programming\n'
              'Refer to the link: https://alison.com/tag/virtual-reality')
    if get_skills == 3:
        print('Welcome to Data Analytics program!\n'
              'Program requirements\n'
              '1. Ensure you have a strong background in Statistics, SQL and programming\n'
              'Refer to the link: https://alison.com/tag/data-science')

    if get_skills == 4:
        print('Welcome to Data Engineering program!\n'
              'Program requirements\n'
              '1. Ensure you have a strong background in Mathematics and Programming\n'
              'Refer to the link: https://alison.com/tag/data-engineering')
    if get_skills == 5:
        print('Welcome to Cloud Computing program!\n'
              'Program requirements\n'
              '1. Ensure you have a strong background in Mathematics and Programming\n'
              'Refer to the link: https://alison.com/tag/cloud-computing')
    if get_skills == 6:
        print('Welcome to Cyber Security program!\n'
              'Program requirements\n'
              '1. Stay determined and you will be a great cyber engineer\n'
              'Refer to the link: https://alison.com/tag/cyber-security')
    if get_skills == 7:
        print('Welcome to UI/UX Design program!\n'
              'Program requirements\n'
              '1. Ensure you have a strong background in Mathematics and Programming\n'
              'Refer to the link: '
              'https://alison.com/topic/learn/introduction-and-basics-of-adobe-xd-learning-outcomes')
    if get_skills == 8:
        print('Welcome to Full Stack Web Development program!\n'
              'Program requirements\n'
              'Refer to the link: https://alison.com/tag/full-stack-development')
    if get_skills == 9:
        print('Welcome to Blockchain program!\n'
              'Program requirements\n'
              '1. Ensure you have a strong background in Mathematics and Programming\n'
              'Refer to the link: https://alison.com/tag/blockchain')


user_skill()
