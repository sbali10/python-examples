#Creating new user profile for a student or get user info of a existing student


select = input("Hello if you're our student select 1, if not select 2 : ")
select = int(select)
print(select)



if select == 1:

    student= {
        '120': {
            'name': 'Ali',
            'surname': 'A',
            'phone': '111 111'    
        },
        '121' : {
            'name': 'Bali',
            'surname': 'B',
            'phone': '222 222'
        },
        '122': {
            'name': 'CAli',
            'surname': 'C',
            'phone': '444 111'
        }
    
    }

    idk = input('Entry student number: ')   #öğrenci no girdirdik
    idk = int(idk)
    if 120<idk<123 :
        idk = str(idk)
        stud = student[idk]               # öğrenci no'suna ait tablodaki index bulundu
        print('*'*50)                          
        print(f"The name of your student is {((stud)['name'])} and surname is {((stud)['surname'])}. Contact number of your student is {((stud)['phone'])}")
        print('*'*50)
    
    else:
        print("Select 2 on start and create user profile")
        

elif select == 2:

    student = {}

    number = input("Student number: ")
    name = input("Student name: ")
    surname = input("Student surname: ")
    phone = input("Student phone number: ")
    
    student.update({
        number: {
            'name': name,
            'surname': surname,
            'phone': phone
    
        }
    })
    
    print('*'*50)
    print(student)
    print('*'*50)



else:
    print("Select 1 or 2 for your correct status")





