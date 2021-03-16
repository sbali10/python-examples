
# class Person():
#     def __init__(self, fname, lname):
#         self.firstName = fname
#         self.lastName = lname
#         print("person created")

#     def who_am_i(self):
#         print("I am a person")



# class Student(Person):
#     def __init__(self, fname, lname, number):
#         Person.__init__(self, fname, lname)
#         self.studentNumber = number
#         print("Student created")

#     def who_am_i(self):              #yukarıdaki who_am_i ı override ettik
#         print("I am a student")



# class Teacher(Person):
#     def __init__(self, fname, lname, branch):
#         super().__init__(fname, lname)
#         self.branch = branch

#     def who_am_i(self):
#         print(f"I am a {self.branch} teacher")




# p1 = Person("ali", "yilmaz")
# s1 = Student("baran", "bali", 121)
# t1 = Teacher("mehmet", "hoca", "matematik")



# print(p1.firstName + " " + p1.lastName)
# print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))
# print(t1.branch)



# p1.who_am_i()
# s1.who_am_i()
# t1.who_am_i()


############################################################################################################

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

m = Movie("film adı", "yönetmen adı", 120)


print(str(m))
print(len(m))