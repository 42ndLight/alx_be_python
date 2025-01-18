class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_score(self):
        return self.score

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

student1 = Student("John", 20, 90)
student2 = Student("Jane", 22, 95)
print(f"{student1.get_name()} is {student1.get_age()} years old and scored {student1.get_score()}.")
print(f"{student2.get_name()} is {student2.get_age()} years old and scored {student2.get_score()}.")