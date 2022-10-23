import mean as mean

Students_logbook = True
button = ['1', '2', '3', '4', '5', '6']
Students_list = {1: 'Piotr Zyla',
                 2: 'Kamil Stoch',
                 3: 'Klemens Muranka',
                 4: 'Gregor Shlirenzauer',
                 5: 'Maciej Kot'}
Students_grades_maths = {1: 1,
                         2: 'Kamil Stoch: 5',
                         3: 'Klemens Muranka: 3',
                         4: 'Gragor Shlirenzauer: 6',
                         5: 'Maciej Kot: 2'}
while Students_logbook:
    print("""Please select\nStudent List: 1\nStudent Grades: 2\nAdd Grade: 3\nStudent Average Grades: 4
Add Student: 5\nDelete Student: 6""")
    action = input()
    if action == button[0]:
        for key, value in Students_list.items():
            print(f'{key}, {value}')
    elif action == button[1]:
        for key, value in Students_grades_maths.items():
            print('Maths:', value)
    elif action == button[2]:
        print('Choose number in logbook')
        action = input()
        if action == button[0]:
            print(Students_list.get(1))
            print('Do you want add mark?')
            action = input()
            if action == str('yes'):
                print('what grade')
                Students_grades_maths[1] = (Students_grades_maths[1], input())
        if action == button[1]:
            print(Students_list.get(2))
            print('Do you want add mark?')
            action = input()
            if action == str('yes'):
                print('what grade?')
                Students_grades_maths[2] = (Students_grades_maths[2], input())
        if action == button[2]:
            print(Students_list.get(3))
            print('Do you want add mark?')
            action = input()
            if action == str('yes'):
                print('what grade?')
                Students_grades_maths[3] = (Students_grades_maths[3], input())
        if action == button[3]:
            print(Students_list.get(4))
            print('Do you want add mark?')
            action = input()
            if action == str('yes'):
                print('what grade?')
                Students_grades_maths[4] = (Students_grades_maths[4], input())
        if action == button[4]:
            print(Students_list.get(5))
            print('Do you want add mark?')
            action = input()
            if action == str('yes'):
                print('what grade?')
                Students_grades_maths[5] = (Students_grades_maths[5], input())
    elif action == button[3]:
        print('Choose student')
        action = input()
        if action == button[0]:
            print(Students_list[1])
            print('Do you want calculate mean for this student ?')
            action = input()
            if action == 'yes':
                print(mean.Students_grades_maths[1])
    elif action == button[4]:
        print('Do you want to add student?')
        action == input()
        if action == 'yes':
            Students_list[6] = input()
    elif action == button[5]:
        print('Choose student')
        action = input()
        if action == button[0]:
            print(Students_list[1])
            print('Do you want delete this student')
            action = input()
            if action == 'yes':
                del Students_list[1]
        elif action == button[1]:
            print(Students_list[2])
            print('Do you want delete this student')
            action = input()
            if action == 'yes':
                del Students_list[2]
        elif action == button[2]:
            print(Students_list[3])
            print('Do you want delete this student')
            action = input()
            if action == 'yes':
                del Students_list[3]
        elif action == button[3]:
            print(Students_list[4])
            print('Do you want delete this student')
            action = input()
            if action == 'yes':
                del Students_list[4]
        elif action == button[4]:
            print(Students_list[5])
            print('Do you want delete this student')
            action = input()
            if action == 'yes':
                del Students_list[5]

