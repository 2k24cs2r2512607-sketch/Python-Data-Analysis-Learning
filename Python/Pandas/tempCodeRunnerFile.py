class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id=None
        self.__fees=None

    # Setter methods
    def set_student_id(self, student_id):
        self.__student_id = student_id
    

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    # Getter methods
    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age
    def get_course_id(self):
        return self.__course_id 
    def get_fees(self):
        return self.__fees
    # Validation methods
    def validate_marks(self):
        if 0 <= self.__marks <= 100:
            return True
        return False

    def validate_age(self):
        if self.__age > 20:
            return True
        return False

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                return True
        return False
    def choose_course(self,course_id):
        if self.check_qualification() and course_id in (1001,1002):
                if course_id==1001:
                    if self.__marks>85:
                        self.__fees=25575.0-((25575.0*25)/100)
                    else:
                        self.__fees=25575.0
                else:
                    if self.__marks>85:
                        self.__fees=15500.0-((15500.0*25)/100)
                    else:
                        self.__fees=15500.0
                self.__course_id=course_id
                return True
        else:
            return False