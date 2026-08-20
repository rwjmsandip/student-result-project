
import numpy as np 

class Student:
    def __init__(self,id ,name,marks):
        self.id =id
        self.name = name
        self.__marks = marks

    def set_marks(self,marks):
        self.__marks = marks


    def display(self):
        arr = np.array(self.__marks)
        total = arr.sum()
        avg= arr.mean()
        per =(total/(len(arr)*100))*100 
        print("Student Id :" , self.id)
        print("Student name: " , self.name)
        print("Student marks: " , self.__marks)
        print("marks total: " , total)
        print("percentage : " , per)


class StudentManagementSystem:
    def __init__(self):
        self.Students=[
            Student(101,"ram",[12,36,45]),
            Student(102,"sham",[12,36,45])
        ]

       

    def add_student(self):
        while True:
            try:
                std_id = int(input("Enter student id "))

                if std_id>0:
                    for student in self.Students:
                        if student.id == std_id:
                            print("Already existing student.")
                            break
                    else:
                        break
                else:
                    print("student id must be greater than 0")

            except:
                print("Enter valid student id ")

        while True:
            try:
                name = input("Enter student name ").strip()

                if len(name)>=2 and len(name)<=50 and name.replace(" ","",50).isalpha():
                    break
                else:
                    print("Enter valid student name ")
            except:
                print("Enter valid student name")


        marks =[]
        subjects =["python","java","c"]

        for subject in subjects:
            while True:
                try:
                    mark = float(input(f"Enter the marks of {subject} = "))

                    if mark>=0 and mark<=100:
                        marks.append(mark)
                        break
                    else:
                        print("marks must be in between 0 to 100.")
                except:
                    print("Enter valid marks ")

        student =Student(std_id, name,marks)
        self.Students.append(student)

    def show_students(self):
        if len(self.Students) !=0:
            for student in self.Students:
                student.display()
        else:
            print("Student not found")

    def search_student(self):
        if len(self.Students) !=0:
            while True:
                try:
                    std_id = int(input("Seach student id "))

                    for student in self.Students:
                        if student.id == std_id:
                            student.display()
                            break
                        
                    else:
                        print("Student not found")
                        break
                    break
                except:
                    print("Enter valid id")
        else:
            print("No student data found!")

    def update_student(self):
        if len(self.Students) !=0:
            while True:
                try:
                    std_id =int(input("Enter student id "))

                    for student in self.Students:
                        if student.id == std_id:
                            while True:
                                print("1. update name")
                                print("2. update marks")
                                print("3. to stop program")

                                choice = int(input("Enter your choice between 1 to 3 "))

                                if choice ==1:
                                    new_name = input("Enter the new name ").strip()

                                    if len(new_name)>=2 and len(new_name)<=50 and new_name.replace(" ", "",50).isalpha():
                                        student.name = new_name
                                        print("Student name updated successfully.")
                                        break
                                    else:
                                        print("Enter valid name")

                                elif choice ==2:
                                    while True:
                                        print("1. update python marks")
                                        print("2. update java marks")
                                        print("3. update c marks")
                                        print("4. Exit.")

                                        ch= int(input("Enter your subject choice between 1 to 4 "))

                                        if ch == 1:
                                            mark = float(input("Enter python marks "))
                                            student._Student__marks[0]=mark
                                            student.display()
                                            print("python marks added successfully.")
                                            break
                             
                    else:
                        break

                except:
                    print("Enter valid student id")
        else:
            print("No data found")



 
 