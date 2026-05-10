# Mehedi Hasan Bhuiyan


class StudentDatabase:

    student_list = []
    
    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def view_all_students(cls):
        if len(cls.student_list) == 0:
            print("No student found.")
        else:
            for search in cls.student_list:
                search.view_student_info()

class Student:
    
    __counter = 1

    def __init__(self, name, department):
        self.__student_id = Student.__counter
        Student.__counter += 1

        self.__name = name
        self.__department = department
        self.__is_enrolled = False

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print("Student is already enrolled.")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Student is not enrolled.")
        else:
            self.__is_enrolled = False
            StudentDatabase.student_list.remove(self)
            print("Student dropped successfully.")

    def view_student_info(self):
        if self.__is_enrolled:
            status = "Enrolled"
        else:
            status = "Not Enrolled"
        print(f"Student Name: {self.__name}, Student ID: {self.__student_id}, "
                f"Department: {self.__department}, Status: {status}")

    def get_id(self):
        return self.__student_id



while True:
    print("\n\nWelcome to the Mehedi's Charity School")
    print("To View All Students: 1") 
    print("To Enroll Student: 2")
    print("To Drop Student: 3")
    print("To Exit: 4")

    choice = input("Enter your choice: ")

    if choice == "1":
        StudentDatabase.view_all_students()
        
    elif choice == "2":
        name = input("Student Name: ")
        dept = input("Department: ")

        student = Student(name, dept)
        student.enroll_student()
        print(f"Your Student ID is: {student.get_id()}")

    elif choice == "3":
        sid = input("Enter Student ID: ")

        found = False
        for s in StudentDatabase.student_list:
            if str(s.get_id()) == sid:
                s.drop_student()
                found = True
                break

        if not found:
            print("Invalid Student ID.")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
