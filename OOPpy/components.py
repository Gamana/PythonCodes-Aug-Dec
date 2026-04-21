class Student:
    #class Variable - class name or ref variable
    institute = "Kodnest"

    #Instance variables - ref variable
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    #Instance variables & Instance Method (self) - ref
    def study(self):
        print(f"{self.name} Studies")

    #class method - (cls) - classname , ref
    @classmethod
    def institute_change(cls, new_institute):
        cls.institute = new_institute

    #Static method - classnamne, ref
    @staticmethod
    def student_trip(student):
        print(f"{student.name} like to go for trip")


Student.institute_change("Kodnest pvt lmt")        
s1 = Student("Abhi", 21)
print(f"{s1.name}, {s1.age}, {s1.institute}")
print(Student.institute)
s1.study()
# Student.study()

s2 = Student("Viju", 22)
s2.student_trip(s2)
print(f"{s2.name}, {s2.age}, {s2.institute}")
s2.study()

Student.student_trip(s2)